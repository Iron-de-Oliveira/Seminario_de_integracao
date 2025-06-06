from flask_login import UserMixin
from database.cenexao import conectar

class Usuario(UserMixin):
    def __init__(self, idusuario, nome, email, senha, telefone, localizacao, foto_perfil):
        self.idusuario = idusuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.localizacao = localizacao
        self.foto_perfil = foto_perfil

    def get_id(self):
        return str(self.idusuario)

    def to_dict(self):
        return {
            "idusuario": self.idusuario,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "localizacao": self.localizacao,
            "foto_perfil":self.foto_perfil
        }

    @staticmethod
    def buscar_por_email(email):
        conn = conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT idusuario, nome, email, senha, telefone, localizacao, foto_perfil FROM usuario WHERE email = %s", (email,))
                dados = cursor.fetchone()
                if dados:
                    return Usuario(
                        idusuario=dados['idusuario'],
                        nome=dados['nome'],
                        email=dados['email'],
                        senha=dados['senha'],
                        telefone=dados['telefone'],
                        localizacao=dados['localizacao'],
                        foto_perfil=dados['foto_perfil']
                    )
        finally:
            conn.close()
        return None

    @staticmethod
    def buscar_por_id(idusuario):
        conn = conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario WHERE idusuario = %s", (idusuario,))
                dados = cursor.fetchone()
                if dados:
                    return Usuario(
                        idusuario=dados['idusuario'],
                        nome=dados['nome'],
                        email=dados['email'],
                        senha=dados['senha'],
                        telefone=dados['telefone'],
                        localizacao=dados['localizacao'],
                        foto_perfil=dados['foto_perfil']
                    )
        finally:
            conn.close()
        return None
