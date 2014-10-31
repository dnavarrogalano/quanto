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
import talib as ta
import pandas as pd
import numpy as np


class QAnalisys():
    def __init__(self):
        pass
    def strategy(self):
        pass


if __name__ == '__main__':
    symbol = Symbol('LAN')
    df = symbol.OCV('20140101')
    df['rsi'] = ta.RSI(df['Close'].values)
    df['ema'] = ta.EMA(df['Close'].values, timeperiod=5)
    print df.tail(20)

