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

## Menu Options

The script provides the following menu options:

 - view_cars(): View Cars| Display a list of all cars.
 - view_one_car():View one car details of a specific car by ID.
 - delete_car(): Delete a car record by it's ID.
 - count_cars(): Count the total number of cars in database.
 - count_4_cyc_cars(): Count cars with a 4-cylinder engine.
 - count_6_cyc_cars(): Count the number of cars with a 6-cylinder engine.
 - export_as_csv(): Export car data to a CSV file.
 - Exit: Quit the application.

## Error Handling

The script includes error handling to handle exceptions during database operations.

## Data Models
The code defines two SQLAlchemy models:
- Maker: Represents car makers with fields for id and maker name.
- Model: Represents car models with fields for id, model name, year,      engine type, price, and a foreign key maker_id to link to a Maker.
