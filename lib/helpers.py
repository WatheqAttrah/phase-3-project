from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Maker, Model

# Create a database engine for SQLite using the specified file
engine = create_engine("sqlite:///database.db")
# Create a session factory to manage interactions with the database
Session = sessionmaker(bind=engine)
# Create a session object for database operations
session = Session()


# Function to view cars in the database
def view_cars():
    # Create a new session for querying
    session = Session()
    # Query all car models from the Model table
    cars = session.query(Model).all()
    # Print message if the specified car ID is not found
    if not cars:
        print("~~~~Database Empity~~~~")
    else:
        for car in cars:
            print(
                f"id:{car.id}, model:{car.model}, year:{car.year}, engine:{car.engine}, price:{car.price}, maker id:{car.maker_id}"
            )


# Function to delete a car from the database
def delete_car():
    session = Session()
    view_cars()  # Call the view_cars function to display the list of cars
    maker_id = input("Enter car id to delete: ")
    car = session.query(Model).filter_by(id=maker_id).first()
    if not car:
        print("Car not found:")
        return
    session.delete(car)
    session.commit()
    print("Car deleted from database")


# Function to count the number of records in the Model table
def count_cars():
    session = Session()
    # Use the .query().count() method to count records in the table
    record_count = session.query(Model).count()
    session.close()  # Close the session
    print(f"Total number of cars in the Model table: {record_count}")
    pass


# Function to export car data to a CSV file
def export_as_csv():
    session = Session()
    cars = session.query(Model).all()
    session.close()  # Close the session

    with open("lib\cars.csv", "w") as gr:
        gr.write("id, model, year, engine, price, maker_id\n")
        for car in cars:
            gr.write(
                f"Car Id:{car.id}, Car Model:{car.model}, Car Year: {car.year}, Car Engine: {car.engine},Car Price: {car.price}, Car Maker: {car.maker_id}\n"
            )
        print("~~~~~~Exported Successfully!!!~~~~~~")
