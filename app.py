from flask import Flask,request,jsonify
from flask_restful import Api
from models import db, ma
from resources import UsuariosResource, ProdutosResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api = Api(app)
db.init_app(app)
ma.init_app(app)


api.add_resource(ProdutosResource, '/cadastrar_produtos', '/cadastrar_produtos/<int:produtos_id>')
api.add_resource(UsuariosResource, '/cadastrar_usuarios', '/cadastrar_usuarios/<int:usuarios_id>')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)