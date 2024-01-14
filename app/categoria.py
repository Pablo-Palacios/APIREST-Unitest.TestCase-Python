from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Se conecta a la base de datos 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/api_rest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bd = SQLAlchemy(app)
ma = Marshmallow(app)

# Crear tabla en base de datos
class Categoria(bd.Model):
    id = bd.Column(bd.Integer, primary_key = True)
    nombre = bd.Column(bd.String(100))
    trabajo = bd.Column(bd.String(100))

    def __init__(self, nombre, trabajo):
        self.nombre = nombre
        self.trabajo = trabajo
with app.app_context():
    bd.create_all()

# Esquema de categorias
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'trabajo')


# Esquema de un solo objeto
categoria_schema = CategoriaSchema()

# Esquema de todos los objetos
categorias_schema = CategoriaSchema(many=True)

# Mensaje de bienvenida
@app.route('/', methods = ['GET'])
def get():
    return jsonify({'mensaje':'Bienvenidos API REST'})

# GET all 
@app.route('/categorias', methods = ['GET'])
def get_all():
    all = Categoria.query.all()
    resul = categorias_schema.dump(all)
    return jsonify(resul)


# GET by ID
@app.route('/categoria/<id>', methods = ['GET'])
def get_id(id):
    categoria = Categoria.query.get(id)
    resul = categoria_schema.dump(categoria)

    if categoria is None:
        abort(404, "resultado null")
        
    return jsonify(resul)


# POST
@app.route('/categoria', methods = ['POST'])
def post_categorias():
    data = request.get_json(force=True)
    nom = data["nombre"]
    tra = data["trabajo"]

    new_categoria = Categoria(nom, tra)

    bd.session.add(new_categoria)
    bd.session.commit()

    return categoria_schema.jsonify(new_categoria)

# PUT 
@app.route('/categoria/<id>', methods = ['PUT'])
def update_categoria(id):
    actualizar_categoria = Categoria.query.get(id)
    data = request.get_json(force=True)

    nombre = data["nombre"]
    trabajo = data["trabajo"]

    actualizar_categoria.nombre = nombre
    actualizar_categoria.trabajo = trabajo

    bd.session.commit()

    return categoria_schema.jsonify(actualizar_categoria)



# DELETE 
@app.route('/categoria/<id>', methods = ['DELETE'])
def delete_categoria(id):
    id_cat = Categoria.query.get(id)
    bd.session.delete(id_cat)
    bd.session.commit()

    return categoria_schema.jsonify(id_cat)


if __name__ == '__main__':
    app.run(debug=True)
    