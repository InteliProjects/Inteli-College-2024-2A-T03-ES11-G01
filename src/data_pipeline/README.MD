### Rodando os Testes
### Ferramentas utilizadas
- pytest
- unittest
#### Como rodar
-       poetry run pytest
#### Nível de cobertura
- ferramenta utilizada: pytest cov

Como rodar e gerar html:
-       poetry run pytest --cov=core --cov-report=html

Relatório gerado:
![relatorio-cobertura](<../../assets/coverage.png>)