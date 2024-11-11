# Front-end

Desenvolvido em Streamlit, o front-end da aplicação se encontra neste diretório. Ele foi organizado de forma a se manter otimizado e organizado para aplicações e alterações futuras.

# Pastas

A organização se deu conforme descrição abaixo:

```
├── 📁 frontend
│   ├── 📁 .streamlit
|   ├── 📁 assets
│   ├── 📁 components
│   ├── 📁 pages
│   ├── 📄 Dockerfile
|   ├── 📄 poetry.lock
|   ├── 📄 pyproject.toml
|   ├── 📄 README.md
|   ├── 📄 streamlit_app.py
```

Onde, as pastas presentes são:

- [.streamlit](./.streamlit): configurações nativas do streamlit. Esta pasta é criada automaticamente, quando se adiciona um novo projeto usando a tecnologia.
- [assets](./assets/): recursos visuais usados na plataforma, como imagens, logos e ícones.
- [components](./components/): componentização dos elementos do app, usados a fim de otimizar o desenvolvimento.
- [pages](./pages/): as páginas presentes na aplicação, todas são chamadas no navbar.


# Instruções para iniciar o projeto
Instalar dependencias 

        poetry install

Rodar projeto

        poetry run streamlit run streamlit_app.py

Acessar no navegador: http://localhost:8501 (deve ser inicializado sozinho, caso não ocorra, acessar a url indicada).