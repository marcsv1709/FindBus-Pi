# 🚌 **FindBus**

## 📋 **Índice**

- Sobre o Projeto
- Funcionalidades
- Tecnologias Utilizadas
- Instalação
- Configuração
- Uso
- Endpoints da API
- Contribuindo
- Licença

---

## 🛠️ **Sobre o Projeto**

O **FindBus** é um sistema de gerenciamento de rotas de ônibus com o backend desenvolvido para o Projeto integrador com Flask para fornecer funcionalidades de autenticação e gerenciamento de usuários. Ele permite que os usuários se registrem, façam login, editem seus perfis, e redefinam suas senhas.

## 🌟 **Funcionalidades**

- **Autenticação com JWT**: Login seguro usando tokens JWT.
- **Registro de Usuário**: Criação de novos usuários com validação de dados.
- **Atualização de Perfil**: Permite que o usuário edite suas informações.
- **Alteração de Senha**: Redefina sua senha com segurança.
- **Proteção de Rotas**: Rotas protegidas utilizando Flask-Login e JWT.

## 🧰 **Tecnologias Utilizadas**

- **Backend**: Flask, Flask-Login, Flask-JWT-Extended
- **Banco de Dados**: SQLite (ou PostgreSQL para produção)
- **Frontend**: Axios para consumo da API
- **Autenticação**: JWT (JSON Web Token)
- **Outras Bibliotecas**: Flask-Migrate, Flask-SQLAlchemy

## 🚀 **Instalação**

1. Clone o repositório:
   git clone https://github.com/BrnFbrian/back.git

2. Crie e ative um ambiente virtual:
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

## 🗄️ **Migrações do Banco de Dados**

Inicialize o banco de dados e aplique as migrações:

flask db init
flask db migrate
flask db upgrade

## 🏃 **Uso**

Inicie o servidor Flask:

python.exe .\main.py

## 📚 **Endpoints da API**

### **Autenticação**

- **POST** `/register`

  - Registra um novo usuário.

- **POST** `/login`

  - Realiza login e retorna o token JWT.

- **POST** `/auth/refresh-token`
  - Atualiza o token JWT.

### **Perfil**

- **GET** `/profile`

  - Retorna os dados do usuário logado.

- **PUT** `/profile/edit`

  - Edita o perfil do usuário.

- **POST** `/new-password`
  - Redefine a senha do usuário.

## 💬 **Contato**

- **Nome**: Felipe Brian
- **GitHub**: https://github.com/brnfbrian

---

Feito por [Brian](https://github.com/seu-usuario).
