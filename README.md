# Bernardo_Araujo__DDF_TECH_012026

# Case Técnico: Ingestão e Governança de Dados - Dadosfera

## 1. Introdução
Este projeto apresenta a solução para o case técnico de ingestão, catalogação e análise de dados utilizando a plataforma **Dadosfera** e infraestrutura **AWS**. O objetivo foi processar uma volumetria de +250k registros, garantindo a integridade e a disponibilidade dos dados para análise de negócio.

## 2. Arquitetura da Solução
A arquitetura foi desenhada para ser escalável e segura, utilizando:
* **Armazenamento de Origem:** Arquivos CSV (Vendas, Clientes, Produtos, Eventos).
* **Banco de Dados Operacional:** AWS RDS (MySQL).
* **Plataforma de Dados:** Dadosfera (Coleta, Catálogo e Pipeline).
* **Linguagem de Ingestão:** Python 3.14 (SQLAlchemy + Pandas).



## 3. Etapas do Projeto

### 3.1. Ingestão de Dados (ETL)
Para a carga de dados no **AWS RDS**, foi desenvolvido um script customizado em Python para superar limitações de ferramentas visuais em altas volumetrias (+250k linhas).
* **Estratégia:** Carga em lotes (*Chunks*) de 20.000 registros para otimização de memória e estabilidade da conexão.
* **Infraestrutura:** Configuração de *Security Groups* na AWS para permitir a comunicação segura entre o script local, o RDS e a Dadosfera.

### 3.2. Pipeline na Dadosfera
Configuração de um pipeline de dados na plataforma Dadosfera utilizando:
* **Tipo de Carga:** Full Load (Carga Inicial).
* **Conector:** MySQL RDS.
* **Frequência:** Única Extração (Batch).

### 3.3. Governança e Catálogo
Após a ingestão, os dados foram catalogados na Dadosfera:
* **Enriquecimento de Metadados:** Adição de descrições amigáveis e etiquetas (tags).
* **Ajuste de Tipagem:** Tratamento de campos de data (ex: `signup_date`) de String para `DATETIME` na camada de processamento.

## 4. Dicionário de Dados (Resumo)

| Tabela | Descrição | Principais Colunas |
| :--- | :--- | :--- |
| `customers` | Dados cadastrais dos clientes | `customer_id`, `signup_date`, `email` , `state`, `city`,  |
| `orders` | Histórico de transações | `order_id`, `total_price`, `order_date`, `customer_id`, `channel`, `shipping_state`, `shipping_city`|
| `products` | Catálogo de itens disponíveis | `product_id`, `category`, `subcategory`, `price`, `title`, `subtitle`, `base_price`, `attributes_json`, `created_at`, `attributes_json` `description`, `brand`|
| `events` | Logs de navegação e interação | `event_id`, `event_type`, `product_id`, `customer_id`, `device`, `ts`, `referrer`|

## 5. Como Executar o Projeto
1. Clone o repositório.
2. Configure as variáveis de ambiente (Host RDS, User, Password).
3. Instale as dependências: `pip install pandas sqlalchemy pymysql`.
4. Execute o script `index.py` para popular o RDS.
5. Inicie o coletor na plataforma Dadosfera.

---
**Desenvolvido por:** [Seu Nome]
**Data:** Janeiro de 2026
