# Exercicio sobre banco de dados com sqlite

Este projeto inplementa funções e operações basicas de banco de dados com sqlite no python.
Ela realiza as seguintes operações:

## Explicação do código

1. **Configuração do Ambiente Virtual**:


Linux (no meu caso):
```
    python3 -m venv venv
```
2. **Gerar o arquivo requirements.txt**:
```
pip freeze > requirements.txt
```
3. **Conectar ao banco de dados**: Função `conectar_banco()` cria ou abre o banco `banco.db`.
4. **Gerenciar a tabela de livros**:
    - Criar a tabela `livros` com colunas: `id`, `titulo`, `autor`, `ano`, `genero` e `disponivel`
    - Inserir 5 livros diferentes na tabela
    - Consultar livros disponiveis na tabela (`disponivel = 1`)
    - Atualizar disponibilidade de um determinado livro
    - Ordenar os livros por ano em ordem decrescente
    - Deletar livros antigos com ano de publicação inferior a `1940`
5. **Gerenciar tabela de usuarios**:
    - Cria a tabela `usuario` com colunas `id` e `nome`
    - Alterar a tabela para adicionar a coluna `idade`
    - Insere 5 usuários
    - apaga a tabela usuario

## Como executar

### 1. Clone o repositório
```
git clone https:_/github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
### 2. Crie e ative o ambiente virtual:

***Linux***
```
python3 -m venv venv
source venv/bin/activate
```
***Windows***
```
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências (se houver)
```pip install -r requirements.txt```

### 4. Execute o script
```pyhon livros_sqlite.py```

### Tabela livros
| Coluna     | Tipo    | Restrições                          |
| ---------- | ------- | ----------------------------------- |
| id         | INTEGER | PRIMARY KEY AUTOINCREMENT           |
| titulo     | TEXT    | NOT NULL, UNIQUE                    |
| autor      | TEXT    |                                     |
| ano        | INTEGER |                                     |
| genero     | TEXT    |                                     |
| disponivel | INTEGER | NOT NULL, DEFAULT 1, CHECK (0 ou 1) |


### Tabela usuario
| Coluna     | Tipo    | Restrições                          |
| ---------- | ------- | ----------------------------------- |
| id         | INTEGER | PRIMARY KEY AUTOINCREMENT           |
| nome       | TEXT    |                                     |
| idade      | INTEGER |                                     |


## Estrutura do projeto
    meu-projeto-sql/
    │
    ├── venv/ # (ignorado pelo git)
    ├── .gitignore
    ├── livraria.db
    ├── livros_sqlite.py
    ├── README.md
    └── requirements.txt

## Fundamentos de Banco de dados


### 1. Por que os bancos de dados são essenciais em aplicações modernas?

Porque permitem armazenar grandes volumes de dados de forma organizada, assim permitindo
que gerenciem e usem informações de maneira eficaz para tomar decisões, melhorar a produtividade e inpulsionar
o crescimento

