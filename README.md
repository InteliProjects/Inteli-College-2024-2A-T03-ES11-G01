# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
  <img src="https://i.imgur.com/aIfBsxk.png" alt="Inteli logo" border="0" width="300px">
</p>

# Estrutura e governança para análise de dados - DataApp voltado para vendedores e gerentes

## Grupo 1 - DataLoom
<div align="center">
  <img src="https://res.cloudinary.com/dujx0hv4e/image/upload/v1724417404/entregavel/aewdoo13gmygkertglzq.png" width="40%">
</div>

<br>

### 🚀 Integrantes
- <a href="https://www.linkedin.com/in/ana-clara-zaidan/">Ana Clara Müller</a>
- <a href="https://www.linkedin.com/in/bruno-omeira/">Bruno Meira </a>
- <a href="https://www.linkedin.com/in/felipe-saadi/">Felipe Saadi</a>
- <a href="https://www.linkedin.com/in/jordan-acs/">Jordan Andrade</a>
- <a href="https://www.linkedin.com/in/mateus-neves-3b767123b/">Mateus Neves</a>
- <a href="https://www.linkedin.com/in/priscila-falc%C3%A3o-3435a1244/">Priscila Falcão</a>
- <a href="https://www.linkedin.com/in/sofia-moreiras-pimazzoni/">Sofia Pimazzoni</a>

## 🔍 Sumário

