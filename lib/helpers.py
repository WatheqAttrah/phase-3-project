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
            print(
                f"id:{car.id}, model:{car.model}, year:{car.year}, engine:{car.engine}, price:{car.price}, maker id:{car.maker_id}"
            )


def delete_car():
    session = Session()
    view_cars()
    maker_id = input("Enter car id to delete: ")
    car = session.query(Model).filter_by(id=maker_id).first()
    if not car:
        print("Car not found:")
        return
    session.delete(car)
    session.commit()
    print("Car deleted from database")


def export_as_csv():
    session = Session()
    cars = session.query(Model).all()
    session.close()

    with open("lib\cars.csv", "w") as gr:
        gr.write("id, model, year, engine, price, maker_id\n")
        for car in cars:
            gr.write(
                f"{car.id},{car.model},{car.year},{car.engine},{car.price},{car.maker_id}\n"
            )
        print("Exported Successfully!!!")
