# Documentação do projeto

## [Apresentações](./apresentacoes/)

Nesse diretório, são disponibilizados os materiais visuais utilizados durante as cerimônias de Sprint Review.

## [R Notebooks](./R%20notebooks/)

O diretório contém os arquivos em Rmd e HTML utilizados para realizar as análises exploratórias dos dados do parceiro.

## [Análise exploratória](./analise_exploratoria.md)

O documento aborda a análise exploratória dos dados fornecidos pelo parceiro, descrevendo como os eles foram manipulados para garantir a conformidade com a governança de dados. O foco inicial foi na escolha estratégica de três variáveis principais, que estavam alinhadas com as user stories e os requisitos do projeto. A escolha das variáveis foi baseada em três temas macro: vendedores e gerentes, produtos e lojas, com o objetivo de cobrir cada um desses aspectos.

## [Arquitetura de Dados](./arquitetura_dados.md)

O documento aborda uma visão horizontal do projeto, todas as questÕes relacionadas a requisitos, arquitetura, modelagem de dados, testes de usabilidade e outros aspectos de governança de dados.

## [Arquitetura de negócios](./arquitetura_negocio.md)

O documento aborda assuntos relacionados à estrutura da governança de dados e políticas de uso de dados no projeto "Assistente de Vendas Hiper Personalizado", detalhando práticas de segurança, conformidade com a LGPD, critérios para acesso, medição da qualidade e retenção de dados. São apresentadas diretrizes para a classificação e gestão dos dados, além de políticas de tratamento e descarte, e medidas de segurança como criptografia e autenticação multifatorial. O documento também trata da medição da qualidade dos dados, impacto nos processos operacionais, e a importância da conformidade com a LGPD para garantir a privacidade e a segurança das informações.

## [Design](./design.md)

O documento apresenta todas as análises de design realizadas, desde a criação do guia de estilos, prototipação do wireframe e explicação dos componentes até a elaboração do mockup e a documentação completa do MVP do DataApp.

## [Devops](./devops.md)

O documento descreve os processos de Integração Contínua (CI) e Entrega Contínua (CD) no projeto, abordando a automação de testes, builds e deploys para garantir a eficiência do ciclo de desenvolvimento. Utilizando GitHub Actions, Docker e Portainer, o CI automatiza a verificação de código e execução de testes, enquanto o CD utiliza contêineres Docker para flexibilidade, portabilidade e segurança. A infraestrutura é gerenciada pelo Portainer, facilitando o controle de recursos e escalabilidade. O documento também destaca as decisões arquiteturais para balancear custos e desempenho sem comprometer a segurança.

## [Modelagem Física](./modelagem_fisica.sql)

O documento cria tabelas e views para gerenciar dados já tratados de transações, produtos, funcionários, lojas e metas de vendas em um banco de dados.

## [Template da Arquitetura](./template_arquitetura.md)

A partir de estudos à cerca do TOGAF (The Open Group Architecture Framework), o documento foi adaptado para abrangir uma visão detalhada da solução desenvolvida, com foco na arquitetura do sistema, seus componentes, e outros artefatos que compõe a solução.
