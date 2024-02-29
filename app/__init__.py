from flask import Flask
from flask_mail import Mail
from .config import Config 
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)


app.config.from_object(Config)
# app.secret_key = "vbdfvdfvadsdd"
app.config['MAIL_PORT'] = 2525
csrf = CSRFProtect(app)

mail = Mail(app)

from app import views


