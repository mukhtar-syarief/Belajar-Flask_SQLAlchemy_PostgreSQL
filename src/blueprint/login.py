from flask import Blueprint, request, render_template, redirect, session
from flask_login import login_user
from src.controller.user import user_login 
import hashlib

login_api = Blueprint("login", __name__)

@login_api.route("/login", methods=['POST', 'GET'])
def login():
    if "_user_id" in session:
        return redirect('/article')
    else:
        # LOGIN REQUEST METHOD = GET
        if request.method == 'GET':   
            return render_template('home/login_form.html')
        # LOGIN REQUEST METHOD = POST
        elif request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            user = user_login(email)
            #JIKA USER ADA
            if user:
                password = hashlib.md5(password.encode())
                hash_password = password.hexdigest()
                if user.password == hash_password:
                    login_user(user)
                    session['user_id'] = user.id
                    session['nama'] = user.nama
                    session['email'] = user.email
                    return redirect('/article')
                else:
                    error = "Password yang Anda masukkan salah..!!"
                    return render_template("home/login_form.html", error = error)
            #JIKA EMIAL ATAU PASSWORD SALAH
            else:
                error = "Email yang Anda masukkan salah..!!"
                return render_template('home/login_form.html', email = email, error = error, password = password)
        