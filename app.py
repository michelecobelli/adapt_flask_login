from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.user import db, User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def landing():
        return render_template('user_landing.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            full_name = request.form.get('full_name')
            email = request.form.get('email')
            password = request.form.get('password')

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return 'User already exists!'

            user = User(full_name=full_name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id
            session['first_name'] = full_name.split()[0]

            return redirect(url_for('dashboard'))

        return render_template('sign_up.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first()

            if user and user.check_password(password):
                session['user_id'] = user.id
                session['first_name'] = user.full_name.split()[0]
                return redirect(url_for('dashboard'))
            else:
                return 'Invalid credentials'

        return render_template('log_in.html')

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        user = User.query.get(session['user_id'])
        first_name = user.full_name.split()[0]
        return render_template('main_page_user.html', first_name=first_name, project_description=user.project_description or "")

    @app.route('/logout', methods=['POST'])
    def logout():
        session.clear()
        return redirect(url_for('landing'))

    @app.route('/save_project', methods=['POST'])
    def save_project():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        user = User.query.get(session['user_id'])
        new_description = request.form.get('project_description')
        user.project_description = new_description
        db.session.commit()

        return redirect(url_for('dashboard'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