🔗 [Fonte](https://www.etice.ce.gov.br/2023/07/25/10-razoes-que-explicam-a-importancia-dos-bancos-de-dados-nos-dias-de-hoje/)

### 2. Quais são as duas principais categorias de bancos de dados existentes?

**Bancos de dados relacionais** são
fundamentados no paradigma da orientação
a conjuntos. Seus dados são armazenados
em estruturas denominadas **tabelas**.


**Bancos de dados não relacionais** são
soluções para situações nas quais os bancos
relacionais não atendem. Um exemplo são os
ambientes com **dados mistos** (imagens, mapas
e tabelas), que não podem ser tabulados em
linhas e colunas. 

🔗 [Fonte](https://www.opservices.com.br/files/bancos-de-dados.pdf)
### 3. Em quais cenários é recomendado utilizar um banco de dados relacional?

Os **bancos de dados relacionais** são usados para dar suporte a muitos tipos de aplicações, incluindo de e-commerce, controle de inventário, gerenciamento de relacionamento com o cliente e muitas outras.

🔗 [Fonte](https://www.nutanix.com/pt_br/info/database)

### 4. De que forma os recursos de hardware (CPU, memória, disco) afetam a performance de um banco de dados?

O desempenho da CPU, memória e disco influência na velocidade de processamento, acesso e armazenamento dos dados,
assim afetando o processamento dos dados

🔗 [Fonte](https://www.linkedin.com/advice/0/what-role-does-hardware-play-database-performance-nsyyf?lang=pt&lang=pt&originalSubdomain=pt)

### 5. O que significa escalabilidade no contexto de bancos de dados?

A escalabilidade de um banco de dados refere-se à sua capacidade de lidar com cargas de trabalho crescentes e volumes de dados cada vez maiores sem comprometer o desempenho ou os tempos de resposta.
A **escalabilidade vertical** (ou escalonamento para cima) significa adicionar mais capacidade a um servidor existente, como CPU, RAM, armazenamento ou uma combinação destes. É uma abordagem direta que aumenta a capacidade de uma única máquina, mas possui limitações físicas.

A **escalabilidade horizontal** (ou escalonamento horizontal) , por outro lado, significa adicionar máquinas para distribuir as cargas de trabalho entre vários sistemas. Isso pode aumentar significativamente a escalabilidade e fornecer backup caso um servidor fique inativo. Essa abordagem é mais complexa, mas também mais flexível, redundante e resiliente.

🔗 [Fonte](https://aerospike.com/blog/vertical-vs-horizontal-scaling/)

### 6. Qual a relevância de organizar corretamente os dados em bancos relacionais?

Por meio da normalização de dados, as informações se tornam consistentes, os erros são removidos e reunidos em um formato semelhante para facilitar a interpretação e o uso. Seu objetivo é reduzir a redundância e a dependência das informações armazenadas, garantindo sua integridade e eliminando anomalias.

🔗 [Fonte](https://blog.invgate.com/pt/normalizacao-de-dados)

### 7. Como escolher entre SQL e NoSQL para um novo projeto?

A escolha entre SQL e NoSQL depende da estrutura de dados do seu projeto, das necessidades de desempenho e dos requisitos de escalabilidade.
**SQL:** estrutura e integridade
**NoSQL:** desempenho e flexibilidade

🔗 [Fonte](https://appwrite.io/blog/post/sql-vs-nosql)



## Comandos SQL

### 1. Qual é a finalidade do comando SELECT em SQL?
O comando **SELECT** permite definir critérios para realizar consultas aos registros que foram armazenados no banco de dados.
```
SELECT id, nome, cargo FROM funcionarios;
```
🔗 [Fonte](https://blog.betrybe.com/sql/?utm_term=&utm_campaign=Performance+Max+Cursos&utm_source=adwords&utm_medium=ppc&hsa_acc=1466424558&hsa_cam=21861374146&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=21850942791&gbraid=0AAAAACnih50XVID-p6yMbRiE4PHppj15u&gclid=Cj0KCQjwgpzIBhCOARIsABZm7vE6ALiYqB3ZXMsqGEwgG2m0mtneSdV2v0WapS2uCAPg0Hv5aMjN0msaAtiDEALw_wcB)

### 2. O que significam as siglas DML e DDL em bancos de dados?
O **DML** (Data Manipulation Language) é o subconjunto do SQL que define os comandos usados para manipular os dados armazenados em um banco.
Os comandos mais importantes desse subconjunto são: INSERT, DELETE e UPDATE.
O **DDL** (Data Definition Language) é o subconjunto SQL que apresenta comandos usados para gerenciar as estruturas do banco de dados.
Os comandos definidos pelo DDL são: CREATE, DROP e ALTER.

🔗 [Fonte](https://blog.betrybe.com/sql/?utm_term=&utm_campaign=Performance+Max+Cursos&utm_source=adwords&utm_medium=ppc&hsa_acc=1466424558&hsa_cam=21861374146&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=21850942791&gbraid=0AAAAACnih50XVID-p6yMbRiE4PHppj15u&gclid=Cj0KCQjwgpzIBhCOARIsABZm7vE6ALiYqB3ZXMsqGEwgG2m0mtneSdV2v0WapS2uCAPg0Hv5aMjN0msaAtiDEALw_wcB)
### 3. Para que serve a cláusula WHERE em consultas SQL?
O **WHERE** é usado para filtrar registros em uma consuta SQL, retornando somente os dados que atenden a uma condição especifica

🔗 [Fonte](https://blog.betrybe.com/sql/?utm_term=&utm_campaign=Performance+Max+Cursos&utm_source=adwords&utm_medium=ppc&hsa_acc=1466424558&hsa_cam=21861374146&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=21850942791&gbraid=0AAAAACnih50XVID-p6yMbRiE4PHppj15u&gclid=Cj0KCQjwgpzIBhCOARIsABZm7vE6ALiYqB3ZXMsqGEwgG2m0mtneSdV2v0WapS2uCAPg0Hv5aMjN0msaAtiDEALw_wcB)

### 4. Por que é fundamental estabelecer uma chave primária (PRIMARY KEY) em tabelas?
Essa chave é utilizada como identificador único da tabela, sendo representada por aquele campo (ou campos) que não receberá valores repetidos.
Com isso, ela garante a organização, integridade dos dados e facilitando relações entre tabelas.

🔗 [Fonte](https://www.devmedia.com.br/sql-aprenda-a-utilizar-a-chave-primaria-e-a-chave-estrangeira/37636?gad_source=1&gad_campaignid=22326280955&gbraid=0AAAAADrVyXHsdN2CMbI6WuMVKRoCX_J1d&gclid=Cj0KCQjwgpzIBhCOARIsABZm7vH-Tx5pgkf4iNQgIBrydwYdBNRd-LxjbOZTmotcnbF8mk5txvWnGLQaAr39EALw_wcB)

### 5. Como funciona o comando UPDATE e qual sua sintaxe básica?
O comando **UPDATE** é o comando SQL responsável por atualizar os dados já armazenados em uma tabela do banco. Ele pode ser usado tanto para atualizar um único registro quanto para alterar múltiplas informações de uma vez.

```
 UPDATE nome_da_tabela
 SET nome_da_coluna1 = valor_da_coluna1, nome_da_coluna2 = valor_da_coluna2
 WHERE condição;
 ```

🔗 [Fonte](https://blog.betrybe.com/sql-update/)

### 6. Qual a função do comando DELETE em SQL?
O comando SQL DELETE é usado para deletar os dados de uma ou mais linhas da tabela. É importante ressaltar que esse comando não exclui estruturas do banco, apenas os dados armazenados nele.
O comando DROP é usado para excluir toda a tabela, removendo sua estrutura de dados

🔗 [Fonte](https://blog.betrybe.com/sql/sql-delete/)

### 7. Como a cláusula ORDER BY organiza os resultados de uma consulta?
**ORDER BY** organiza os resultados de acordo com uma ou mais colunas da tabela, podendo definir a ordem do resultados como crescente ou decrescente.

🔗 [Fonte](https://www.devmedia.com.br/sql-order-by/41225?gad_source=1&gad_campaignid=22326280955&gbraid=0AAAAADrVyXHsdN2CMbI6WuMVKRoCX_J1d&gclid=Cj0KCQjwgpzIBhCOARIsABZm7vEubELrtIWsIjAo0g-R25FAvrKSlMQGYxCSn5ZMfuGZVhd2lwbR9dEaAs7hEALw_wcB)

### 8. Para que serve o comando LIMIT em consultas SQL?
**LIMIT** é uma cláusula SQL que especifica o número de linhas que devem ser retornadas no resultado de uma consulta.

🔗 [Fonte](https://www.devmedia.com.br/sql-limit/41216?gad_source=1&gad_campaignid=22326280955&gbraid=0AAAAADrVyXHsdN2CMbI6WuMVKRoCX_J1d&gclid=Cj0KCQjwgpzIBhCOARIsABZm7vFZ1O6KEQlEx7YYSm6zm2PzWt3CQEB9Qst6wtcy8a6kYA3pvHQsP3AaAm-MEALw_wcB)


## Outros Conceitos

## 1. Por que é importante integrar o banco de dados com a camada de backend da aplicação?
No contexto do back-end, eles servem como uma ponte entre o front-end e os dados que a aplicação manipula, garantindo que o fluxo de informações seja rápido, seguro e confiável. Seja para recuperar o histórico de compras de um cliente ou armazenar as configurações de um usuário, o banco de dados está sempre no centro da ação.

🔗 [Fonte](https://www.stackx.com.br/post/banco-de-dados-e-back-end)

## 2. O que são views (visões) em bancos de dados e quais suas vantagens?
Uma view é uma maneira alternativa de observação de dados de uma ou mais entidades (tabelas), que compõem uma base de dados. Pode ser considerada como uma tabela virtual ou uma consulta armazenada.
**As vantagens de usar views são:**
Economizar tempo com retrabalho, Velocidade de acesso às informações, Mascarar complexidade do banco de dados,
Simplifica o gerenciamento de permissão de usuários, Organizar dados a serem exportados para outros aplicativos

🔗 [Fonte](https://www.devmedia.com.br/introducao-a-views/1614)

## 3. Quais são as propriedades ACID e por que são cruciais para transações?
- **Atomicidade:** cada instrução de uma transação (leitura, gravação, atualização ou exclusão de dados) é tratada como uma única unidade. Ou as instruções são todas executadas ou nenhuma é executada. Essa propriedade evita perda ou corrupção de dados, como quando a fonte de dados de streaming falha no meio do fluxo.
- **Consistência:** garante que as transações apenas modifiquem as tabelas de maneiras predefinidas e previsíveis. A consistência transacional mantém as tabelas consistentes em caso de corrupção de dados ou erros, evitando resultados de execução não intencionais.
- **Isolamento:** vários usuários podem ler e gravar na mesma tabela ao mesmo tempo, mas as transações são isoladas para que as simultâneas não interfiram ou afetem umas às outras. Na verdade, cada solicitação é tratada como se estivesse ocorrendo de forma independente, mesmo que ocorram simultaneamente.
- **Durabilidade:** garante que as alterações de dados feitas por transações executadas com sucesso sejam preservadas, mesmo em caso de falha do sistema.

🔗 [Fonte](https://www.databricks.com/br/glossary/acid-transactions)

## 4. O que estabelece o Princípio do Privilégio Mínimo em segurança de bancos de dados?
O princípio do privilégio mínimo (PoLP) é um conceito de segurança da informação que sustenta que um usuário ou entidade deve ter acesso apenas aos dados, recursos e aplicativos específicos necessários para concluir uma tarefa exigida.

🔗 [Fonte](https://www.paloaltonetworks.com.br/cyberpedia/what-is-the-principle-of-least-privilege)