from database import db

class Editora(db.Model):
    __tablename__ = 'editora'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    fundacao = db.Column(db.Integer)

    def __init__(self, nome, fundacao):
        self.nome = nome
        self.fundacao = fundacao

    def __repr__(self):
        return '<Editora {}>'.format(self.nome)



class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key = True)
    editora_id = db.Column(db.Integer, db.ForeignKey('editora.id'))
    titulo = db.Column(db.String(100))
    genero = db.Column(db.String(50))   

    editora = db.relationship('Editora', foreign_keys = editora_id)

    def __init__(self, editora_id, titulo, genero):
        self.editora_id = editora_id
        self.titulo = titulo
        self.genero = genero

    def __repr__(self):
        return '<Livro {}>'.format(self.titulo)

    
