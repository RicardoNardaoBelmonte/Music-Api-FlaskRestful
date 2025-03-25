from database import db

#criando a tabela Music com seus respectivos campos para o banco de dados
class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Music {self.artist} - {self.genre} - {self.year}>'