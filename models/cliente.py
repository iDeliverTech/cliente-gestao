from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from models import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    email = Column(String(120), unique=True)
    nome = Column(String(100))
    idade = Column(Integer)
    cpf = Column(String(14), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, email: str, nome: str, idade: int, cpf: str, data_insercao: Union[DateTime, None] = None):
        """
        Cria um cliente

        Arguments:
            email: email.
            nome: nome
            idade : idade
            cpf: cpf
            data_insercao: data de quando o cliente foi inserida à base
        """
        self.email = email
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
