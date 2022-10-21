from flask import Blueprint, render_template
from flask_login import login_required, current_user
# aqui eu vou guardar as rotas para o servidor
# acabei não usando essa parte mas aqui seria onde eu colocaria mais rotas 
views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)
