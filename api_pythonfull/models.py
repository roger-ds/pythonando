from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


USER = "postgres"
PASSWORD = "96020064"
HOST = "54.80.144.16"
PORT = 5432
DB = "teste"

CONN = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    email = Column(String(100))
    senha = Column(String(100))


class Tokens(Base):
    __tablename__ = "Tokens"    
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey("Pessoa.id"))
    token = Column(String(50))
    data = Column(DateTime, default=datetime.datetime.utcnow)


if __name__ == "__main__":
    Base.metadata.create_all(engine)