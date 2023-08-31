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
                model=fake.name(),
                year=fake.year(),
                engine=random.choice((4, 6)),
                price=random.randint(15000, 40000),
                maker_id=maker.id,
            )

            models.append(model)

    session.bulk_save_objects(models)
    session.commit()
    session.close()

    print("~~~~~~Done seeding~~~~~~")
