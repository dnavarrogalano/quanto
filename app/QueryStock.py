import numpy as np
import pandas as pd
import sqlite3
import datetime
import json
import urllib2
import urllib
import codecs
from sqlalchemy import create_engine
import ConnectDBMySQL as cnx
from pandas.io import sql

folder = 'E:\\virtualenv\\Quanto_Backend\\Quanto\\stocks\\'
folder2 = 'E:\\virtualenv\\Quanto_Backend\\Quanto\\stocks\\'


class BaseDatos():

    def conectaDB(self):
		#return  sqlite3.connect("d:/dev/stocks/stocks.sqlite")

        return cnx.ConnectDBMySQL()

    def consultaOHLCV(self, nemo, fechaINI, fechaFIN):
            q = """select  unix_timestamp(Fecha)   Fechanum, Fecha ,Close , Volume from  t_ohlcv where NANO = '""" \
                + nemo + """'  and Fecha >= """ + str(fechaINI)
            con = self.conectaDB()
            #cursor = con.execute(q)
            engine = create_engine('mysql://root:suba@localhost/stocksdb')
            df = pd.read_sql_query(q, engine)
            #df = pandas.DataFrame(cursor.fetchall())

#			json_string = json.dumps(dict(cursor.fetchall()))
#			con.close()
#			return json_string
            return df


    def cargaArchivoAtablaOHLCV(self, x):


        #archivoStock = open(folder + 'listadoIPSA.dat')
        #splitLines = archivoStock.read().split('\n')
        #archivoStock.close
        #for x in splitLines:
        #        print x
        f = pd.DataFrame(self.abreArchivo(x))
        f['NANO']=x
        self.grabaRegistros(f, "t_ohlcv")


    def traeStockBCSHistorico(self ,stockName):

        u = {'Symbol' : stockName}
        u = urllib.urlencode(u)
        print "u : " , u

        url = 'http://www.bolsadesantiago.cl/Theme/Data/Historico.aspx?' + u + '&dividendo=S'

        print url

        f = urllib2.urlopen(url)

        guarda = codecs.decode(f.read(),'utf-16').replace(',','.')

        output = codecs.open(folder2 + stockName + '.stk','w', 'utf-8')

        output.write(guarda)
        output.close()


    def abreArchivo(self ,stockName):
        archivoDatos = codecs.open(folder2 + stockName + '.stk', 'r')

        #data = np.genfromtxt(archivoDatos,skiprows=3)
        #data = np.fromfile(archivoDatos.read())

        stockFile =[]
        try:
                sourceCode = codecs.open(folder + stockName + '.stk','rb').read()
                splitSource = sourceCode.split('\n')
                for eachLine in splitSource[4:]:
                    splitLine = eachLine.split(';')
                    if len(splitLine)==6:
                        if 'values' not in eachLine:
                            stockFile.append(eachLine)

        except Exception, e:
                print str(e), 'failed to organize pulled data.'

        return pd.read_csv(folder2 + stockName + ".stk", skiprows=2, delimiter=';')

    def cargaDataFrameaBD(self,DF, nombreTabla, drop = False):

        con = self.conectaDB()   # sqlite3.connect("d:/dev/stocks/stocks.sqlite")
        #drop = True
        if drop:
            con.execute("DROP TABLE IF EXISTS " + nombreTabla)

        self.grabaRegistros(DF,nombreTabla)

    def grabaRegistros(self ,t,nombreTabla):

        engine = create_engine('mysql://root:suba@localhost/stocksdb')


        #con = self.conectaDB()
       # pd.io.sql.write_frame(t, nombreTabla, con, if_exists="append")
        pd.io.sql.to_sql(t, nombreTabla, engine, flavor='mysql', if_exists="append",)


