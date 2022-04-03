from datetime import date, datetime
import imp
from msilib.schema import Error
import sqlite3
from time import ctime
import db.conexao
from db.conexao import Conn
from classes.usuario import User
from dao.usuarioDAO import DaoUser

class Controle:

    def cadastrar():
        user =User()
        Conn.con
        user.email = input("digite seu email:")
        user.login = input("digite seu login:")
        user.senha = input("digite sua senha:")
        user.tel = input("digite seu telefone:")

        try:
            DaoUser.salvar(user)
        except Exception as e:
            print(e)
        
        

    def login():

        pass

    def baterPonto():
        Conn.con
        data = datetime.today().date()
        time = datetime.today().time().isoformat('minutes')
        print(f'Dia {data} e hora {time}')

        

Controle.cadastrar()