# Microsserviço B - Cliente-Gestao
Este repositório abrigará o código e os recursos associados ao microsserviço responsável pelo gerenciamento das informações dos clientes em seu sistema.

> É de suma importância que este Microsserviço seja iniciado após o Microsserviço A (Entrega-Gestão) para garantir que ambos estejam na mesma rede e possam se comunicar.


&nbsp;


---


## Como executar via Docker 
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.


&nbsp;


Este comando constrói uma imagem Docker com a tag `ideliver-tech-cliente:1.0` a partir do contexto atual (diretório atual).
```
docker build -t ideliver-tech-cliente:1.0 .
```


&nbsp;


Este comando executa um contêiner Docker com o nome `ideliver-cliente`, usando a imagem `ideliver-tech-cliente:1.0`. Ele define a variável de ambiente `DOCKER_ENV` como true, mapeia a porta 5001 do host para a porta 5001 do contêiner e conecta o contêiner à rede `rede-deliver`. Isso permite que sua aplicação seja executada em um ambiente Docker configurado adequadamente, pronto para se comunicar com outros microserviços na mesma rede.
```
docker run -e DOCKER_ENV=true -p 5001:5001 --name ideliver-cliente --network rede-deliver ideliver-tech-cliente:1.0
```
> É de suma importância que o Microsserviço A seja iniciado antes do Microsserviço B (Cliente-Gestão), uma vez que ambos compartilham a mesma rede `rede-deliver`. Certifique-se de que o Microsserviço A esteja em execução para garantir uma comunicação eficaz entre os dois microserviços.


&nbsp;


> Após a execução dos comandos passados, Abra o http://127.0.0.1:5001/#/ no navegador desejado.

---


&nbsp;


## Como executar por via linha de comando

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).


&nbsp;


Execute o seguinte comando para utilizar o ambiente virtual.

```
(Unix/macOS)
$ source env/Scripts/activate

(Windows)
$ .\env\Scripts\activate
```

&nbsp;


Estando no ambiente virtual, execute o comando abaixo:

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.


&nbsp;


> Caso ocorra algum erro de instalação com greenlet, execute o seguinte comando:

```
(env)$ pip install greenlet
```

Este comando instala a biblioteca, chamada Greenlet que permite a execução de tarefas concorrentes de forma controlada em um único thread.


&nbsp;


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```


&nbsp;


Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução. 
