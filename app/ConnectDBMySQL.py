from sqlalchemy import create_engine

from MySQLdb.constants.CLIENT import LONG_PASSWORD

__author__ = 'DNG'

import _mysql
import sys




class ConnectDBMySQL():

    server = 'localhost'
    usuario = 'root'
    password = 'suba'
    basedatos = 'stocksdb'


    def __init__(self):
        server = 'localhost'
        usuario = 'root'
        password = 'suba'
        basedatos = 'stocksdb'

    def connectDB(self):
            con = _mysql.connect(server, usuario, password, basedatos)
            engine = create_engine('mysql://root:suba@localhost/stocksdb')
            return engine
