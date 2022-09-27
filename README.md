
[Microsserviços.docx.pdf](https://github.com/camilacodes/ApiRestFlask/files/9498708/Microsservicos.docx.pdf)

## 🛠 Tools

WSL(Subsistema Windows para Linux), Python como linguagem, a biblioteca
HTTP Requests, o sistema de gerenciamento de banco de dados MySQL e o
microframework Flask.

## Passo a passo:
No diretório onde será criada cada API deve ser feito:
- Criar um abiente virtual:

python3 -m venv venv
```
- Ativar ambiente virtual:
```
. venv/bin/activate
```
- Instalar módulos Flask:
```
pip install Flask flask-mysql requests
pip install pymysql
```
- Para rodar a aplicação:
```
export FLASK_ENV=development
export FLASK_APP=main
flask run -p 5000 (cada API roda em um porta diferente)
```


## Banco de dados e Schemas
Para a construção do nosso banco de dados optamos por criar um banco para
cada API pensando na arquitetura de microsserviços, onde cada serviço é
independente e autônomo.

Utilizamos MySQL e a biblioteca Pymysql, separamos em quatro banco de
dados:]

- Banco Clientes: Contém uma tabela nomeada Cadastro, uma chave primária sendo ela o ID. Nela são armazenados os dados pessoais dos clientes cadastrados.


- Banco Endereços: Contendo uma tabela nomeada Endereço, com uma chave primária sendo ela o ID e um campo “id_cliente” que seria um campo utilizado para conectar o cliente cadastrado aos seus endereços, sendo um ou mais.

- Banco Catalogo_produtos:Contendo uma tabela nomeada Catálogo contendo com chave primária o id. Aqui são armazenados os produtos comercializados pela empresa.

- Banco Inventário_Produtos: Contendo uma chave primária sendo ela o id do inventário e esse banco contém um campo com id_produto e com id_cliente, correlacionando quais produtos determinado cliente adquiriu a partir do catálogo de produtos.


## Autenticação - Basic Auth

Criamos um arquivo para criarmos nossa autenticação Básica, onde passamos
os parâmetros de acesso: login e senha, uma resposta de erro caso o usuário
erre a senha e o tipo de autenticação. Em cada verbo HTTP das aplicações do
nosso microsserviço passamos o request de autorização de acesso.


## API gateway
Ainda pensando na arquitetura de microsserviços criamos um exemplo de uma
API Gateway que poderia ajudar na performance da nossa aplicação, na
segurança através de autenticações e também para os serviços de back-end
que alimentam as APIs, também sendo possível rastrear acessos e criar
análises de dados.


