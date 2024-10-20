from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.exc import OperationalError, IntegrityError
from sqlalchemy import select, text
import csv
import asyncio
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
        self.async_engine = create_async_engine('postgresql+asyncpg://postgres:M7cIWJYjxBodNojL@uncertainly-pretty-chimaera.data-1.use1.tembo.io:5432/postgres')
        self.async_session = async_sessionmaker(self.async_engine, expire_on_commit=False)

    async def consultar_senha_por_usuario(self, consulta):
        try:
            async with self.async_session() as conn:
                inserir_dados = text(f"select senha from usuarios where nome_usuario = '{consulta}'")
                result = await conn.execute(inserir_dados)
                
                for row in result:
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
    async def main():
        consulta = Query()
        resultado= await consulta.consultar_senha_por_usuario('admin')
        print(resultado)
    asyncio.run(main())

