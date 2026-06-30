# Sistema de Gerenciamento - Marcenaria Afeto

## Descrição

Este projeto foi desenvolvido em Python com o objetivo de gerenciar clientes, produtos e vendas de uma marcenaria por meio de um menu interativo no terminal.

## Funcionalidades

### Clientes

- Cadastrar clientes
- Listar clientes
- Alterar cadastro
- Excluir cadastro

### Produtos

- Cadastrar produtos
- Listar produtos
- Alterar informações
- Excluir produtos

### Vendas

- Realizar vendas
- Aplicar desconto respeitando o limite do produto
- Registrar a data da venda
- Sortear um brinde
- Listar todas as vendas realizadas

## Bibliotecas utilizadas

- `random` - utilizada para o sorteio de brindes.
- `datetime` - utilizada para registrar a data das vendas.

## Como executar

1. Instale o Python 3.
2. Baixe o projeto.
3. Execute o arquivo principal:

```bash
python nome_do_arquivo.py
```

## Estrutura dos dados

O sistema utiliza listas e dicionários para armazenar as informações durante a execução do programa.

- Clientes
- Produtos
- Vendas

Os dados são armazenados apenas em memória e são perdidos quando o programa é encerrado.

## Menu principal

```
1 - Cadastrar Cliente
2 - Ver Cadastros
3 - Alterar Cadastro
4 - Deletar Cadastro

5 - Cadastrar Produtos
6 - Ver Produtos
7 - Alterar Produtos
8 - Deletar Produto

9 - Vender
10 - Ver Vendas

0 - Sair
```

## Observações

- O sistema é executado pelo terminal.
- Não utiliza banco de dados.
- Possui validações para CPF, nome, senha, preço e desconto.
- O produto vendido é removido da lista de produtos disponíveis.

## Autor

Projeto desenvolvido para fins acadêmicos utilizando a linguagem Python e conceitos de programação estruturada.
