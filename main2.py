from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid


db = create_engine('sqlite:///bancodedados.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# Criação da tabela
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha",String)
    telefone = Column("telefone",String)
    endereco = Column("ativo",String)
    cidade = Column("cidade",String)

    def __init__(self, id, nome, email, senha, telefone, endereco, cidade):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade




Base.metadata.create_all(bind=db)