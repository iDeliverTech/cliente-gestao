# Definindo a imagem Python 3.8
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner como /app
WORKDIR /app

# Copia todos os arquivos e pastas do diretório local para /app no contêiner
COPY . /app

# Instala as dependências listadas no arquivo requirements.txt
RUN pip install -r requirements.txt

# Informa ao Docker que o contêiner escutará na porta 5001 (documentação)
EXPOSE 5001

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "app.py"]

# docker build -t ideliver-tech-cliente:1.0 .
# docker run -e DOCKER_ENV=true -p 5001:5001 --name container-cliente --network rede-deliver ideliver-tech-cliente:1.0