class QueryStock():



        def sma(self, prices, n_periods):
            """
            Returns the rolling mean of a given list of stock prices "prices"
            over a period of time "n_periods". Interfaces with Pandas, so the details are
            sort of unknown to me.

            n_periods, for a typical SMA, is equivalent to the "days" it spans.
            So for a 50-day SMA, n_periods is equal to 50.

            Accepts: Array; integer.
            Return type: Array.
            """
            sma = pd.rolling_mean(prices, n_periods, min_periods=n_periods)
            return sma  # Returns a Numpy array in this case


        def bollinger_upper(self, prices, sma, n_periods):
            """
            Returns the upper Bollinger band line, for implementing a Bollinger
            band into the plot. Uses the list of stock prices "prices",
            the rolling mean returned by sma() "sma", over a number of periods "n_periods".
            You must use the same number of periods as used in the associated sma() function.
            Accepts: Array; array; integer.
            Return type: Array.
            """
            stdev = pd.rolling_std(prices, n_periods, min_periods=n_periods)
            return sma + (2 * stdev)  # Returns a Numpy Array in this case


        def bollinger_lower(self, prices, sma, n_periods):
            """
            Returns the lower Bollinger band line, for implementing a Bollinger
            band into the plot. Uses the list of stock prices "prices",
            the rolling mean returned by sma() "sma", over a number of periods "n_periods".
            You must use the same number of periods as used in the associated sma() function.
            Accepts: Array; array; integer.
            Return type: Array.
            """
            stdev = pd.rolling_std(prices, n_periods, min_periods=n_periods)
            return sma - (2 * stdev)  # Returns a Numpy Array in this case


        def stackify(x, y):
            """
            Stacks two arrays of data together. Used with Bollinger bands, at least for Bokeh.

            For example, in Bollinger bands, x would be the upper band data (which gets reversed)
            and y would be the lower band data (which has the reversed upper data appended).
            This would supply the y coordinates.

            The function still needs a little more work, since it's not very generalized.
            (Especially since it assumes the input is an array.)
            Accepts: Array 1; Array 2.
            Return type: Array.
            """

            stack = np.append(y, x[::-1])
            return stack


        def rsi(self , prices , timeframe=14):
            """
            Returns the Relative Strength Index for a list of stock prices "prices"
            over a period of time "timeframe".
            Code shamelessly stolen from Sentdex. Sorry!

            Accepts: Array; integer (optional).
            Return type: Array.
            """

            delta = np.diff(prices)
            seed = delta[:timeframe + 1]

            up = seed[seed >= 0].sum() / timeframe
            down = -seed[seed < 0].sum() / timeframe

            rs = up / down

            rsi = np.zeros_like(prices)
            rsi[:timeframe] = 100. - (100. / (1. + rs))

            for i in range(timeframe, len(prices)):

                i_delta = delta[i - 1]

                if i_delta > 0:
                    upval = i_delta
                    downval = 0.
                else:
                    upval = 0.
                    downval = -i_delta

                up = (up * (timeframe - 1) + upval) / timeframe
                down = (down * (timeframe - 1) + downval) / timeframe

                rs = up / down
                rsi[i] = 100. - (100. / (1. + rs))

            return rsi  # Returns a Numpy Array.


        def ema(self, prices, n_periods):
            """
            Returns the exponentially weighted moving average of a given SMA "sma".

            A MACD requires a 12-day EMA, a 26-day EMA, and a 9-day EMA.
            When writing an EMA, we need to figure out how to say "give me an n-day EMA".
            n_periods is the number of days you want it to span.
            So, a 12-day EMA would have n_periods=12.

            Accepts: Array; float.
            Return type: Array.
            """

            span = n_periods

            ema = pd.ewma(prices, span=span)
            return ema


        def macd_line(self, prices):
            """
            Returns the Moving Average Convergence-Divergence (MACD) of a given set of price data.
            This is the main line for plotting on a chart.

            Accepts: Array.
            Return type: Array.
            """

            ema12 = pd.ewma(prices, span=12)
            ema26 = pd.ewma(prices, span=26)

            macd = ema12 - ema26
            return macd


        def macd_signal(self ,prices):
            """
            Returns the MACD signal line of a given set of price data.

            Accepts: Array.
            Return type: Array.
            """

            ema9 = pd.ewma(prices, span=9)

            return ema9


        def macd_hist(self ,prices):
            """
            Returns the MACD histogram data for a given set of price data.

            Accepts: Array.
            Return type: Array.
            """

            ema9 = pd.ewma(prices, span=9)
            ema12 = pd.ewma(prices, span=12)
            ema26 = pd.ewma(prices, span=26)

            hist = (ema12 - ema26) - ema9
            return hist



        def stdev(self, prices, n_periods = 5):
             s = pd.rolling_std(prices, n_periods, min_periods=n_periods)
             return s

        def diferencial(self ,prices):
            return prices


        def procesaNemo(self, nemo, fechaIni, fechaFin):
            bd = BaseDatos()
            f = bd.consultaOHLCV(nemo, fechaIni, fechaFin)

            f["nemo"] = nemo
            sma = self.sma(f["Close"].values, 200)
            f["sma200"] = np.nan_to_num(sma)
            sma = self.sma(f["Close"].values, 50)
            f["sma50"] = np.nan_to_num(sma)
            sma = self.sma(f["Close"].values, 10)
            f["sma10"] = np.nan_to_num(sma)
            #def bollinger_upper(_self, prices, sma, n_periods):
            f["bol_UP"] = np.nan_to_num(self.bollinger_upper(f["Close"].values, sma, 2))
            #def bollinger_lower(_self, prices, sma, n_periods):
            f["bol_DOWN"] = np.nan_to_num(self.bollinger_lower(f["Close"].values, sma, 2))
            #def rsi(prices, timeframe=14):
            try:
                rrrsi = self.rsi(f["Close"].values)
                where_are_NaNs = np.isnan(rrrsi)
                rrrsi[where_are_NaNs] = 0
                f["RSI"] = rrrsi
            except:
                pass
            #def stdev(_self, prices, n_periods = 5):
            f["stdev"] = np.nan_to_num(self.stdev(f["Close"], 2))

            bd.grabaRegistros(f, "t_indicadores")

