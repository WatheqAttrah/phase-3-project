# Import necessary libraries
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Maker, Model

if __name__ == "__main__":
    # Create a database engine and session
    engine = create_engine("sqlite:///database.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    print("~~~~~Clearing out all data~~~~~")
    # Delete all old data from the Maker and Model tables
    session.query(Maker).delete()
    session.query(Model).delete()

    # Create a Faker instance for generating fake data
    fake = Faker()

    print("~~~~~~Seeding data~~~~~~")

    maker_list = ["Toyota", "Nissan", "Ford", "Chevrolet", "Jeep", "BMW"]

    makers = []
    for i in range(6):
        maker = Maker(maker=maker_list[i])

        # add and commit individually to get IDs back
        session.add(maker)
        session.commit()

        # Store the created makers in a list
        makers.append(maker)

    models = []
    for maker in makers:
        for i in range(random.randint(1, 6)):
            model = Model(
                model=fake.name(), # Generate a fake name for the model
                year=fake.year(), # Generate a fake year for the model
                engine=random.choice((4, 6)), # Choose a random engine type (4 or 6)
                price=random.randint(15000, 40000), # Generate a random price
                maker_id=maker.id,  # Set the maker ID for the model
            )
            # Store the created models in a list
            models.append(model)

    # Use bulk_save_objects to efficiently add all models to the session and commit
    session.bulk_save_objects(models)
    session.commit()
    session.close()

    print("~~~~~~Done seeding~~~~~~")
