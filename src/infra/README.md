# Infra

A pasta conta com a infraestrutura da aplicação, sendo todo o suporte para as pipelines rodarem, o back-end operar, juntamente com os mecanismos de otimização. Está organizada no seguinte formato:

```
├── 📁 infra
│   ├── 📁 dev
|   ├── 📁 volumes
│   ├── 📄 .env
|   ├── 📄 .env.exemple
|   ├── 📄 docker-compose.yaml
|   ├── 📄 makefile
|   ├── 📄 README.md
```

Onde, as pastas e arquivos presentes são:

- [dev](./dev): containers para desenvolvimento.
- [volumes](./volumes): implementação de alguns volumes.
- [.env](./.env): configuração de ambiente, contando com urls, usuários e senhas (criado automaticamente a partir do makefile).
- [docker-compose.yaml](./docker-compose.yml): configuração dos containers em Docker referentes ao projeto.
- [makefile](./makefile): automatização para criação da infra completa, a partir de um comando.

## Como rodar (sem portainer)

1) Abra a pasta src/infra no terminal.


2) Crie o .env e troque as senhas.

- Linux/Mac:
```
make copy
```
- Windows:
```
make copy-w
```

**Atenção:** Será criado .env na pasta infra

3) Rode o comando:
```
make up
```
4) Para desligar a infra, rode:
```
make down
```