from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user





# configurando views e auth da mesma forma, configuramos usando o Blueprint() 
# significa que tem varias URLS dentro desse arquivo basicamente para separar as rotas do arquivo principal

auth = Blueprint('auth', __name__)







# rota de login do usuario, conectar uma conta
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login concluido com sucesso!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta, tente novamente!', category='error')
        else:
            flash('Esse email não existe!', category='error')
    return render_template("login.html", user=current_user)




# rota de logout do usuario, desconectar da conta
@auth.route('/logout')
@login_required
def logount():
    logout_user()
    return redirect(url_for('auth.login'))



# Rota de inscrição de novos usuarios, criar uma nova conta
@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Esse email já existe!', category='error')
        elif len(email) < 4:
            flash('O email tem que ter mais que 4 caracteres!', category='error')
        elif len(first_name) < 2:
            flash('O primeiro nome tem que ter mais que 1 caractere!', category='error')
        elif password1 != password2:
            flash('As senhas não são identicas!', category='error')
        elif len(password1) < 7:
            flash('Senhas tem que ter no mínimo 7 caracteres!', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #login_user(user, remember=True)
            login_user(new_user, remember=True)
            
            # gmail.enviar_email()
            # flash(f'Um email foi mandado para {email} por favor confirme seu email!', category='success')
            # A ideia aqui era colocar uma confirmação de email para verificar a autenticidade da conta, porém não quero arriscar quebrar o tempo limite


            return redirect(url_for('views.home'))
        

    return render_template("sign_up.html", user=current_user)

