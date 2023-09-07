from flask_restful import Resource, request
from flask import jsonify
from models import db, ProdutosSchema,Produtos,Usuario, UsuarioSchema,Fornecedor,FornecedorSchema,Carrinho,CarrinhoSchema

class ProdutosResource(Resource):
    # Cadastro de Produtos
    def post(self):
        data = request.json

        # Verifique se o fornecedor existe
        fornecedor_id = data.get('fornecedor_id')
        fornecedor = Fornecedor.query.get(fornecedor_id)

        if not fornecedor:
            return {"message": "Fornecedor não encontrado"}, 400

        # Continue com a criação do produto
        produtos = Produtos(
            nome_produto=data['nome_produto'],
            price=data['price'],
            quant=data['quant'],
            tipo=data['tipo'],
            fornecedor_id=fornecedor_id
        )

        db.session.add(produtos)
        db.session.commit()
        return ProdutosSchema().dump(produtos), 201
    
    #Listagem de Produtos
    def get(self, produtos=None):
        if produtos is None:
            produtos = Produtos.query.all()
            return ProdutosSchema(many=True).dump(produtos)
        
        produtos = Produtos.query.get(produtos)
        if not produtos:
            return {"message": "Produtos não encontrado"}, 404
        return ProdutosSchema().dump(produtos)
    
    #Alteração de produtos
    def put(self, produtos):
        produtos = Produtos.query.get(produtos)
        if not produtos:
            return jsonify({"message": "Produtos não encontrado"}), 404

        data = request.json
        produtos.nome_produto = data.get('nome_produto', produtos.nome_produto)
        produtos.price = data.get('price', produtos.price)
        produtos.quant = data.get('quant', produtos.quant)
        produtos.tipo = data.get('tipo', produtos.tipo)
        produtos.fornecedor_id = data.get('fornecedor_id',produtos.fornecedor_id)

        db.session.commit()

        return jsonify(ProdutosSchema().dump(produtos))

    
    #Exclusão de produtos
    def delete(self, produtos):
        produtos = Produtos.query.get(produtos)
        if not produtos:
            return jsonify({"message": "Produtos não encontrado"}), 404
        
        db.session.delete(produtos)
        db.session.commit()

        return jsonify({"message": "Produtos excluído com sucesso"}), 204



class UsuarioResource(Resource):
    #Cadastro de Usuarios
    def post(self):
        data = request.json
        usuarios = Usuario(nome_usuario=data['nome_usuario'], login=data['login'], senha=data['senha'])
        db.session.add(usuarios)
        db.session.commit()
        return UsuarioSchema().dump(usuarios),201
    
    #Listagem de Usuarios
    def get(self, usuarios=None):
        if usuarios is None:
            usuarios = Usuario.query.all()
            return UsuarioSchema(many=True).dump(usuarios)
        
        usuarios = Usuario.query.get(usuarios)
        if not usuarios:
            return {"message": "Usuario não encontrado"}, 404
        return UsuarioSchema().dump(usuarios)
    
    #Alteração de usuarios
    def put(self, usuarios_id):
        usuario = Usuario.query.get(usuarios_id)
        if not usuario:
            return {"message": "usuarios não encontrado"}, 404

        data = request.json
        usuario.nome_usuario = data.get('nome_usuario', usuario.nome_usuario)
        usuario.login= data.get('login', usuario.login)
        usuario.senha = data.get('senha', usuario.senha)

        db.session.commit()

        return UsuarioSchema().dump(Usuario)
    
    #Exclusão de usuarios
    def delete(self, usuarios_id):
        usuario = Usuario.query.get(usuarios_id)
        if not usuario:
            return {"message": "usuarios não encontrado"}, 404
        
        db.session.delete(usuario)
        db.session.commit()

        return {"message": "usuarios excluído com sucesso"}, 204


