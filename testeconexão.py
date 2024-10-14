from sqlalchemy import create_engine, text, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


# Substitua os valores entre as aspas simples pelas suas credenciais
db = create_engine('postgresql://postgres:M7cIWJYjxBodNojL@uncertainly-pretty-chimaera.data-1.use1.tembo.io:5432/postgres')

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

#Tabelas
class Usuariolivro(Base):
    __tablename__ = "usuariolivros"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__= 'livros'

    id = Column('id', Integer, primary_key=True)
    titulo = Column('titulo', String)
    qtde_paginas = Column('qtd_paginas', Integer)
    dono = Column('dono', ForeignKey('usuariolivros.id'))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono

Base.metadata.create_all(bind=db)


'''# Criar uma conexão
connection = engine.connect()

# Executar uma consulta (opcional)
sql = text("SELECT * FROM usuarios")
result = connection.execute(sql)
for row in result:
    print(row)

# Fechar a conexão
connection.close()'''

#adicionar usuario
'''usuario = Usuariolivro(nome = 'Neto', email='ksjsj@ksks.com', senha='1234')
session.add(usuario)
session.commit()'''


#lista_de_usuarios = session.query(Usuariolivro).all()
usuario_neto = session.query(Usuariolivro).filter_by(email='ksjsj@ksks.com').first()
print(usuario_neto.nome)

#adiicionar livro
'''livro = Livro(titulo='Guerra da ucrânia', qtde_paginas=65, dono=usuario_neto.id)
session.add(livro)
session.commit()'''



#atualização
usuario_neto.nome = 'Armando Neto'
session.add(usuario_neto)
session.commit()

#deletar
session.delete(usuario2)
session.commit()





