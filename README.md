# 📦 Gestão de Stock

Sistema web de **gestão de stock, produtos, categorias e movimentos de inventário**, desenvolvido para facilitar o controlo de produtos e operações de entrada e saída de mercadorias.

O projeto foi desenvolvido com foco em **simplicidade, segurança, organização e utilização através do navegador**, incluindo suporte para dispositivos móveis.

## 🚀 Funcionalidades

* 🔐 Autenticação e controlo de acesso
* 👤 Gestão de utilizadores e funções
* 📦 Gestão de produtos
* 🗂️ Gestão de categorias
* 📥 Registo de entradas de stock
* 📤 Registo de saídas de stock
* 📊 Dashboard com informações do stock
* ⚠️ Identificação de produtos com stock baixo
* 🔎 Pesquisa e consulta de produtos
* ✏️ Edição de informações
* 🗑️ Remoção de registos
* 📋 Histórico de movimentos
* 📱 Interface responsiva para computador, tablet e telemóvel

## 🛠️ Tecnologias

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Alembic**
* **PostgreSQL**
* **JWT**
* **bcrypt**

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Font Awesome**

### Infraestrutura

* **Git / GitHub**
* **Render**
* **Neon PostgreSQL**

## 🏗️ Arquitetura

O sistema utiliza uma arquitetura separada entre frontend e backend:

```text
                    Gestão de Stock
                          │
             ┌────────────┴────────────┐
             │                         │
          Frontend                  Backend
       HTML/CSS/JS                Python/FastAPI
             │                         │
             └────────── API ──────────┘
                                       │
                                  PostgreSQL
```

O frontend comunica com a API através de requisições HTTP, enquanto o backend é responsável pela autenticação, regras de negócio, validação e persistência dos dados.

## 🔐 Segurança

O sistema utiliza autenticação baseada em **JWT** e proteção das rotas da API.

As palavras-passe são armazenadas utilizando **hash com bcrypt**, não sendo guardadas em texto simples.

As funcionalidades protegidas são verificadas no backend, evitando depender exclusivamente da proteção existente no frontend.

## 📂 Estrutura do projeto

Uma estrutura simplificada do projeto:

```text
project/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── routers/
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── requirements.txt
│   └── ...
│
└── frontend/
    ├── pages/
    ├── css/
    ├── js/
    └── assets/
```

A estrutura pode variar conforme a versão atual do projeto.

## ⚙️ Execução local

### 1. Clonar o projeto

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente

Criar um arquivo `.env` com as configurações necessárias, incluindo a ligação com o PostgreSQL e as configurações de autenticação.

Exemplo:

```env
DATABASE_URL=postgresql://usuario:senha@host:5432/database
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> **Nunca publique o `.env` no GitHub.**

### 6. Executar o backend

```bash
uvicorn app.main:app --reload
```

A API ficará disponível, por padrão, em:

```text
http://127.0.0.1:8000
```

A documentação interativa da API pode ser acessada através de:

```text
http://127.0.0.1:8000/docs
```

## 🗄️ Banco de dados

O projeto utiliza **PostgreSQL** como sistema de gestão de base de dados.

As alterações estruturais do banco podem ser geridas através do **Alembic**.

Para criar uma migration:

```bash
alembic revision --autogenerate -m "descricao"
```

Para aplicar as migrations:

```bash
alembic upgrade head
```

## 🌐 Deploy

O projeto foi preparado para utilização em ambiente de produção com:

* **Render** para hospedagem do backend;
* **Neon** para PostgreSQL;
* **GitHub** para versionamento e hospedagem do frontend.

A separação entre frontend e backend permite que cada componente seja atualizado de forma independente.

## 📱 Responsividade

A interface foi desenvolvida para funcionar em diferentes tamanhos de ecrã:

* 💻 Desktop
* 📱 Telemóvel
* 📲 Tablet

As tabelas, formulários, menus, modais e componentes principais possuem regras específicas para dispositivos menores.

## 🔮 Próximas funcionalidades

O projeto pode evoluir para uma solução comercial de gestão de stock, incluindo:
* 👥 Gestão de clientes
* 🚚 Gestão de fornecedores
* 🎪 Gestão de eventos

## 🎯 Objetivo

O objetivo do projeto é fornecer uma solução simples e acessível para empresas que precisam de controlar os seus produtos e operações de stock sem depender de sistemas complexos ou equipamentos especializados.

## 👨‍💻 Autor

**Albino Mareleco**

Projeto desenvolvido como parte da exploração e desenvolvimento de soluções de software para gestão empresarial.

## ✅ VETOR CONFIRMADO

**Tecnologia, precisão e execução.**

Desenvolvido por **Albino Mareleco**


## 📄 Licença

Este projeto encontra-se em desenvolvimento. A utilização, distribuição ou comercialização do código deve respeitar as condições definidas pelo autor.
