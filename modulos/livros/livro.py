from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Livro, Editora

bp_livro = Blueprint('livro', __name__, template_folder='templates')

@bp_livro.route('/')
def index():
    dados = Livro.query.all()
    return render_template('livro.html', dados=dados)

@bp_livro.route('/add')
def add():
    e = Editora.query.all()
    return render_template('livro_add.html', editora = e)

@bp_livro.route('/save', methods=['POST'])
def save():
    editora_id = request.form.get('editora_id')
    titulo = request.form.get('titulo')
    genero = request.form.get('genero')
    if editora_id and titulo and genero:
        objeto = Livro(editora_id, titulo, genero)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/livro')
    else:
        flash('Preencha todos os campos!')
        return redirect('/livro/add')