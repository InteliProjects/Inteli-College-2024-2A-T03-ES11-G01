from flask import Flask, url_for, jsonify
from flask_jwt_extended import JWTManager
from routes import auth, view
import os
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from models import User
from flask_jwt_extended import create_access_token, JWTManager

load_dotenv()

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['SECRET_KEY'] = JWT_SECRET_KEY

jwt = JWTManager(app)

oauth = OAuth(app)

oauth.register(
    name='google',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    redirect_uri='http://localhost:5001/auth/google/callback',
    client_kwargs={'scope': 'openid profile email'},
)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(view, url_prefix='/view')

@app.route('/google/login')
def google_login():
    redirect_uri = url_for('google_authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/google/callback')
def google_authorize():
    token = oauth.google.authorize_access_token()
    user_info = oauth.google.parse_id_token(token)

    # Extraia informações do usuário
    email = user_info.get('email')
    username = user_info.get('name', email)  # Use o nome ou email se o nome não estiver disponível

    # Verifique se o usuário já está registrado
    user = User.get_user_by_email(email)
    if not user:
        # Registre um novo usuário se ele ainda não existir
        User.insert_user(email, username, None, False, 132)

    # Gere um token JWT para o usuário autenticado
    access_token = create_access_token(identity=email)
    
    return jsonify(
        email=email,
        username=username,
        access_token=access_token
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)
