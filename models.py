from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    price = Column(Float)
    quantity = Column(Float)
    time = Column(Integer)

def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)

def add_trade(session, trade_data):
    """Add a new trade to the database."""
    trade = Trade(
        symbol=trade_data["symbol"],
        price=trade_data["price"],
        quantity=trade_data["quantity"],
        time=trade_data["time"]
    )
    session.add(trade)
    session.commit()

def get_all_trades(session):
    """Fetch all trades from the database."""
    return session.query(Trade).all()


DATABASE_URL = "sqlite:///trades.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)