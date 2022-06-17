from flask import Blueprint, render_template, redirect, request, session
from flask_login import current_user, login_user
from src.controller.user import find_user_by_email, create_user

signup_api = Blueprint("signup", __name__)

@signup_api.route("/signup", methods = ["POST", "GET"])
def signup():
    if "_user_id" in session:
        return redirect('/article')
    else:
        if request.method == "POST":
            nama = request.form.get("nama")
            email = request.form.get("email")
            password = request.form.get("password")
            if nama == "" or email == "" or password == "":
                error = "Nama, E-mail, atau Password TIDAK BOLEH KOSONG.!"
                return render_template('home/signup.html', error = error)
            else:
                user = find_user_by_email(email)
                if user:
                    error = "Email telah digunakan..!!"
                    return render_template('home/signup.html', error = error)
                else:
                    create_user(nama, email, password)
                    user = find_user_by_email(email)
                    login_user(user)
                    session['user_id'] = user.id
                    session['nama'] = user.nama
                    session['email'] = user.email
                    return redirect('/')
        return render_template('home/signup.html')