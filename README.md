# Car Database 

Welcome to my phase 3 project

## Prerquesits 
before running the code,ensure you have the following dependencies installed 
    - Github Repository 
        - Fork & Clone 
    - Visual Studio Code 
    - SQLite3
        - SQLite Viewer 
    - SQLAlchemy 1.4.41
        -Alembic 
    - Python 3.8.13
        - pipenv
        - pip faker
        - pip prettycli

## Installation 

- VS-Code 
    - Run the command:
        - Install Python3:  'pipenv install python3.8.13'
        - Verify python version: 'python3 --version'
        - pipenv install alembic sqlalchemy==1.4.41
        - Install Faker: pip install faker
        - Install prettycli: pip install prettycli

## Running the Script

- Enter python environmanet: 'pipenv shell'
- Enter the CLI: 'Python3 lib/cli.py

## Menu Options - cli.py

The script provides the following menu options:

 - view_cars(): View Cars| Display a list of all cars.
 - view_one_car():View one car details of a specific car by ID.
 - delete_car(): Delete a car record by it's ID.
 - count_cars(): Count the total number of cars in database.
 - count_4_cyc_cars(): Count cars with a 4-cylinder engine.
 - count_6_cyc_cars(): Count the number of cars with a 6-cylinder engine.
 - export_as_csv(): Export car data to a CSV file.
 - Exit: Quit the application.

## Error Handling - SQLAlchemyError

The script includes error handling to handle exceptions during database operations.

## Data Models  - models.py
The code defines two SQLAlchemy models:
- class Maker: Represents car makers with fields for id and maker name.
- class Model: Represents car models with fields for id, model name, year,engine type, price, and a foreign key maker_id to link to a Maker.

## Seeds Fake Database - seed.py
- Python script for database seeder that uses faker librery to 
populate a SQLite database with fake car data records for car makers
and cad modeles 
- To run the seed.py file, go to the terminal and type the following command:
    - python3 lib/seed.py

Once the code is ran the new data generated to the database


