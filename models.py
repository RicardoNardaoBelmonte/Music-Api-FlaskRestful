from database import db

#criando a tabela Music com seus respectivos campos para o banco de dados
class Music(db.Model):
    id = db.Colummn(db.Integer, primary_key=True)
    artist = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)