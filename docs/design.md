# Introdução

Este documento contempla todos os processos de Design, desde o desenvolvimento do Guia de estilos, até a implementação do Front-end.

# Sumário

- [1. Wireframe agnóstico de Dashboard](#1-wireframe-agnóstico-de-dashboard)
    - [1.1 Protótipo de baixa fidelidade](#11-protótipo-de-baixa-fidelidade)
        - [1.1.1 Home vendedor](#111-home-vendedor)
        - [1.1.2 Home gerente](#112-home-gerente)
        - [1.1.3 Insights de vendas](#113-insights-de-vendas)
        - [1.1.4 Simulador de remuneração](#114-simulador-de-remuneração)
        - [1.1.5 Projeção de vendas](#115-projeção-de-vendas)
        - [1.1.6 Informações adicionais](#116-informações-adicionais)
    - [1.2 Relação com a Arquitetura](#12-relação-com-a-arquitetura)
        - [1.2.1 Autenticação](#121-autenticação)
        - [1.2.2 Modelagem de Dados](#122-modelagem-de-dados)
        - [1.2.3 Considerações gerais](#123-considerações-gerais)
    - [1.3 Relação com as Análises Exploratórias](#13-relação-com-as-análises-exploratórias)
    - [1.4 Base de prospecção de tecnologia de Dashboard](#14-base-de-prospecção-de-tecnologia-de-dashboard)
- [2. Guia de estilos](#2-guia-de-estilos)
    - [2.1 Cores](#21-cores)
    - [2.2 Tipografia](#22-tipografia)
    - [2.3 Iconografia](#23-iconografia)
- [3. Mockup](#3-mockup)
    - [3.1 Relação do mockup com requisitos](#31-relação-do-mockup-com-requisitos)
- [4. DataApp](#4-dataapp)

# 1. Wireframe agnóstico de Dashboard

## 1.1 Protótipo de baixa fidelidade

O wireframe foi pensado para ser o mais claro possível para o usuário, e ao mesmo tempo mostrar todas as informações que são relevantes à ele. Como existem duas diferentes personas para a plataforma, os vendedores e os gerentes, a página principal foi levemente modificada para atender a ambas necessidades.

### 1.1.1 Home vendedor

<div align="center">
  <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726238170/Screenshot_2024-09-13_at_11.37.21_sjxmfx.png" style="width: 70%;">
</div>


Essa página tem o objetivo de apresentar as informações mais relevantes para o vendedor, sendo elas baseadas nas principais dores do cliente. Elas estão dispostas em 3 gráficos: um que mostra como está o andamento de suas vendas de acordo com sua meta mensal, um ranking dos melhores vendedores da sua região e os fatores que compõem a sua remuneração.

### 1.1.2 Home gerente

<div align="center">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726238168/Screenshot_2024-09-13_at_11.38.10_ek9foj.png" style="width: 70%;">
</div>

Já a página principal do gerente, é bem semelhante à do vendedor em termos visuais, porém as informações são mais focadas nas estatísticas da loja. A primeira parte mostra como está o andamento das vendas de acordo com sua meta mensal da loja, em seguida, um ranking das melhores lojas daquela região, e por último, um acompanhamento de vendas e metas que aquele gerente administra.

### 1.1.3 Insights de vendas

<div align="center">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726238169/Screenshot_2024-09-13_at_11.37.27_mv97hy.png" style="width: 70%;">
</div>

Essa página engloba os fatores que serão importantes no momento de uma venda, principalmente para o vendedor. A maior parte da tela é preenchida por produtos que possuem a maior margem de lucro, para que seja de fácil acesso ao usuário. Além disso, existe a opção de pesquisa para Cross-sell e produtos substitutos, na qual o vendedor poderá procurar por um produto específico e a aplicação irá retornar as 3 melhores opções, como mostrado no exemplo a seguir:

<div align="center">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726238925/Screenshot_2024-09-13_at_11.51.01_xx7olm.png" style="width: 50%;">
</div>

Isso permite que o usuário tome decisões rápidas sobre qual produto acrescentar na sua venda ou qual produto substituir caso o cliente não encontre o que procura.

### 1.1.4 Simulador de remuneração

<div align="center">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726238169/Screenshot_2024-09-13_at_11.37.46_gkyjx8.png" style="width: 70%;">
</div>

Um dos requisitos mais desejados por vendedores e gerentes é fazer uma simulação de quanto eles podem ganhar dado algumas situações. Por enquanto, pretende-se implementar essa páginas apenas para os vendedores, já que os gerentes não realizam vendas na loja. A remuneração deles é dividia em 3 partes, a comissão normal de cada produto, a comissão de produtos com maior margem de lucro, e o valor que ele ganha ao atingir a sua meta. Sabendo disso, é possível que o vendedor simule algumas situações para entender como sua remuneração se diferencia, e quanto esforço precisa fazer para atingir a meta.

### 1.1.5 Projeção de vendas

<div align="center">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726238169/Screenshot_2024-09-13_at_11.37.59_wr17ts.png" style="width: 70%;">
</div>

A última página tem o objetivo de o usuário poder projetar suas vendas no futuro e relembrar seu atingimento no passado, e caso deseje, compará-las com a meta. Foi pensado na possibilidade do usuário escolher a medida de tempo e também as datas, o que favorece a usabilidade. Na aplicação real, essas funcionalidades foram substituídas pela possibilidade de visualizar ou não a linha que representa a meta e a projeção do vendedor.

### 1.1.6 Informações adicionais

O desenvolvimento do wireframe foi baseado em como distribuir as features de forma que a visualização fosse intuitiva ao usuário, por isso os gráficos individuais ou da loja estão dispostos na página principal, as análises que auxiliam nas vendas agrupadas em outra página, e as demais features separadas em outras páginas.

Além disso, na página insights de vendas, o componente que mostra os produtos com maior margem de venda será dividido por cores e ícones, pois assim o vendedor consegue ao olhar para o card, associar a categoria do produto.

O wireframe pode ser acessado [aqui](https://www.figma.com/design/SVRRy0tBmJXB38MrwAyDII/DataLoom?node-id=0-1&node-type=canvas&t=oSBajPbuAdf47Gtv-0), porém também existe a versão em pdf: [Wireframe](../assets/Wireframe.pdf).

## 1.2 Relação com a Arquitetura

Ao realizar o desenvolvimento do wireframe buscou se manter a coerência com a arquitetura projetada para o sistema.

### 1.2.1 Autenticação
Tela de login para permitir acesso apenas de pessoas autorizadas, identificação que será utilizada para permitir ao usuário o acesso apenas às páginas permitidas pelo seu nível de acesso (vendedor e gerente).

Níveis de acesso bem segmentados, com telas que serão acessadas apenas por vendedores, e outras páginas que serão acessadas apenas por gerentes, podendo visualizar apenas os dados que são permitidos para eles. Ex: sua região para gerentes e seus dados (remunerações e metas) para vendedores. Assim como telas que ambos os tipos de usuários terão acesso (gerais).

### 1.2.2 Modelagem de Dados
Alto nível de abrangência às views definidas, com a criação de visualizações gráficas e informacionais relevantes que estão de acordo com as capacidades de consulta e manipulação das bases de dados, adaptadas para os diferentes usuários da plataforma e respeitando as políticas de governança dos dados.

### 1.2.3 Considerações Gerais
Alto nível de detalhamento e plena implementação dos requisitos, garantindo uma visualização realista e factível do DataApp, com uma estruturação que não compromete as capacidades técnicas da solução.

## 1.3 Relação com as Análises Exploratórias

O wireframe traduz as análises realizadas para a exploração dos dados, de forma que se adapta para a apresentar as informações obtidas da melhor configuração para o usuário. Neste sentido, é possível perceber a presença das análises já na primeira página de entrada que o vendedor tem acesso, na qual se apresenta os dados de venda em relação a meta, sendo correspondentes às análises de metas e transações, na qual se obtém determinado resultado.

Ainda na mesma tela, tem-se o ranking de vendas de determinada região que está correlacionado a análise exploratória de lojas x região x vendedores, encontrada no arquivo [vendedor.Rmd](../docs/R%20notebooks/vendedor.Rmd). A análise faz uma seleção dos vendedores por região e os ordena por porcentagem de meta atingida, através do cruzamento das bases. Nota-se que respeitando o que foi definido por privacidade dos dados, apenas os 5 primeiros aparecem para todos os colaboradores, a fim de destacar positivamente respectivos desempenhos.

Em seguida, tem-se o dado de remuneração acumulada, esse dado é obtido por meio de fórmula e também o uso da base de transações. Ainda trabalhando dentro das análises e insights, outra feature que o sistema carrega é a de apresentação de produtos com maior % de lucro, feature desenvolvida na análise do arquivo [produto.Rmd](../docs/R%20notebooks/produto.Rmd), na qual se tem o cálculo e classificação dos 5 produtos com maior margem de lucro por loja.

Ademais, ainda é possível perceber o uso de dados de cross-sell, também efeito do cruzamento de transações com a tabela de produtos, adicionado a um algoritmo de recomendação, o Apriori. Outros algoritmos são usados para a recomendação de produtos substitutos, que não foi propriamente desenvolvido na análise exploratória, mas que foi feito usando algoritmo de similaridade.

Vale destacar que as políticas de governanças, definidas no documento [Arquitetura de Negócios](./arquitetura_negocio.md), foram aplicadas em cada uma das telas e informações apresentadas, desde a seleção de dados, que garantem integridade e consistência, além de escalabilidade e da segurança desses, que refletem nas telas personalizadas para cada um dos colaboradores. Ademais, também foram consideradas na diferenciação de interfaces entre vendedores e gerentes, para garantir que dados sensíveis ou pessoais não sejam compartilhados com os que não devem ter acesso.

## 1.4 Base de prospecção de tecnologia de Dashboard

Para selecionar a ferramenta ideal para a construção visual da aplicação, foi realizada uma análise criteriosa dos requisitos funcionais, com o objetivo de garantir que o framework escolhido atenda de forma eficaz às principais necessidades da aplicação. Os requisitos funcionais a serem considerados incluem:

* **RF1, RF2 e RF3:** Esses requisitos demandam que a ferramenta selecionada possua alta flexibilidade e facilidade de uso para a criação de gráficos e dashboardsons, considerando que esses elementos serão o conteúdo central do DataApp e irão compor as páginas principais da aplicação;

* **RF4, RF5, RF6, RF7, RF8:** Esses requisitos exigem que a ferramenta escolhida ofereça integração simplificada com frameworks de banco de dados e modelos de análise estatística, visto que as principais funcionalidades da aplicação envolvem o processamento de grandes volumes de dados para exibição no DataApp, proporcionando insights e informações para os funcionários.

Diante dessa análise, a ferramenta **Streamlit** se apresentou como uma escolha adequada para a construção do DataApp, pois atende aos requisitos funcionais da aplicação de forma ágil e eficiente. Desenvolvida em Python, o que facilita a integração com bibliotecas utilizadas na análise de dados, como Pandas e Scikit-Learn, o Streamlit permite criar interfaces interativas para visualização de dados sem a necessidade de conhecimentos avançados em desenvolvimento web. Ademais, a ferramenta se destaca por sua capacidade de gerar gráficos e dashboards interativos de forma ágil e de fácil desenvolvimento, proporcionando visualizações dinâmicas e responsivas para facilitar a análise de dados tanto pelo computador do gerente quanto pelo celular dos vendedores, o que garante ao DataApp o acesso por meio de todos os dispositivos.

Além disso, o Streamlit se destaca no contexto deste projeto por simplificar o processo de deploy do DataApp, permitindo que ele seja rapidamente implementado diretamente nas lojas, em servidores locais ou computadores de fácil acesso. Tal simplicidade garante que as informações de peso relevante, como projeções de vendas, metas e modelos de remuneração, estejam sempre disponíveis aos vendedores no ponto de venda, impulsionando essa operação. Dessa forma, o Streamlit possibilita a adoção do DataApp sem a necessidade de uma infraestrutura complexa, proporcionando uma implementação rápida e eficiente que atende às necessidades imediatas das lojas e seus colaboradores.

# 2. Guia de estilos

Para realização do mockup, foi necessário pensar em um guia de estilos para padronizar alguns elementos. No caso deste projeto, especificamos cores, tipografia e ícones.

Ele pode ser acessado [aqui](https://www.figma.com/design/SVRRy0tBmJXB38MrwAyDII/DataLoom?node-id=59-34&node-type=canvas&t=oSBajPbuAdf47Gtv-0), porém também existe a versão em pdf: [Guia de estilos](../assets/Guia%20de%20estilos.pdf).


## 2.1 Cores

<div style="text-align: center;">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726237561/Screenshot_2024-09-13_at_11.25.54_cmt8ox.png" style="width: 600px;">
</div>

As cores estão divididas em 5 partes:
- **Cores da marca:** foram utilizadas em alguns momentos na aplicação e representam as cores principais da marca;
- **Cores de estado:** representam estados como sucesso, erro, atenção e informação e demonstram ao usuário alguns estados do sistema;
- **Tons de preto:** utilizados em texto, ícones etc;
- **Cores categóricas:** cada cor representa uma categoria de produtos o que facilita a identificação por parte do usuário; 
- **Cores de legenda:** são utilizadas nos gráficos;
- **Cores de fundo:** utilizadas como background na aplicação;

## 2.2 Tipografia 

<div style="text-align: center;">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726237576/Screenshot_2024-09-13_at_11.27.05_ceemxz.png" style="width: 600px;">
</div>

Para a tipografia, foi escolhida a fonte Poppins, que é muito utilizada em aplicativos mobile, além de ser confortável aos olhos por não ser serifada.

## 2.3 Iconografia

<div style="text-align: center;">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1726237604/Screenshot_2024-09-13_at_11.29.00_yn0wqp.png" style="width: 600px;">
</div>

Por último, para a iconografia, foram utilizadas as bibliotecas do Bootstrap e Material UI, pois são fáceis de serem integradas, tem consistência visual, e apresentam uma grande variedade de ícones.

# 3. Mockup

O mockup seguiu como base o wireframe, porém com a adição da estilização e aplicação do guia de estilos. Por enquanto, a única página que não está no mockup é o simulador de remuneração, pois a forma como ela é composta não ficou muito clara, e mesmo após conversar com o parceiro decidimos por não prosseguir com ela devido sua complexidade e a limitação de tempo que a equipe sofreu.

Além disso, ao longo do desenvolvimento algumas alterações foram requisitadas por parte do parceiro, sendo a principal a mudança de um gráfico de ranking por linhas, com a visualização em porcentagem e mostrando aos usuários apenas os nomes dos vendedores.

Foi decicido modificar a estrutura do ranking para algo mais minimalista e com ícones de posicionamento, portanto, no mockup será possível acompanhar a evolução das 3 mudanças de visualização realizadas nessa funcionalidade.

Ele pode ser acessado [aqui](https://www.figma.com/design/SVRRy0tBmJXB38MrwAyDII/DataLoom?node-id=0-1&node-type=canvas&t=G6aGxJMGgWU36Z3B-0), porém também existe a versão em pdf: [Mockup](../assets/Mockup.pdf).

### Fluxo vendedor

<div align="center">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1727446865/Screenshot_2024-09-27_at_11.20.58_kr1gqa.png">
</div>

### Fluxo gerente

<div align="center">
    <img src="https://res.cloudinary.com/dpu52x6xq/image/upload/v1727446808/Screenshot_2024-09-27_at_11.20.02_gsneo9.png">
</div>

## 3.1 Relação do mockup com requisitos

Além de seguir o wireframe, o Mockup também buscou atender os requisitos mapeados inicialmente no projeto. Assim, as telas buscaram garantir a visualização gráfica da projeção de vendas, conforme o RF01, e também recomendações de produtos que são frequentemente vendidos em conjunto, para suportar a prática de cross-sell, assim como no RF04.

Além disso, foi incluído a visualização de metas que devem ser atingidas, tanto para vendedores individuais, quanto para gerentes de lojas, conforme RF02. Somado a isso, o Mockup também permite a simulação de remuneração final do vendedor ao final do mês, de acordo com a sua performance, assim como prevê o RF07.

Para melhor visualizar a relação desses com as telas desenvolvidas, é possível acompanhar pela tabela abaixo.

<center>Tabela 1 - Correlação Mockup e Requisitos</center>

|Telas|RF01|RF02|RF03|RF04|RF05|RF06|RF07|RF08|
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Login - Vendedor|-|-|-|-|-|-|-|-|
|Home - Vendedor|-|x|-|-|-|x|-|-|
|Insights - Vendedor|-|-|-|x|x|-|-|-|
|Simulação - Vendedor|x|-|x|-|-|-|-|-|
|Login - Gerente|-|-|-|-|-|-|-|-|
|Home - Gerente|-|x|-|-|-|x|-|-|
|Insights - Gerente|-|-|-|x|x|-|-|-|
|Simulação - Gerente|x|-|-|-|-|-|-|-|


# 4. DataApp

O DataApp foi desenvolvido com base no mockup documentado acima, estando sujeito a algumas mudanças estritamente relacionadas a estilização, por limitações das tecnologias utilizadas. 

Para rodar a aplicação, acesse nosso [guia para rodar o frontend](../src/frontend/README.md).

Para visualizar a interface rodando, acesse nossa [demo da sprint 4](https://youtu.be/2amIkr0WP7g).
