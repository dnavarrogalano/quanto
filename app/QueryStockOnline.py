import numpy as np
import sqlite3
import datetime
import json
import urllib2
import urllib
from sqlalchemy import create_engine
import ConnectDBMySQL as cnx
from itertools import chain


CONNECTIONSTRING = 'mysql://root:suba@localhost/stocksdb'

folder = 'E:\\virtualenv\\Quanto_Backend\\Quanto\\stocks\\'
folder2 = 'E:\\virtualenv\\Quanto_Backend\\Quanto\\stocks\\'


#class QueryStockOnline():

def conectaDB():

    return create_engine(CONNECTIONSTRING)


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

def traeIndicadoresxInstrumento ( nemo, fechaINI, fechaFIN = 0 ):
    
    conn = conectaDB()
   # query = "select  Fechanum*1000 , Close, bol_up, bol_down ,volume , sma200, sma50, sma10 from t_indicadores where nemo = '%s' and fecha >= %s order by fechanum" 
    query = "select  Fechanum*1000 , Close, bol_up, bol_down ,volume , sma200, sma50, sma10 from t_indicadores where nemo = '%s' and fecha >= %s  order by fechanum" 
    
    cursor = conn.execute(query % (nemo , fechaINI) )
    ss =   np.array(cursor.fetchall())
    fechanum = ss[0:,0]
    valorClose = ss[0:,1]
    bol_up = ss[0:,2]
    bol_down = ss[0:,3]
    volume = ss[0:,4]
    sma200 = ss[0:,5]
    sma50 = ss[0:,6]
    sma10 = ss[0:,7]


    return np.column_stack((fechanum, valorClose)) , np.column_stack((fechanum, bol_up)) , np.column_stack((fechanum, bol_down)), \
    np.column_stack((fechanum, volume)), np.column_stack((fechanum, sma200)) \
    , np.column_stack((fechanum, sma50)) \
    , np.column_stack((fechanum, sma10))


def grabaRegistros(self ,t,nombreTabla):

    engine = create_engine('mysql://root:suba@localhost/stocksdb')


    #con = self.conectaDB()
   # pd.io.sql.write_frame(t, nombreTabla, con, if_exists="append")
    pd.io.sql.to_sql(t, nombreTabla, engine, flavor='mysql', if_exists="append",)



if __name__ == "__main__":
    print "ok"







