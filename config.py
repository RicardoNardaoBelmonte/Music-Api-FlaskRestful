import os 

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///music.db") #name of bdd (caminho)
    SQLALCHEMY_TRACK_MODIFICATIONS = False # disable track modifications off (rastreamente de modificações)