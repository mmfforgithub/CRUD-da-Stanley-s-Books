from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdt435t4654756h3q3464756y'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/bibliofilo'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Editora, Livro, Pedido
from modulos.editora.editora import bp_editora
from modulos.livros.livro import bp_livro
from modulos.pedidos.pedidos import bp_pedidos
app.register_blueprint(bp_editora, url_prefix='/editora')
app.register_blueprint(bp_livro, url_prefix='/livro')
app.register_blueprint(bp_pedidos, url_prefix='/pedidos')
@app.route('/')
def index():
    return render_template('ola.html')