| Tópicos|
|---|
| [Descrição](#-descrição)|
| [Estrutura de pastas](#-estrutura-de-pastas)|
| [Documentação](#-documentação)|
| [Instalação](#-instalação)|
| [Tecnologias](#-Tecnologias) |
| [Histórico de lançamentos](#-histórico-de-lançamentos)|
| [Licença/License](#-licençalicense)|
| [Referências](#-referências)|


## 📜 Descrição

O projeto visa desenvolver uma ferramenta de análise de dados para uma empresa de cosméticos parceira, com foco em melhorar a comunicação de informações e dados entre a empresa e seus vendedores e gerentes. O objetivo é criar um sistema que processe dados de vendas e produtos, realize as devidas transformações para a limpeza e transformação, organize e apresente-os de forma personalizada para gerentes e vendedores através de um aplicativo móvel. A ferramenta fornece insights sobre o desempenho de cada vendedor, ajudando a aumentar o engajamento e a performance da equipe. Além da ferramenta, o projeto inclui a criação de uma estrutura de governança de dados e documentação detalhada sobre o fluxo de dados e o uso da ferramenta.


## 📁 Estrutura de pastas

```
├── 📁 docs
│   ├── 📁 apresentacoes
|   ├── 📁 R notebooks
│   ├── 📝 analise_exploratoria.md
│   ├── 📝 arquitetura_negocio.md
│   ├── 📝 arquitetura_dados.md
|   ├── 📝 template_arquitetura.md
|   ├── 📝 design.md
|   ├── 📝 devops.md
|   |── 📝 modelagem_fisica.sql
|   ├── 📝 readme.md
├── 📁 src
│   ├── 📁 backend
│   ├── 📁 data_pipeline
│   ├── 📁 deploy
|   ├── 📁 frontend
|   |── 📁 infra
├── 📝 README.md

```

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (arquivo atual).

- <b>/docs</b>: as documentações geradas no desenvolvimento do projeto.
    - <b>/apresentacoes</b>: os slides utilizados nas sprint reviews.
    - <b>/R notebooks</b>: rmds e notebooks referentes às análises exploratórias.
    - <b>/analise_exploratoria.md</b>: informações referentes às análises exploratórias realizadas..
    - <b>/arquitetura_negocio.md</b>: documentação de questões de governança de dados voltadas a LGPD.
    - <b>/arquitetura_dados.md</b>: documentação da parte técnica do projeto.
    - <b>/template_arquitetura.md</b>: template de documentação caso haja replicação do projeto.
    - <b>/design.md</b>: documentação voltada ao UX do DataApp, incluindo Wireframe e Mockup.
    - <b>/devops.md</b>: os slides utilizados nas sprint reviews.
    - <b>/readme.md</b>: documento que direciona a todos os outros.

- <b>/src</b>: os artefatos que compõem o sistema. 

  - <b>/backend</b>: controle do sistema, autenticação e regras de negócio.

  - <b>/data_pipeline</b>: esteira para o processamento dos dados.

  - <b>/deploy</b>: processo para disponibilizar a aplicação para uso em um ambiente de produção.

  - <b>/frontend</b>: DataApp, a interface que poderá ser acessada pelos usuários.

  - <b>/infra</b>: apresenta todos os serviços que o projeto utiliza.

## 📄 Documentação principal do projeto

* [Análise Exploratória](./docs/analise_exlporatoria.md)
* [Template da Arquitetura](./docs/template_arquitetura.md)
* [Arquitetura de Negócio](./docs/arquitetura_negocio.md)
* [Arquitetura de Dados](./docs/arquitetura_dados.md)

## ⬇️ Instruções para implantação do projeto

O guia de implantação do projeto pode ser acessado [aqui](./src/deploy/README.md)

## 🔧 Instruções para execução do projeto

O guia de execução do projeto pode ser acessado [aqui](./src/infra/README.md)

## 👨‍💻 Tecnologias Utilizadas
- [R (versão 4.4.1)](https://www.r-project.org/)
- [R Studio (versão 2024.04.2+764)](https://posit.co/products/open-source/rstudio/)
- [Python (versão 3.12)](https://www.python.org/)
- [Docker (última versão disponível)](https://www.docker.com/)
- [Supabase](https://supabase.com/)
- [ClickHouse](https://clickhouse.com/)
- [Elastic](https://www.elastic.co/pt/)

## 📖 Histórico de lançamentos

**Versão 1.0 — 16/08/2024 (Sprint I)**

* Configuração de ambiente
* Notebook inicial de análises
* Template de arquitetura
* Estruturação da documentação
* Definição de requisitos
* Criação de user stories
* Arquitetura de negócio
* Exploração de dados;

**Versão 2.0 — 30/08/2024 (Sprint II)**

* Novas análises exploratórias
* Módulo de Ingestão de Dados
* Criação do DataLake
* Transformação dos Dados
* Modelagem dos Dados
* Aprimoramento da arquitetura
* Wireframe da aplicação

**Versão 3.0 — 13/09/2024 (Sprint III)**

* Mockup da aplicação
* Arquitetura final
* Processamento, integração e manipulação dos dados
* Implementação de Logs


**Versão 4.0 — 27/09/2024 (Sprint IV)**

* Primeira versão do DataApp
* Integração do DataApp com as views
* Aprimoramento de questões de governança de dados voltadas à LGPD
* Dockernização completa da arquitetura
* Implementação do portainer para orquestração de containers
  

**Versão 5.0 — 11/10/2024 (Sprint V)**

* Versão final do DataApp
* Finalização das integrações pendentes do DataApp
* Conclusões da documentação de governança de dados
* Últimos ajustes nas documentações


## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="#">DataLoom</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="#">Inteli, Ana Clara Müller, Bruno Meira, Felipe Saadi, Jordan, Mateus Neves, Priscila Falcão dos Santos, Sofia Pimazzoni.
</a> is 
licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## 🎓 Referências

R CORE TEAM. R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria. Disponível em: https://www.r-project.org/. Acesso em: 8 ago. 2024.

PYTHON SOFTWARE FOUNDATION. Python: A programming language that lets you work quickly and integrate systems more effectively. Disponível em: https://www.python.org. Acesso em: 14 ago. 2024.

SUPABASE. Supabase: The open source Firebase alternative. Disponível em: https://supabase.com. Acesso em: 14 set. 2024.

CLICKHOUSE, INC. ClickHouse: Open-source columnar database management system. Disponível em: https://clickhouse.com/. Acesso em: 14 ago. 2024.

DOCKER. Docker: Empowering App Development for Developers. Disponível em: https://www.docker.com. Acesso em: 22 ago. 2024.

ELASTIC. Elasticsearch: Real-time distributed search and analytics engine. Disponível em: https://www.elastic.co/elasticsearch/. Acesso em: 10 set. 2024.


