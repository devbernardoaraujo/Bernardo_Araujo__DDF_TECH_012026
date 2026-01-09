# Bernardo_Araujo__DDF_TECH_012026

# Case Técnico: Ingestão e Governança de Dados - Dadosfera

## 🎥 Apresentação em Vídeo
Confira a demonstração completa da solução, desde a ingestão dos dados na AWS até a criação dos dashboards na Dadosfera:

👉 [Assista ao vídeo de apresentação do Case aqui](https://youtu.be/HUewzQXcApM)

## 1. Introdução
Este projeto apresenta a solução para o case técnico de ingestão, catalogação e análise de dados utilizando a plataforma **Dadosfera** e infraestrutura **AWS**. O objetivo foi processar uma volumetria de +250k registros, garantindo a integridade e a disponibilidade dos dados para análise de negócio.

![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Database%20at%20AWS%20Aurora%20and%20RDS.PNG)

## 2. Arquitetura da Solução
A arquitetura foi desenhada para ser escalável e segura, utilizando:
* **Armazenamento de Origem:** Arquivos CSV (Vendas, Clientes, Produtos, Eventos).
* **Banco de Dados Operacional:** AWS RDS (MySQL).
* **Plataforma de Dados:** Dadosfera (Coleta, Catálogo e Pipeline).
* **Linguagem de Ingestão:** Python 3.14 (SQLAlchemy + Pandas).

![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Database%20at%20MySQL.PNG)


## 3. Etapas do Projeto

### 3.1. Gestão do Projeto (Kanban)
Para organizar o fluxo de trabalho e garantir o cumprimento de todos os requisitos do case, utilizei o módulo de **Kanban**. É possível visualizá-lo na aba Projects do próprio repositório no GitHub.

* **To Do:** Planejamento e arquitetura.
* **Doing:** Ingestão Python e configuração de Pipelines.
* **Done:** Catalogação, consultas SQL e Visualização de Dados.

![Kanban do Projeto](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Kanban.PNG)

### 3.2. Ingestão de Dados (ETL)
Para a carga de dados no **AWS RDS**, foi desenvolvido um script customizado em Python para superar limitações de ferramentas visuais em altas volumetrias (+250k linhas).
* **Estratégia:** Carga em lotes (*Chunks*) de 20.000 registros para otimização de memória e estabilidade da conexão.
* **Infraestrutura:** Configuração de *Security Groups* na AWS para permitir a comunicação segura entre o script local, o RDS e a Dadosfera.

### 3.3. Pipeline na Dadosfera
Configuração de um pipeline de dados na plataforma Dadosfera utilizando:
* **Tipo de Carga:** Full Load (Carga Inicial).
* **Conector:** MySQL RDS.
* **Frequência:** Única Extração (Batch).
![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Pipeline%20at%20Dadosfera.PNG)

### 3.4. Governança e Catálogo
Após a ingestão, os dados foram catalogados na Dadosfera:
* **Enriquecimento de Metadados:** Adição de descrições amigáveis e etiquetas (tags).
* **Ajuste de Tipagem:** Tratamento de campos de data (ex: `signup_date`) de String para `DATETIME` na camada de processamento.
  ![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/catalog.PNG)

## 4. Dicionário de Dados (Resumo)

| Tabela | Descrição | Principais Colunas |
| :--- | :--- | :--- |
| `customers` | Dados cadastrais dos clientes | `customer_id`, `signup_date`, `email` , `state`, `city`,  |
| `orders` | Histórico de transações | `order_id`, `total_price`, `order_date`, `customer_id`, `channel`, `shipping_state`, `shipping_city`|
| `products` | Catálogo de itens disponíveis | `product_id`, `category`, `subcategory`, `price`, `title`, `subtitle`, `base_price`, `attributes_json`, `created_at`, `attributes_json` `description`, `brand`|
| `events` | Logs de navegação e interação | `event_id`, `event_type`, `product_id`, `customer_id`, `device`, `ts`, `referrer`|

### 4.1. Concentração de Clientes por Estado
**Questão:** Qual a distribuição geográfica da nossa base de clientes para logística e marketing?  
![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Quantidade%20de%20Clientes%20por%20Estado.PNG)

### 4.2. Ranking de Brands
**Questão:** Qual é a marca com mais produtos cadastrados?
![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Ranking%20de%20Marcas%20SQL.PNG)

### 4.3. Status dos pedidos
**Questão:** Como estão o status dos pedidos?
![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Status%20dos%20pedidos%20SQL.PNG)

### 4.4. Volume de Pedidos por Canal e Estado
**Questão:** Quais canais de venda são mais eficazes em cada região?
![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Volume%20de%20pedidos%20por%20canal%20e%20estado%20SQL.PNG)

### 4.5. Comportamento do cliente
**Questão:** Como funciona o comportamento do cliente na plataforma?
![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Comportamento%20do%20Usuario%20SQL.PNG)

## 5. Dashboard Final (Business Intelligence)
Para consolidar os resultados, foi criado um Dashboard na plataforma Metabase (integrada à Dadosfera), permitindo a visualização executiva dos KPIs de vendas, clientes e produtos.
![Image Alt](https://github.com/devbernardoaraujo/Bernardo_Araujo__DDF_TECH_012026/blob/55e97afa06d5cc67225436f8e121bc1401126410/prints/Dashboard%20do%20Ecommerce%20com%20as%20consultas%20SQL.PNG)


## 6. Como Executar o Projeto
1. Clone o repositório.
2. Configure as variáveis de ambiente (Host RDS, User, Password).
3. Instale as dependências: `pip install pandas sqlalchemy pymysql`.
4. Execute o script `index.py` para popular o RDS.
5. Inicie o coletor na plataforma Dadosfera.

---
**Desenvolvido por:** [Bernardo Botelho de Araujo]
**Data:** Janeiro de 2026
