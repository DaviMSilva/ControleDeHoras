from distutils.log import error

from classes.usuario import User
from db.conexao import Conn
class DaoUser:

    def salvar(user: User):
        sql = 'INSERT INTO tb_user (us_login, us_senha, us_email, us_tel) VALUES(?,?,?,?)'
        data= (user.toString())
        if Conn.conectar() != False:
            try:
                con = Conn.conectar()
                cur = con
                cur.execute(sql,data)
                cur.commit()
                print('salvo com sucesso')
            except Exception as e:
                print(e)
    
