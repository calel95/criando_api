#CONFIG DO DOCKER PARA RODAR COM O DOCKER-COMPOSE

# #imagem
# FROM python:3.12

# #instala o sqlite
# #RUN apk add --no-cache sqlite sqlite-dev

# #diretorio de trabalho do container
# WORKDIR /app

# #Copia arquivos de dependencias e instala
# COPY  requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# #copia o restante dos arquivos do projeto
# COPY . /app

# #comando para executar a aplicacao
# CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
# -----------------------------------------------------------------------------
#CONFIG DO DOCKER PARA RODAR NO RENDER NA VERSAO FREE
FROM python:3.12

# Instalando o Poetry
RUN pip install poetry

# Copiar o conteúdo do diretório atual para o contêiner
COPY . /src

# Definir o diretório de trabalho
WORKDIR /src

# Instalar as dependências do projeto com Poetry
RUN poetry install

# Expor a porta em que a aplicação estará escutando
EXPOSE 8501

# Definir o entrypoint para executar o servidor Uvicorn
ENTRYPOINT ["poetry","run", "fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "8501"]