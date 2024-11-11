# Use uma imagem base do Python
FROM python:3.12

# Define o diretório de trabalho
WORKDIR /backend

# Copie os arquivos de configuração
COPY pyproject.toml ./

# Instale o Poetry
RUN pip install poetry

# Instale as dependências da aplicação
RUN poetry install --no-root

# Copie o restante da aplicação
COPY . .

# Exponha a porta que a aplicação Flask usará
EXPOSE 5001

# Comando para rodar a aplicação Flask
CMD ["poetry", "run", "python", "app.py"]