from flask_restful import Resource, request
from flask import jsonify
from models import db, ProdutosSchema,Produtos,Usuarios, UsuariosSchema

class ProdutosResource(Resource):
    #Cadastro de Produtos
    def post(self):
        data = request.json
        produtos = Produtos(nome_produto=data['nome_produto'], price=data['price'], fabric=data['fabric'], quant=data['quant'], tipo=data['tipo'])
        db.session.add(produtos)
        db.session.commit()
        return ProdutosSchema().dump(produtos),201
    
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
        produtos.fabric = data.get('fabric', produtos.fabric)
        produtos.quant = data.get('quanti', produtos.quant)
        produtos.tipo = data.get('tipo', produtos.tipo)

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



class UsuariosResource(Resource):
    #Cadastro de Usuarios
    def post(self):
        data = request.json
        usuarios = Usuarios(nome_usuario=data['nome_usuario'], login=data['login'], senha=data['senha'])
        db.session.add(usuarios)
        db.session.commit()
        return UsuariosSchema().dump(usuarios),201
    
    #Listagem de Usuarios
    def get(self, usuarios=None):
        if usuarios is None:
            usuarios = Usuarios.query.all()
            return UsuariosSchema(many=True).dump(usuarios)
        
        usuarios = Usuarios.query.get(usuarios)
        if not usuarios:
            return {"message": "Usuarios não encontrado"}, 404
        return UsuariosSchema().dump(usuarios)
    
    #Alteração de usuarios
    def put(self, usuarios_id):
        usuario = Usuarios.query.get(usuarios_id)
        if not usuario:
            return {"message": "usuarios não encontrado"}, 404

        data = request.json
        usuario.nome_usuario = data.get('nome_usuario', usuario.nome_usuario)
        usuario.login= data.get('login', usuario.login)
        usuario.senha = data.get('senha', usuario.senha)

        db.session.commit()

        return UsuariosSchema().dump(Usuarios)
    
    #Exclusão de usuarios
    def delete(self, usuarios_id):
        usuario = Usuarios.query.get(usuarios_id)
        if not usuario:
            return {"message": "usuarios não encontrado"}, 404
        
        db.session.delete(usuario)
        db.session.commit()

        return {"message": "usuarios excluído com sucesso"}, 204
