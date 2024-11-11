# Use uma imagem base do Python
FROM python:3.12

# Define o diretório de trabalho
WORKDIR /data_pipeline

# Copie os arquivos de configuração
COPY pyproject.toml ./

# Instale o Poetry
RUN pip install poetry

# Instale as dependências da aplicação
RUN poetry install --no-root

RUN poetry run prefect config set PREFECT_API_URL="http://prefect:4200/api"

# Copie o restante da aplicação
COPY . .

# Exponha a porta que a aplicação Flask usará
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["poetry", "run", "python", "app.py"]