from flask import Blueprint, request, render_template, redirect, session
from flask_login import current_user, login_user
from src.controller.user import user_login 

login_api = Blueprint("login", __name__)

@login_api.route("/login", methods=['POST', 'GET'])
def login():
    if "_user_id" in session:
        return redirect('/article')
    else:
        # LOGIN REQUEST METHOD = POST
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            user = user_login(email,password)
            #JIKA USER ADA
            if user:
                login_user(user)
                session['user_id'] = user.id
                session['nama'] = user.nama
                session['email'] = user.email
                return redirect('/article')
            #JIKA EMIAL ATAU PASSWORD SALAH
            else:
                error = "Email atau Password yang Anda masukkan salah..!!"
                return render_template('home/login_form.html', email = email, error = error, password = password)
        # LOGIN REQUEST METHOD = GET
        else:   
            return render_template('home/login_form.html')