import urllib2
import urllib
import codecs
import numpy as np
import pandas as pd
import sqlite3
folder='D:\\DEV\\stocks\\'
import simplejson as json
#stocks=["AA","AAPL","AAXJ","ABT","ACWI","ACWX","ADP","AESGENER","AFPCAPITAL","AGRICULTOR","AGUAS-A","AGUAS-B","AGUNSA","AIG","AKOA-CL","AKOB-CL","ALMENDRAL","AMGN","AMZN","ANASAC","ANDACOR","ANDINA-A","ANDINA-B","ANTARCHILE","AQUACHILE","ATSA","AUSTRALIS","AVP","AXP","AXXION","AZULAZUL","BA","BAC","BANMEDICA","BANVIDA","BBVACL","BCI","BESALCO","BETLANDOS","BICECORP","BIIB","BKF","BLUMAR","BRF","BSANTANDER","BTU","C","CALICHERAA","CALICHERAB","CAMANCHACA","CAMPOS","CANALISTAS","CAP","CAROZZI","CARVILE","CASABLANCA","CASGEN","CAT","CCT","CCU","CDCRAIG-A","CDCRAIG-B","CEM","CEMENTOS","CENCOSUD","CFMITNIPSA","CFR","CGE","CGEDISTRO","CHILE","CHILECTRA","CHOLGUAN","CIC","CINTAC","CLUBCAMPO","CLUBUNION","CMCSA","CMPC","COLBUN","COLCRAIG-A","COLCRAIG-B","COLINSE","COLOCOLO","COLOSO","COLX","COMERCIO","CONCHATORO","CONSOGRAL","COPEC","COPEVAL","CORPBANCA","CORPESCA","COST","COUNTRY-A","COUNTRY-B","COUNTRY-P","COVADONGA","CPK","CRAIGHOUSE","CRISTALES","CRUZADOS","CRUZBLANCA","CSCO","CTC-A","CTC-B","CTC-MUNDO","CTISA","CU-CL","CUPRUM","CVA","CVS","CVX","DD","DEHESA","DETROIT","DIS","DTV","DUNCANFOX","EBAY","ECH","ECL","ECNS","EDELMAG","EDELPA","EEM","EFA","EGPT","EIDO","EIRL","EIS","EISA","ELECDA","ELECDA-SD","ELECMETAL","ELIQSA","ELIQSA-SD","EMAG","EMBONOR-A","EMBONOR-B","EMC","EMELARI","EMELARI-SD","EMILIANA","EMLC","ENACAR","ENAEX","ENDESA","ENDESPAN","ENERSIS","ENJOY","ENLASA","ENTEL","ENZL","EPERVA","EPHE","EPOL","EPP","EPU","ERUS","ESPANA","ESPANOLA","ESPANOLVAL","ESR","ESRX","ESSAL-A","ESSAL-B","ESSBIO-A","ESSBIO-B","ESSBIO-C","ESTACIONAM","ESVAL-A","ESVAL-B","ESVAL-C","EWA","EWC","EWG","EWH","EWI","EWJ","EWL","EWM","EWN","EWP","EWQ","EWS","EWT","EWU","EWW","EWY","EWZ","EWZS","EZA","EZU","FALABELLA","FASA","FB","FCX","FEPASA","FERIAOSOR","FORUS","FOSFOROS","FROWARD","FXI","GASCO","GDX","GDXJ","GE","GENERADORA","GERJ","GEX","GILD","GOLF","GOOGL","GPK","GRANADILLA","GRANGE-A","GRANGE-B","HABITAT","HAL","HAP","HD","HF","HIPERMARC","HIPICO","HIPODROMOA","HIPODROMOB","HITES","HON","HORNOS","HPQ","HYG","IACSA","IAM","IANSA","IAU","IBM","IDU","IDX","IEV","ILC","ILF","INDISA","INDIVER","INDY","INFODEMA","INGEVEC","INMOBVINA","INTASA","INTC","INTEROCEAN","INVERCAP","INVERFOODS","INVERMAR","INVERNOVA","INVEXANS","INVIESPA","IPAL","IQUIQUE","ISANPA","ITB","IVE","IVV","IVW","IWB","IWC","IWD","IWF","IWM","IWN","IWO","IWP","IWR","IWS","IWV","IXC","IXG","IYC","IYE","IYF","IYJ","IYK","IYM","IYR","IYW","IYZ","JNJ","JPM","KO","KOL","LAN","LASCONDES","LATM","LEASNAC","LFL-CL","LINDEFUT","LITORAL","LNKD","LQD","MAISONNETT","MARBELLACC","MARGARET'S","MARINSA","MASISA","MCD","MCHI","MDLZ","MELON","MINERA","MMM","MO","MOLLER","MOLYMET","MOO","MRK","MS","MSFT","MUELLES","MULTIFOODS","MXI","NAVARINO","NAVIERA","NEM","NIBSA","NITRATOS","NKE","NLR","NORTEGRAN","NUEVAPOLAR","NUEVAREG","OLDBOYS","ORCL","OROBLANCO","PACIFICO","PARAUCO","PASUR","PAZ","PCLN","PEHUENCHE","PEK","PEP","PFE","PG","PILMAIQUEN","PLANVITAL","PLND","POLO","POLPAICO","POTASIOS-A","POTASIOS-B","PREVISION","PROVIDA","PUCOBRE-A","PUCOBRE-C","PUCOBRE-D","PUERTO","PUNTILLA","PUYEHUE","QCOM","QUEMCHI","QUILICURA","QUINENCO","REBRISA-A","REBRISA-B","REMX","RIPLEY","RSX","RSXJ","SALFACORP","SANPEDRO","SANTARITA","SANTANA","SANTANGRUP","SBUX","SCHWAGER","SCIF","SCJ","SCZ","SECURITY","SHV","SHY","SIEMEL","SINTEX","SIPSA","SIXTERRA","SK","SLV","SLX","SM-CHILEA","SM-CHILEB","SM-CHILED","SM-CHILEE","SMSAAM","SOCOVESA","SOFRUCO","SONDA","SOPROCAL","SOQUICOM","SPLS","SPORTFRAN","SPORTING","SQM-A","SQM-B","STADITALIA","SUDAMER-A","T","TATTERSALL","TECHPACK","TELSUR","TGT","THD","TIP","TRICAHUE","TRV","TUR","TXN","UNESPA","UNH","UNIONGOLF","UNP","UPS","USB","UTX","V","VALORES","VAPORES","VCMAC1","VCMBC1","VENTANAS","VICONTO","VNM","VOLCAN","VZ","WATTS","WFC","WMT","WMTCL","X","XOM","YHOO","YUGOSLAVA","ZOFRI"]


