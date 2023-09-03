from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Maker, Model
from sqlalchemy.exc import SQLAlchemyError
from prettycli import green, yellow, red, blue

# Create a database engine for SQLite using the specified file
engine = create_engine("sqlite:///database.db")
# Create a session factory to manage interactions with the database
Session = sessionmaker(bind=engine)
# Create a session object for database operations
session = Session()


# 1. Function to view cars in the database
def view_cars():
    try:
        # Create a new session for querying
        session = Session()
        # Query all car models from the Model table
        cars = session.query(Model).all()
        # Print message if the specified car ID is not found
        if not cars:
            print("~~~~Database Empty~~~~")
        else:
            for car in cars:
                print(
                    f" Car Id:{car.id}, Car Model:{car.model}, Car Year:{car.year}, engine:{car.engine}, price:{car.price}, maker id:{car.maker_id}"
                )

    except SQLAlchemyError as e:
        print(red(f"An error occurred: {str(e)}"))


# 2 Function Veiw one car
def view_one_car():
    try:
        session = Session()
        view_cars()
        maker_id = input(yellow("Enter car id to view: "))
        car = session.query(Model).filter_by(id=maker_id).first()
        if not car:
            print(red("Invalid car id"))
        else:
            # Print individual car details
            print(green("Car Details:"))
            print(f"*) Car ID: {car.id}")
            print(f"*) Car Model: {car.model}")
            print(f"*) Car Year: {car.year}")
            print(f"*) Cae Engine: {car.engine}")
            print(f"*) Price $ {car.price}")
    except SQLAlchemyError as e:
        print(red(f"An error occurred: {str(e)}"))


# 3. Function to delete a car from the database
def delete_car():
    try:
        session = Session()
        view_cars()  # Call the view_cars function to display the list of cars

        maker_id = input(yellow("Enter car id to delete: "))
        car = session.query(Model).filter_by(id=maker_id).first()
        if not car:
            print("Car not found:")
            return
        session.delete(car)
        session.commit()
        print(red("Car deleted from database"))
    except SQLAlchemyError as e:
        print(red(f"An error occurred: {str(e)}"))


# 4. Function to count the number of records in the Model table
def count_cars():
    try:
        session = Session()
        # Use the .query().count() method to count records in the table
        record_count = session.query(Model).count()
        session.close()  # Close the session
        print(f"Total number of cars in the Model table: {record_count}")
    except SQLAlchemyError as e:
        print(red(f"An error occurred: {str(e)}"))


# 5. Function count number of cars with 4 Cyclender engine
def count_4_cyc_cars():
    try:
        session = Session()
        cars_4_cylender = session.query(Model).filter(Model.engine == 4).all()
        count_4 = len(cars_4_cylender)
        session.close()
        print(f"Total number of cars with 4 cyclender engine: {count_4}")
    except SQLAlchemyError as e:
        print(red(f"An error occurred: {str(e)}"))


# 6. Function count number of cars with 6 Cyclender engine
def count_6_cyc_cars():
    try:
        session = Session()
        cars_6_cylender = session.query(Model).filter(Model.engine == 6).all()
        count_6 = len(cars_6_cylender)
        session.close()
        print(f"Total number of cars with 6 cyclender engine: {count_6}")
    except SQLAlchemyError as e:
        print(red(f"An error occurred: {str(e)}"))


# 7. Function to export car data to a CSV file
def export_as_csv():
    try:
        session = Session()
        cars = session.query(Model).all()
        session.close()  # Close the session

        with open("cars.csv", "w") as gr:
            gr.write("id, model, year, engine, price, maker_id\n")
            for car in cars:
                gr.write(
                    f"Car Id:{car.id}, Car Model:{car.model}, Car Year: {car.year}, Car Engine: {car.engine},Car Price: {car.price}, Car Maker: {car.maker_id}\n"
                )
            print("~~~~~~Exported Successfully!!!~~~~~~")
    except SQLAlchemyError as e:
        print(red(f"An error occurred: {str(e)}"))
