from datetime import date, datetime
import imp
import sqlite3
from time import ctime
import db.conexao
from db.conexao import Conn
from classes.usuario import User

class Controle:

    def cadastrar(user: User):
        Conn.con

        pass

    def login():

        pass

    def baterPonto():
        Conn.con
        data = datetime.today().date()
        time = datetime.today().time().isoformat('minutes')
        print(f'Dia {data} e hora {time}')

        

Controle.baterPonto()