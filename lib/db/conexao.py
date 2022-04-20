from ast import Str
from msilib.schema import Class
import sqlite3

path = '.\lib\db\controleDeHoras.db'


class Conn:
    path = '.\lib\db\controleDeHoras.db'
    con = sqlite3.connect(path) 
    
    def conectar():
        try:
            con = sqlite3.connect(path)
            print('--db conectado')
            return con
        except Exception as e:
            print(e)
            return False


    def createTable():
        con = Conn.con
        cur = con.cursor()
        sql = open(".\lib\db\\tables.sql", 'r')
        print('--db Criando tabelas')
        lines = sql.readlines()
         
        for line in lines:
            
            cur.execute(line)


Conn.createTable()
