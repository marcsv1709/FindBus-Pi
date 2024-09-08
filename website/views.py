from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template("home.html")

@views.route('/rotas', methods=['GET', 'POST'])
@login_required
def rotas():
    return render_template("rotas.html", user=current_user)

@views.route('/horarios', methods=['GET', 'POST'])
@login_required
def horarios():
    return render_template("horarios.html", user=current_user)

@views.route('/perfil', methods=['GET'])
@login_required
def visualizar_perfil():
    return render_template('perfil.html', user=current_user)

@views.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        
        if len(email) < 4:
            flash('Email inválido.', category='error')
        elif len(user_name) < 2:
            flash('Nome muito curto.', category='error')
        else:
            current_user.email = email
            current_user.user_name = user_name
            db.session.commit()
            flash('Perfil atualizado!', category='success')
            return redirect(url_for('views.visualizar_perfil'))

    return render_template('editar_perfil.html', user=current_user)

@views.route('/perfil/deletar', methods=['POST'])
@login_required
def deletar_perfil():
    user = User.query.get(current_user.id)
    db.session.delete(user)
    db.session.commit()
    flash('Conta excluída com sucesso.', category='success')
    return redirect(url_for('auth.logout'))
