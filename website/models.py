from xmlrpc.client import Boolean
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    # confirmed = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    
# modelos para que uma conta seja salva na base de dados 
# dessa forma vai ser passado para a base de dados  as informações das contas cadastradas