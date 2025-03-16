from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import uuid

# Configuração do banco de dados SQLite
db = create_engine('sqlite:///bancodedados.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# Criação da tabela
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=db)



