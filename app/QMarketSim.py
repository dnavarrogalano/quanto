#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DNG
#
# Created:     31-10-2014
# Copyright:   (c) DNG 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from QueryStock import Symbol
import QAnalisys as qa
import talib as ta
import pandas as pd
import numpy as np


class QMarketsim():
    def __init__(self,inicioPeriodo, finPeriodo):
        self._fecInicio = inicioPeriodo
        self._fecTermino = finPeriodo
    def simularPeriodo(self):
        arr = []
        portfolio = 0
        valorP = 0
        n = 50
        valorV = 0
        symbol = Symbol('LAN')
        df = symbol.OCV(self._fecInicio)
        df['rsi'] = ta.RSI(df['Close'].values)
        df['ema5'] = ta.EMA(df['Close'].values, timeperiod=5)
        df['ema15'] = ta.EMA(df['Close'].values, timeperiod=15)
        i=0
        da = None
        df['orden']=''
        for  dia in df.index:
           i+=1
           d = df.loc[dia]
           if i > 1:
             if d.ema5 > da.ema15 and  da.ema5 < da.ema15 and d.ema5 > da.ema5 and d.Close:
                print "compra" , d.Close, dia
                valorP += d.Close * n
                portfolio +=n
             if d.ema5 < da.ema15 and  da.ema5 > da.ema15 and d.ema5 < da.ema5 and portfolio > n:
                print "Venta" , d.Close*n, dia
                valorV += d.Close
                portfolio -=n
           da = d
        print "-------------------------------------------------------"
        print '\n'
        print "portfolio", portfolio
        print "Total ", valorV-valorP













    def strategy():
        pass


if __name__ == '__main__':
    qs = QMarketsim(20100101, 0)
    sim = qs.simularPeriodo()


