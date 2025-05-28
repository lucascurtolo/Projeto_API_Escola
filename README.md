# 🏫 Projeto API Escola

Uma API REST completa para gerenciamento de sistema escolar, desenvolvida em Python utilizando Flask. O projeto oferece endpoints para gestão de alunos, professores e turmas, com documentação interativa via Swagger.

## 📋 Funcionalidades

- **Gestão de Alunos**: CRUD completo (Create, Read, Update, Delete)
- **Gestão de Professores**: CRUD completo com todas as operações
- **Gestão de Turmas**: Sistema completo de gerenciamento de turmas
- **Documentação Interativa**: Interface Swagger para teste dos endpoints
- **Containerização**: Suporte completo ao Docker
- **Sistema de Cache**: Otimização de performance com cache integrado

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **SQLite** - Banco de dados
- **Swagger** - Documentação da API
- **Docker** - Containerização
- **Flask-SQLAlchemy** - ORM para banco de dados

## 📁 Estrutura do Projeto

```
PROJETO_API_ESCOLA/
├── Controllers/
│   ├── alunos_routes.py      # Rotas para gerenciamento de alunos
│   ├── professores_routes.py # Rotas para gerenciamento de professores
│   └── turmas_routes.py      # Rotas para gerenciamento de turmas
├── Models/
│   ├── alunos.py            # Model de alunos
│   ├── professores.py       # Model de professores
│   ├── turmas.py            # Model de turmas
│   └── models.py            # Configurações dos models
├── swagger/
│   ├── swagger_config.py    # Configuração do Swagger
│   └── __init__.py
├── docker/
│   ├── docker-compose.yml   # Orquestração dos containers
│   └── Dockerfile           # Imagem Docker da aplicação
├── App.py                   # Arquivo principal da aplicação
├── Config.py                # Configurações da aplicação
├── requirements.txt         # Dependências do projeto
├── wsgi.py                  # WSGI para deploy
├── tests.py                 # Testes da aplicação
└── memory                   # Arquivo de cache/memória
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)
- Docker (opcional)

### Instalação Local

1. **Clone o repositório**
```bash
git clone https://github.com/lucascurtolo/Projeto_API_Escola.git
cd Projeto_API_Escola
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
python App.py
```

A aplicação será iniciada em `http://localhost:8000`

### Instalação com Docker

1. **Build e execute com Docker Compose**
```bash
docker-compose up --build
```

2. **Ou execute apenas o container**
```bash
docker build -t api-escola .
docker run -p 8000:8000 api-escola
```

## ⚙️ Configurações

A aplicação utiliza as seguintes configurações padrão:

- **Host**: 0.0.0.0 (aceita conexões de qualquer IP)
- **Porta**: 8000
- **Debug**: Habilitado (desenvolvimento)
- **Banco de Dados**: SQLite em memória (`sqlite:///memory`)

### Configurações Personalizadas

As configurações podem ser modificadas no arquivo `Config.py`:

```python
app.config['HOST'] = '0.0.0.0'      # Host da aplicação
app.config['PORT'] = 8000           # Porta da aplicação  
app.config['DEBUG'] = True          # Modo debug
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memory"  # Banco de dados
```

## 📚 Endpoints da API

A API oferece endpoints completos para todas as entidades:

### 👨‍🎓 Alunos
- `GET /alunos` - Listar todos os alunos
- `GET /alunos/{id}` - Buscar aluno por ID
- `POST /alunos` - Criar novo aluno
- `PUT /alunos/{id}` - Atualizar aluno
- `DELETE /alunos/{id}` - Deletar aluno por ID
- `DELETE /alunos` - Deletar todos os alunos

### 👨‍🏫 Professores
- `GET /professores` - Listar todos os professores
- `GET /professores/{id}` - Buscar professor por ID
- `POST /professores` - Criar novo professor
- `PUT /professores/{id}` - Atualizar professor
- `DELETE /professores/{id}` - Deletar professor por ID
- `DELETE /professores` - Deletar todos os professores

### 🏛️ Turmas
- `GET /turmas` - Listar todas as turmas
- `GET /turmas/{id}` - Buscar turma por ID
- `POST /turmas` - Criar nova turma
- `PUT /turmas/{id}` - Atualizar turma
- `DELETE /turmas/{id}` - Deletar turma por ID
- `DELETE /turmas` - Deletar todas as turmas

**Base URL**: `http://localhost:8000`

## 📖 Documentação Swagger

Após iniciar a aplicação, acesse a documentação interativa:

```
http://localhost:8000/swagger
```

A interface Swagger permite:
- Visualizar todos os endpoints disponíveis
- Testar as requisições diretamente no navegador
- Ver exemplos de requisições e respostas
- Entender a estrutura dos dados

## 🗄️ Banco de Dados

O projeto utiliza **SQLite em memória** como banco de dados. Isso significa que:

- O banco é criado automaticamente na primeira execução
- Os dados são armazenados apenas durante a execução da aplicação
- Quando a aplicação é reiniciada, os dados são perdidos
- Ideal para desenvolvimento e testes

### Estrutura das Tabelas

O banco de dados é criado automaticamente com as tabelas:
- **Alunos**: Informações dos estudantes
- **Professores**: Dados dos educadores  
- **Turmas**: Informações das classes

### Persistência de Dados

Para usar um banco persistente, altere a configuração em `Config.py`:
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///escola.db"  # Banco persistente
```

## 🧪 Testes

Execute os testes da aplicação:

```bash
python tests.py
```

## 🚀 Deploy

### Deploy Local
A aplicação pode ser executada localmente usando:
```bash
python wsgi.py
```

### Deploy com Docker
Para ambientes de produção, utilize Docker:
```bash
docker-compose -f docker-compose.yml up -d
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Lucas Curtolo** **Marcelo Augusto** **Eduardo Omena** **Carlos Eduardo** **Vinícius Gama**
- GitHub: [@lucascurtolo](https://github.com/lucascurtolo)

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas, abra uma [issue](https://github.com/lucascurtolo/Projeto_API_Escola/issues) no repositório.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
