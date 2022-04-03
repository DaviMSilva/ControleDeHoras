from distutils.log import error
from msilib.schema import Error
from classes.usuario import User
from db.conexao import Conn
class DaoUser:

    def salvar(user: User):
        sql = 'INSERT INTO tb_user(login, senha, email, tel) VALUES(?,?,?,?)'
        data= (user.getLogin(),user.getSenha(), user.getEmail(), user.getTel())
        con = Conn.con
        cur = con.cursor()

        try:
            cur.execute(sql,data)
            print('salvo com sucesso')
        except Exception as e:
            print(e)
    
