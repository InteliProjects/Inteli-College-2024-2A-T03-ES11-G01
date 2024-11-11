# Arquivos de código

## [Backend](./backend/)

Essa pasta contém o código responsável pela API de autenticação do DataApp, e os endpoints que consomem as views.

## [Data_pipeline](./data_pipeline/)

Essa pasta contém o código referente ao processo de ETL, ou seja, à ingestão, tratamento e carregamento dos dados recebidos. Ela também contém um arquivo *README.MD*, que evidencia os resultados dos testes realizados no código.

## [Deploy](./deploy/)

O arquivo mais importante dessa pasta, em termos de código, é o *docker-compose.yml*, que é responsável pelo serviço do portainer, para garantir a orquestração e configuração do projeto em qualquer máquina. Além disso, existe um arquivo *README.MD* que explica ao leitor como realizar esse processo.

## [Frontend](./frontend/)

Essa pasta contém todo o código referente ao DataApp da aplicação desenvolvido no Streamlit, além de arquivos de Docker necessários para tornar a replicação do projeto mais fácil.

## [Infra](./infra/)

Essa pasta apresenta todos os serviços que o projeto utiliza, configurados em um arquivo *docker-compose.yml*