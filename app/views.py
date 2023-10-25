from flask import Blueprint, render_template
from models import SessionLocal, Trade

trading_data = Blueprint('trading_data', __name__)

@trading_data.route('/')
def index():
    session = SessionLocal()
    trades = session.query(Trade).all()
    session.close()
    return render_template('index.html', trades=trades)
