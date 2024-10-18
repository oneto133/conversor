from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError, IntegrityError
import csv
class Conexao:
    def __init__(self, nome_completo='', nome='', senha='', email=''):
        self.banco = create_engine('postgresql://postgres:M7cIWJYjxBodNojL@uncertainly-pretty-chimaera.data-1.use1.tembo.io:5432/postgres')
    
    def inserir_dados(self, nome_completo, nome, senha, email):
        try:
            with self.banco.connect() as conn:
                with conn.begin():
                    self.inserir_dados = text(f"INSERT INTO usuarios (nome_completo, nome_usuario, senha, email) VALUES ('{nome_completo}','{nome}', '{senha}', '{email}')")
                    conn.execute(self.inserir_dados)
                    return "executado com sucesso!"
        except OperationalError as e:
            return(f"Erro de conexão ou sintaxe SQL: {e}")
        except IntegrityError as e:
                return(f"Violação de integridade: {e}")
        except Exception as e:
            return(f"Erro inesperado: {e}")
    
class Query():
    def __init__(self, consulta=''):
        self.banco = create_engine('postgresql://postgres:M7cIWJYjxBodNojL@uncertainly-pretty-chimaera.data-1.use1.tembo.io:5432/postgres')
    
    def consultar_senha_por_usuario(self, consulta):
        try:
            with self.banco.connect() as conn:
                with conn.begin():
                    self.inserir_dados = text(f"select senha from usuarios where nome_usuario = '{consulta}'")
                    resultado = conn.execute(self.inserir_dados)
                    for row in resultado:
                        return self.tratar_resultado_de_consulta(row)
        except OperationalError as e:
            return(f"Erro de conexão ou sintaxe SQL: {e}")
        except IntegrityError as e:
                return(f"Violação de integridade: {e}")
        except Exception as e:
            return(f"Erro inesperado: {e}")

    def tratar_resultado_de_consulta(self, dado):
        self.dado = str(dado)
        return self.dado[2:-3]
            

if __name__ == '__main__':
    #adicionando dados
    '''conexao = Conexao()
    resultado = conexao.inserir_dados('Administrador', 'admin', 'admin', 'allmyfilesondrive@gmail.com')
    print(resultado)
'''
    #consultando dados  
    consulta = Query()
    resultado= consulta.consultar_senha_por_usuario('admin')
    print(resultado)

