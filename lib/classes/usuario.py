
class User:

    def __init__(self, email, login,senha,tel) -> None:
        
        self.email = email
        self.login = login
        self.senha = senha
        self.tel = tel
    
    def getLogin(self):

        return self.login
    
    def getSenha(self):
        return self.senha

    def getEmail(self):
        return self.email

    def getTel(self):
        return self.tel

    def setLogin(self,login):
        self.login = login

    def setSenha(self,senha):
        self.senha=senha

    def setEmail(self, email):
        self.email = email

    def setTel(self, tel):
        self.tel =tel
    
    def toString(self):
        return (self.login,self.senha,self.email,self.tel)