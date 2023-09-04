from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    fabric = db.Column(db.String)
    quant = db.Column(db.Integer)
    tipo = db.Column(db.String)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    senha = db.Column(db.Integer, nullable=False)
    login = db.Column(db.String, nullable=False)
    nome_usuario = db.Column(db.String, nullable=False)

class ProdutosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produtos

    id = ma.auto_field()
    nome_produto = ma.auto_field()
    price = ma.auto_field()
    fabric = ma.auto_field()
    quant = ma.auto_field()
    tipo = ma.auto_field()

class UsuariosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios

    id = ma.auto_field()
    senha = ma.auto_field()
    login = ma.auto_field()
    nome_usuario = ma.auto_field()
