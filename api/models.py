from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


USER = "postgres"
PASSWORD = "96020064"
HOST = "database-teste.ctvh5h8ilrad.us-east-1.rds.amazonaws.com"
PORT = 5432
DB = "aula_fastAPI"

CONN = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))


class Tokens(Base):
    __tablename__ = "Tokens"    
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey("Pessoa.id"))
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow)


Base.metadata.create_all(engine)