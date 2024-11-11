# Processos de Devops

Este documento aborda os processos de Integração Contínua (CI) e Entrega Contínua (CD) implementados no projeto, fornecendo um guia completo sobre como foram automatizados os testes, builds e deploys. O objetivo é garantir que as alterações do código sejam integradas de maneira contínua e que as versões sejam entregues de forma eficiente, minimizando erros manuais e acelerando o ciclo de desenvolvimento em nossas sprints.

A seguir, foi descrito as ferramentas utilizadas, a configuração do pipeline, as etapas envolvidas e as boas práticas para manter um fluxo de CI/CD robusto e confiável.

Os arquivos `.yml` referentes as pipelines de integração e entrega continua podem ser encontradas [nesta pasta](https://github.com/Inteli-College/2024-2A-T03-ES11-G01/tree/main/.github/workflows).

## Esteira de CI - Integração Contínua (CI)

A integração contínua (CI) é uma prática essencial no DevOps, pois automatiza a execução de testes, verificações de código e integração de alterações em um projeto de Software. Isso garante que o código seja constantemente testado e validado antes de ser integrado ao ambiente de produção ou às principais branches usadas para entrega da Sprint. Este processo ajuda a identificar problemas rapidamente, promovendo um ciclo de feedback rápido e evitando a introdução de bugs em versões futuras.

Nesta esteira de CI, está sendo utilizado o GitHub Actions, que automatiza o fluxo de integração contínua para o projeto. Ela é disparada automaticamente quando há um **pull request** na branch `main`. O pipeline é dividido em múltiplos jobs, com o objetivo de garantir a qualidade do código, desde a verificação do PR até a execução de testes unitários.

O primeiro passo na esteira é verificar se o pull request (PR) foi aprovado ou se foi mesclado com sucesso. Esta etapa é importante para garantir que o código passou por revisão antes de ser integrado à branch principal. Apenas PRs aprovados ou mesclados corretamente poderão seguir para as próximas etapas.

Em seguida, há uma verificação adicional para garantir que o PR foi enviado a partir da branch `develop`. Isso assegura que as alterações de desenvolvimento estejam sendo feitas na branch correta, evitando que código de outras branches seja erroneamente submetido ou revisado, mantendo a organização e consistência do ciclo de desenvolvimento.

Após a validação da branch, o código é inspecionado por meio de linting utilizando o **Flake8**, uma ferramenta que detecta erros de sintaxe, códigos complexos ou linhas muito longas. O linting é essencial para manter a legibilidade e qualidade do código. Além disso, erros críticos, como falhas de sintaxe e nomes indefinidos, são destacados para que possam ser corrigidos. A configuração permite que erros sejam tratados como avisos, para não interromper imediatamente o fluxo de CI, mas assegurando que problemas de qualidade sejam visíveis.

Na sequência, são executados os testes unitários do projeto. Utilizando **Poetry** para gerenciar as dependências, a esteira instala os pacotes necessários e executa os testes com o **pytest**. Isso garante que o comportamento das funções e módulos do projeto seja testado conforme as especificações, evitando que novas alterações quebrem funcionalidades existentes.

Além disso, os testes são executados com cobertura de código, o que permite avaliar o quanto do código está sendo testado pelas suites de testes. A cobertura de código é uma métrica fundamental para garantir que as principais funcionalidades e fluxos estejam devidamente cobertos.

Ao final da execução dos testes, o relatório de cobertura gerado é carregado como um artefato no GitHub, permitindo que a gente possam acessar e verificar o quanto do código foi testado. O upload do relatório nos ajuda a identificar possíveis áreas que não estão sendo testadas adequadamente.

Após a etapa de verificação de qualidade do código e execução de testes, o próximo processo da esteira é a construção de uma imagem Docker do projeto. Essa etapa é importante para garantir que o projeto seja empacotado com todas as suas dependências em um ambiente consistente. A esteira utiliza o docker-compose para construir a imagem de forma limpa, utilizando a configuração disponível em `src/infra/docker-compose.yml`. O build é realizado sem cache para garantir que as dependências sejam atualizadas, proporcionando maior consistência e controle sobre o ambiente de execução.

Após a construção da imagem Docker, a esteira passa para a criação de uma release no GitHub. Utilizando o GitHub CLI, a esteira automatiza o processo de criação de um novo release, garantindo que cada release receba uma tag única baseada na data e no número da versão. Caso uma tag já exista para a data atual, a esteira incrementa automaticamente o número da versão, evitando conflitos. Isso garante que todas as alterações aprovadas e testadas estejam disponíveis como releases formais do projeto, facilitando o acompanhamento e a distribuição das versões mais recentes do software.

Ao final, a criação da release no GitHub permite que o código e os artefatos gerados estejam disponíveis para uso e integração em ambientes de produção, proporcionando um processo fluido e bem definido de entrega contínua.

## Esteira de CD - Entrega Contínua (CD)

Uma das principais decisões arquiteturais do projeto foi não utilizar um provedor de nuvem específico para deploy, optando por subir toda a infraestrutura em Docker, aliado ao Portainer para o gerenciamento de contêineres. Essa escolha foi feita considerando variáveis como flexibilidade, portabilidade, segurança, custo e desempenho, além da facilidade de escalabilidade proporcionada pelo Portainer.

A estratégia com Docker atende às necessidades do projeto nesse momento, oferecendo simplicidade no processo de desenvolvimento e implantação, sem comprometer a segurança ou o desempenho. Somado a isso, traz flexibilidade para a escolha de um serviço de nuvem posteriormente pelo parceiro, garantida pelo desenvolvimento agnóstico da aplicação.

Além disso, a infraestrutura está sendo planejada para facilitar um deploy em provedor específico no futuro.

-> Um Guia de Implantação do Portainer na nossa solução pode ser encontrado [aqui](https://github.com/Inteli-College/2024-2A-T03-ES11-G01/tree/develop/src/deploy).

Dessa forma, segue alguns dos benefícios do uso de containers com Docker e gerenciamento com Portainer:

### 1. Flexibilidade e Portabilidade

O Docker oferece uma solução muito flexível e portátil, o que permite rodar a aplicação da mesma forma em diferentes ambientes, diferentes máquinas ,e, eventualmente, em provedores de nuvem. Essa flexibilidade evita que se fique presos a um único provedor, garantindo uma liberdade para os parceiros de migrar para qualquer infraestrutura no futuro sem precisar fazer grandes mudanças no código ou na estrutura da aplicação.

### 2. Redução de Custos

Ao escolher Docker, consegue-se evitar custos com serviços de nuvem durante a fase de desenvolvimento e testes. Isso porque, existe limitações na versão free tier dos provedores. Além disso, o uso de contêineres permite rodar todos os serviços localmente ou em servidores mais simples, sem precisar depender de infraestruturas mais caras que normalmente são oferecidas por grandes provedores de nuvem como a AWS e a Azure. Além disso, o gerenciamento dos contêineres localmente com o Portainer mantém capacidade de escalar a aplicação de forma eficiente e controlada.

### 3. Simplicidade no Desenvolvimento e Deploy

Consegue-se encapsular todo o ambiente da aplicação em contêineres, incluindo todos os componentes da arquitetura. Isso simplifica o processo de desenvolvimento e implantação, pois tudo o que a aplicação precisa – como bibliotecas e dependências – já está incluído no contêiner. Essa abordagem garante que a aplicação rode da mesma forma em qualquer lugar, facilitando o desenvolvimento e evitando problemas de configuração de ambiente. Com o Portainer, esse processo é ainda mais simplificado, já que ele oferece uma interface gráfica para gerenciar os contêineres e monitorar a saúde da aplicação, facilitando a administração e o deploy de novas atualizações. Isso facilita, inclusive, que os parceiros -ou outros interessados- rodem o projeto localmente, eventualmente.

### 4. Segurança

Outro ponto positivo de usar Docker é o isolamento que ele oferece entre os contêineres, o que melhora a segurança da aplicação. Pode-se rodar cada parte da aplicação em contêineres separados, o que significa que se ocorrer erro em um serviço, isso não afeta os outros. Além disso, por não expor a aplicação diretamente em um ambiente de nuvem pública, evita-se muitos dos problemas de segurança que normalmente surgem, como configurações erradas de firewall e permissões de rede.

### 5. Controle e Escalabilidade com Portainer

Além do controle de recursos nativos do Docker (como CPU e memória), o Portainer ajuda a gerenciar a escalabilidade da aplicação. Ele permite visualizar e configurar facilmente o ambiente de execução, facilitando a adição de novos contêineres. Mesmo que o projeto ainda esteja em desenvolvimento - e seja um MVP - , essa abordagem possibilita escalar a aplicação conforme o volume de uso aumentar, sem ter que lidar apenas com os comandos do Docker via terminal.
