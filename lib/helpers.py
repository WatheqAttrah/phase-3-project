from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from models import Maker, Model

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()


def view_cars():
    session = Session()
    cars = session.query(Model).all()
    
    if not cars:
        print("database Empity")
    else:
        for car in cars:
            print(f'id:{car.id}, model:{car.model}, year:{car.year}, engine:{car.engine}, price:{car.price}, maker id:{car.maker_id}')