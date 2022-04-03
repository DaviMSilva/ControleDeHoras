from ast import Str
from msilib.schema import Class
import sqlite3

path = '.\lib\db\controleDeHoras.db'
con = sqlite3


class Conn:
    path = '.\lib\db\controleDeHoras.db'
    con = sqlite3.connect(path) 
    
    def createTable():
        con = Conn.con
        cur = con.cursor()
        sql = open(".\lib\db\\tables.sql", 'r')
        print('--db conectado')
        lines = sql.readlines()
         
        for line in lines:
            
            cur.execute(line)



Conn.createTable()