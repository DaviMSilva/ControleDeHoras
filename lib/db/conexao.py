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
        tb_horas = 'CREATE TABLE IF NOT EXISTS tb_horas (id INTEGER PRIMARY KEY AUTOINCREMENT, data text(10), e1_hora text, s1_hora text, e2_hora text, s2_hora text)'
        sql = open(".\lib\db\\tables.sql", 'r')

        lines = sql.readlines()
         
        for line in lines:
            cur.execute(line)



Conn.createTable()