class FornecedorResource(Resource):
    #Cadastro de fornecedores
    def post(self):
        data = request.json
        fornecedores = Fornecedor(nome_fornecedor=data['nome_fornecedor'])
        db.session.add(fornecedores)
        db.session.commit()
        return FornecedorSchema().dump(fornecedores),201
    
    #Listagem de fornecedores
    def get(self, fornecedores=None):
        if fornecedores is None:
            fornecedores = Fornecedor.query.all()
            return FornecedorSchema(many=True).dump(fornecedores)
        
        fornecedores = Fornecedor.query.get(fornecedores)
        if not fornecedores:
            return {"message": "fornecedor não encontrado"}, 404
        return FornecedorSchema().dump(fornecedores)
    
    #Alteração de fornecedores
    def put(self, fornecedores_id):
        fornecedor = Fornecedor.query.get(fornecedores_id)
        if not fornecedor:
            return {"message": "fornecedors não encontrado"}, 404

        data = request.json
        fornecedor.nome_fornecedor = data.get('nome_fornecedor', fornecedor.nome_fornecedor)

        db.session.commit()

        return FornecedorSchema().dump(fornecedor)
    
    #Exclusão de fornecedors
    def delete(self, fornecedores_id):
        fornecedor = Fornecedor.query.get(fornecedores_id)
        if not fornecedor:
            return {"message": "fornecedores não encontrado"}, 404
        
        db.session.delete(fornecedor)
        db.session.commit()

        return {"message": "fornecedores excluído com sucesso"}, 204

class CarrinhoResource(Resource):
    # Cadastro de carrinhos
    def post(self):
        data = request.json

        # Verifique se o usuário existe
        usuario_id = data.get('usuario_id')
        usuario = Usuario.query.get(usuario_id)

        if not usuario:
            return {"message": "Usuário não encontrado"}, 400

        # Continue com a criação do carrinho
        carrinhos = Carrinho(
            usuario_id=usuario_id,
            produtos_id=data['produtos_id']
        )

        db.session.add(carrinhos)
        db.session.commit()
        return CarrinhoSchema().dump(carrinhos), 201
    
    #Listagem de carrinhos
    def get(self, carrinhos=None):
        if carrinhos is None:
            carrinhos = Carrinho.query.all()
            return CarrinhoSchema(many=True).dump(carrinhos)
        
        carrinhos = Carrinho.query.get(carrinhos)
        if not carrinhos:
            return {"message": "Carrinho não encontrado"}, 404
        return CarrinhoSchema().dump(carrinhos)
    
    #Alteração de carrinhos
    def put(self, carrinhos_id):
        carrinho = Carrinho.query.get(carrinhos_id)
        if not carrinho:
            return {"message": "Carrinho não encontrado"}, 404

        data = request.json
        carrinho.usuario_id= data.get('usuario_id', carrinho.usuario_id)
        carrinho.produtos_id = data.get('produtos_id', carrinho.produtos_id)

        db.session.commit()

        return CarrinhoSchema().dump(carrinho)
    
    #Exclusão de carrinhos
    def delete(self, carrinhos_id):
        carrinho = Carrinho.query.get(carrinhos_id)
        if not carrinho:
            return {"message": "Carrinho não encontrado"}, 404
        
        db.session.delete(carrinho)
        db.session.commit()

        return {"message": "Carrinho excluído com sucesso"}, 204
    
    def post(self):
        data = request.json
        usuario_id = data['usuario_id']
        produtos_id = data['produtos_id']

        # Verificar se o produto existe
        produto = Produtos.query.get(produtos_id)
        if not produto:
            return {"message": "Produto não encontrado"}, 404

        quantidade_adicionada = data.get('quantidade_adicionada', 1)

        # Verificar se a quantidade em estoque é suficiente
        if produto.quant < quantidade_adicionada:
            return {"message": "Quantidade insuficiente em estoque"}, 400

        # Atualizar o estoque do produto
        produto.quant -= quantidade_adicionada
        db.session.add(produto)

        carrinhos = Carrinho(usuario_id=usuario_id, produtos_id=produtos_id, quantidade=quantidade_adicionada)
        db.session.add(carrinhos)
        db.session.commit()
        return CarrinhoSchema().dump(carrinhos), 201



