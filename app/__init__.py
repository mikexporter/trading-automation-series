from flask import Flask
from .views import trading_data

app = Flask(__name__)
app.register_blueprint(trading_data)
