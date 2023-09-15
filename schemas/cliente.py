from pydantic import BaseModel
from typing import List
from models.cliente import Cliente


class ClienteSchema(BaseModel):
    """ Define como um cliente deve ser representado
    """
    email: str = "abc@gmail.com"
    nome: str = "abc@gmail.com"
    idade: float = 78.90
    cpf: str = "000.000.000-00"


class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no cpf do cliente
    """
    cpf: str = "000.000.000-00"


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: cliente.
    """
    id: int = 1
    email: str = "abc@gmail.com"
    nome: str = "abc@gmail.com"
    idade: float = 78.90
    cpf: str = "000.000.000-00"



class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    clientes: List[ClienteViewSchema]


class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    numero_entrega: str


def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação de clientes seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "email": cliente.email,
            "nome": cliente.nome,
            "idade": cliente.idade,
            "cpf": cliente.cpf
        })

    return {"clientes": result}


def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação de um cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "email": cliente.email,
        "nome": cliente.nome,
        "idade": cliente.idade,
        "cpf": cliente.cpf
    }
