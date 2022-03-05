from datetime import date, datetime
import sqlite3
from time import ctime
import db.conexao
from db.conexao import Conn

class Controle:

    def baterPonto():
        Conn.con
        data = datetime.today().date()
        time = datetime.today().time().isoformat('minutes')
        print(f'Dia {data} e hora {time}')

        

Controle.baterPonto()