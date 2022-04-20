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
        
        Conn.con
        email = input("digite seu email:")
        login = input("digite seu login:")
        senha = input("digite sua senha:")
        tel = input("digite seu telefone:")
        user = User(email,login,senha,tel)
        try:
            
            DaoUser.salvar(user)
            print(user.toString())
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