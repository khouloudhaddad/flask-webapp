from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if len(email) > 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 3 characters.', category='error')
        elif password != confirm_password:
            flash('Passords dont\' match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Add user to database
            flash('User account successfully created.', category='success')

    return render_template("sign_up.html")