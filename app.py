from flask import Flask, jsonify, request
from shared.config import configure_app
from models import db, Categoria
from flask_cors import CORS

app = Flask(__name__)
configure_app(app)
db.init_app(app)
CORS(app)


# C - Criar uma nova categoria 
@app.route('/categorias', methods=['POST'])
def criar_categoria():
    dados = request.json
    nome_categoria = dados.get("nome")

    if not nome_categoria:
        return jsonify({"erro": "Nome obrigatório"}), 400

    categoria_existente = Categoria.query.filter_by(nome=nome_categoria).first()
    if categoria_existente:
        return jsonify({"erro": "Categoria já existe"}), 400

    nova_categoria = Categoria(nome=nome_categoria)
    db.session.add(nova_categoria)
    db.session.commit()

    return jsonify({"id": nova_categoria.id}), 201

# R - Retorna as categorias existentes
@app.route('/categorias', methods=['GET'])
def listar_categorias():
    categorias = Categoria.query.all()
    return jsonify([{"id": c.id, "nome": c.nome} for c in categorias])

# U - Alterações nos dados da categoria
@app.route('/categorias/<int:id>', methods=['PUT'])
def atualizar_categoria(id):
    dados = request.json
    categoria = Categoria.query.get_or_404(id)
    novo_nome = dados.get("nome")
    if not novo_nome:
        return jsonify({"erro": "Nome da categoria é obrigatório"}), 400
    categoria.nome = novo_nome
    db.session.commit()
    return jsonify({"mensagem": "Categoria atualizada com sucesso!"})

# D - Excluir uma categoria existente
@app.route('/categorias/<int:id>', methods=['DELETE'])
def deletar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({"mensagem": "Categoria deletada com sucesso!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')
