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

 - View Cars: Display a list of all cars.
 - View One Car: View details of a specific car by ID.
 - Delete Car: Delete a car record by ID.
 - Count Cars: Count the total number of cars.
 - Cars with 4-Cylinder Engine: Count cars with a 4-cylinder engine.
 - Cars with 6-Cylinder Engine: Count cars with a 6-cylinder engine.
 - Export as CSV File: Export car data to a CSV file.
 - Exit: Quit the application.

## Error Handling

The script includes error handling to handle exceptions during database operations.