def traeStock(stockName):
          
        u = {'Symbol' : stockName}  
        u = urllib.urlencode(u) 
        print "u : " , u

        url = 'http://www.bolsadesantiago.cl/Theme/Data/Historico.aspx?' + u + '&dividendo=S'

        print url 

        f = urllib2.urlopen(url)
        
        guarda = codecs.decode(f.read(),'utf-16').replace(',','.')
        
        output = codecs.open(folder + stockName + '.stk','w', 'utf-8')

        output.write(guarda)
        output.close()

'''function linkNemo() 
	{
		var url = '/theme/resumenInstrumento.aspx?nemo=';    
		var texto = document.getElementById('buscadorNemo');
		window.location.href = url + texto.value.toString();     
	}	
'''

def verificaArchivoStock(stockName):
    fileInput  = codecs.open(folder + stockName + '.stk','rb')
    print fileInput.read()


def pronostico(X_digits , y_digits):

    from scikits.learn import datasets, neighbors, linear_model
    from sklearn.ensemble import RandomForestClassifier
    from collections import deque
    #digits = datasets.load_digits()
    classif = RandomForestClassifier()
    changes = np.diff(X_digits) > 0

    X_train=changes[:-1] # Add independent variables, the prior changes
    y_train=changes[-1] # Add
    classif.fit(X_train, y_train) # Generate the model
            
    prediction = classif.predict(changes[1:]) # Predict
    
    print prediction
    return

    
    n_samples = len(X_digits)





    X_train = X_digits[:.9*n_samples]
    y_train = y_digits[:.9*n_samples]
    
    #print X_train, y_train
    X_test = X_digits[.9*n_samples:]
    y_test = y_digits[.9*n_samples:]
    


   # knn = neighbors.NeighborsClassifier()
    logistic = linear_model.LogisticRegression()

    #print 'KNN score:', knn.fit(X_train, y_train).score(X_test, y_test)
    print 'LogisticRegression score:', logistic.fit(X_train, y_train).score(X_test, y_test)


def abreArchivo(stockName):
    archivoDatos = codecs.open(folder + stockName + '.stk','r' )

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

    #date, openp, highp, lowp, closep,  volume = np.loadtxt(stockFile,delimiter=';', unpack=True
                                                               #   converters={ 0: mdates.strpdate2num('%Y%m%d')})
    
    return pd.read_csv(folder + stockName + ".stk", skiprows=2, delimiter=';')

    #variation = closep - openp

    #pronostico(closep, date )

'''    newAr = []
    while x < y:
        appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
        newAr.append(appendLine)
        x+=1
    '''



def conectaDB():
    return  sqlite3.connect("d:/dev/stocks/stocks.sqlite")
    
def grabaRegistros(t):
        
    con = sqlite3.connect("d:/dev/stocks/stocks.sqlite")
    
    print "a grabar...."
    pd.io.sql.write_frame(t, "t_ohlcv", con, if_exists="append")
    print "ok"
   

def cargaArchivoAtablaOHLCV():

    #con = conectaDB()# sqlite3.connect("d:/dev/stocks/stocks.sqlite")
    #con.execute("DROP TABLE IF EXISTS t_ohlcv")
    #con.close()
    archivoStock = open(folder + 'listadoIPSA.dat')
    splitLines = archivoStock.read().split('\n')
    archivoStock.close
    for x in splitLines:
            f = abreArchivo(x)
            f['NANO']=x
            grabaRegistros(f)
            
        #traeStock(x)
        #verificaArchivoStock(x)

def consultaOHLCV(nemo, fechaini, fechafin=0):
        q = """select NANO, Fecha, Close, Volume from t_ohlcv
                where NANO = %s and Fecha >= """, nemo, fechaini
        con = conectaDB()
        con.execute(q)
        cursor = con.fetchall()
        print cursor

#df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, 
#                 index_col=['id', 'date_time'])

if __name__ == '__main__':
        print "ok"        
        nemo = 'CENCOSUD'
        fechaini = 20140101
        q = """select Fecha, Close
        from 
        t_ohlcv
              where NANO = '""" + nemo + """'  and Fecha >= """ + str(fechaini)
        print q
        con = conectaDB()
        cursor = con.execute(q)
        #cursor = con.cursor()
        json_string = json.dumps(dict(cursor.fetchall()))
        #records =  cursor.fetchall()
        print json_string









