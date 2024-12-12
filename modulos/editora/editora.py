from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Editora

bp_editora = Blueprint('editora', __name__, template_folder='templates')

@bp_editora.route('/')
def index():
    e = Editora.query.all()
    return render_template('editora.html', dados=e)

@bp_editora.route('/add')
def add():
    return render_template('editora_add.html')

@bp_editora.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    fundacao = request.form.get('fundacao')
    if nome and fundacao:
        objeto = Editora(nome, fundacao)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/editora')
    else:
        flash('Preencha todos os campos!')
        return redirect('/editora/add')

@bp_editora.route("/remove/<int:id>")
def remove(id):
    e = Editora.query.get(id)
    try:
        db.session.delete(e)
        db.session.commit()
        flash("Editora removida!")
    except:
        flash("Editora Inválida!")
    return redirect("/editora")


@bp_editora.route("/edit/<int:id>")
def edit(id):
    e = Editora.query.get(id)
    return render_template("editora_edit.html", dados=e)


@bp_editora.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    fundacao = request.form.get("fundacao")
    id = request.form.get("id")
    if nome and fundacao and id:
        e = Editora.query.get(id)
        e.nome = nome
        e.fundacao = fundacao
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/editora")
