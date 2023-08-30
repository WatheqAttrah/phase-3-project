
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Maker, Model

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Clearing old data")
    session.query(Maker).delete()
    session.query(Model).delete()

    fake = Faker()

    print("Seeding data")

    maker_list = ["Toyota", 
                     "Nissan", 
                     "Ford",
                     "Chevrolet",
                     "Jeep"
                     ]

    makers = []
    for i in range(5):
        maker = Maker(maker=maker_list[i])

        # add and commit individually to get IDs back
        session.add(maker)
        session.commit()

        makers.append(maker)

    models = []
    for maker in makers:
        for i in range(random.randint(1,5)):
            model = Model(
		        model=fake.name(),
                year = fake.year(),
                engine = random.choice((4, 6)),
		        price=random.randint(15000, 40000),
                maker_id=maker.id
            )

            models.append(model)
    
    session.bulk_save_objects(models)
    session.commit()
    session.close()

    print("Done seeding")