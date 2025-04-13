### Desenvolvimento Full Stack - PUC-Rio

## MVP Back End com Flask + Interface React:
# 🛒 Big Loja (loja virtual) 

O objetivo do MVP foi desenvolver uma loja virtual, contemplando tanto a experiência do usuário quanto o gerenciamento administrativo do sistema. 

👤 Usuário: pode navegar entre produtos, filtrar por categoria ou preço, adicionar e manipular itens no carrinho, finalizar compras e acompanhar pedidos no histórico.

🛠️ Administrador: conta com um painel de controle que permite o cadastro e gerenciamento de produtos e categorias, além de visualizar todos os pedidos realizados (incluindo a opção de cancelamento de pedidos).

---

## 🗂️ API de Categorias (backend_categorias)

Esse repositório é o backend responsável por gerenciar as categorias dos produtos da loja virtual. Ele permite cadastrar, listar, editar e remover categorias. Tudo feito com Flask, e rodando como container Docker junto dos demais serviços.

---

## 🚀 O que essa API faz

- ➕ **Cadastrar nova categoria**
- 📋 **Listar categorias existentes**
- ✏️ **Editar uma categoria**
- ❌ **Excluir uma categoria**

---

## 🔄 Principais rotas

| Método | Rota                  | Função                             |
|--------|-----------------------|------------------------------------|
| GET    | `/categorias`         | Lista todas as categorias          |
| POST   | `/categorias`         | Cria uma nova categoria            |
| PUT    | `/categorias/<id>`    | Atualiza uma categoria existente   |
| DELETE | `/categorias/<id>`    | Remove uma categoria (se possível) |

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10**
- **Flask** com `flask_sqlalchemy` e `flask_cors`
- **Docker** para containerização

---

## 📦 Como rodar o projeto

Esse container faz parte de um sistema completo e depende dos seguintes repositórios para funcionar corretamente:

### Estrutura do sistema:

- 🌐 **API externa**: [FakeStore](https://fakestoreapi.com/) → usada para popular a base com produtos fictícios. O modelo `Produto` foi estruturado com base nos dados dessa API (nome, valor, imagem, etc).
- 🔹 [`backend_categorias`] ← Você está nesse repositório
- 🔹 [`backend_produtos`](https://github.com/marcos-grando/mvp_backend_produtos) → responsável pelo gerenciamento dos produtos (incluindo uploads das imagens dos produtos)
- 🔹 [`backend_compras`](https://github.com/marcos-grando/mvp_backend_compras) → responsável por registrar e consultar compras feitas na loja
- 🔸 [`backend_shared`](https://github.com/marcos-grando/mvp_backend_shared) → módulo auxiliar compartilhado (banco de dados, pastas de upload, etc)
- 💠 [`frontend`](https://github.com/marcos-grando/mvp_frontend_bigloja) → interface React responsável pela exibição dos produtos, carrinho, compras e painel administrativo, conectando-se às APIs

**Esse container precisa acessar um volume compartilhado (`backend_shared`) para acessar:**
 - O banco de dados SQLite
 - Configuração centralizada da aplicação Flask em `config.py`

***OBS: `docker-compose`***  
 - O sistema utiliza 3 APIs diferentes, com dependências entre os módulos  
 - Por isso, é recomendado utilizar o `docker-compose`, que está no repositório `frontend`  
 - Isso evita a necessidade de buildar e subir manualmente cada componente um por um

---

## ▶️ Como rodar

1. Clone esse repositório  
2. Certifique-se de que os outros containers estão na mesma estrutura  
3. No terminal, execute:

```bash
docker-compose up --build -d
```

---

## 🧠 Observações
Esse repositório faz parte de um MVP acadêmico. O sistema foi dividido em partes que se comunicam entre si por rotas. O backend foi feito com Flask (Python) e frontend com React.js.

### 🙋‍♂️ Autor
Desenvolvido por Marcos Grando ✌️

"""
