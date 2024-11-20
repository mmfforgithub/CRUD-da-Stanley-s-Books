from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Editora, Livro, Pedido

bp_pedidos = Blueprint('pedidos', __name__, template_folder='templates')

@bp_pedidos.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedidos.html', dados=dados)

@bp_pedidos.route('/add')
def add():
    u = Editora.query.all()
    p = Livro.query.all()
    return render_template('pedidos_add.html', editora = u, livro = p)

@bp_pedidos.route('/save', methods=['POST'])
def save():
    editora_id = request.form.get('editora_id')
    livro_id = request.form.get('livro_id')
    data = request.form.get('data')
    if editora_id and livro_id and data:
        objeto = Pedido(editora_id, livro_id, data)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/pedidos')
    else:
        flash("I'm sorry, Dave! Dados insuficientes!")
        return redirect('/pedidos/add')