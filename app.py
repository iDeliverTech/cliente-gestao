from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from models import Session, Cliente
from logger import logger
from schemas import *
from flask_cors import CORS

import requests

info = Info(title="API destinada para o projeto iDeliverTech, Microsserviço responsável pelo gerenciamento de clientes ", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(
    name="Cliente", description="Adição, alteração, visualização e remoção de clientes da base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/cadastrar_cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def cadastrar_cliente(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados

    Retorna uma representação dos clientes.
    """
    cliente = Cliente(
        email=form.email,
        nome=form.nome,
        idade=form.idade,
        cpf=form.cpf
    )
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando cliente
        session.add(cliente)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cliente de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"message": error_msg}, 400
    

@app.get('/buscar_clientes', tags=[cliente_tag],
         responses={"200": ListagemClientesSchema, "404": ErrorSchema})
def buscar_clientes():
    """Faz a busca por todos os clientes cadastrados

    Retorna uma representação da listagem de clientes.
    """
    logger.debug(f"Coletando clientes ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    clientes = session.query(Cliente).all()

    if not clientes:
        # se não há clientes cadastrados
        return {"clientes": []}, 200
    else:
        logger.debug(f"%d clientes encontrados" % len(clientes))
        # retorna a representação de clientes
        print(clientes)
        return apresenta_clientes(clientes), 200
    

@app.get('/buscar_cliente_cpf', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def buscar_cliente_cpf(query: ClienteBuscaSchema):
    """Faz a busca por um cliente a partir do cpf do cliente

    Retorna uma representação dos clientes.
    """
    cliente_cpf = query.cpf
    logger.debug(f"Coletando dados sobre cliente #{cliente_cpf}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.cpf == cliente_cpf).first()

    if not cliente:
        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao buscar cliente com cpf '{cliente_cpf}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Cliente econtrado: '{cliente.nome}'")
        # retorna a representação de cliente
        return apresenta_cliente(cliente), 200
    

@app.delete('/deletar_cliente', tags=[cliente_tag],
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def deletar_cliente(query: ClienteBuscaSchema):
    """Deleta um Cliente a partir do cpf do cliente informado

    Retorna uma mensagem de confirmação da remoção.
    """
    cliente_cpf = unquote(unquote(query.cpf))
    print(cliente_cpf)
    logger.debug(f"Deletando dados sobre cliente #{cliente_cpf}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cliente).filter(Cliente.cpf == cliente_cpf).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado cliente #{cliente_cpf}")
        return {"message": "Cliente removido", "cpf": cliente_cpf}
    else:
        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente #'{cliente_cpf}', {error_msg}")
        return {"message": error_msg}, 404


