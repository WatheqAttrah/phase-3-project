from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine("sqlite:///database.db")

Base = declarative_base()


# - class Maker: Represents car makers with fields for id and maker name.
class Maker(Base):
    __tablename__ = "makers"

    id = Column(Integer(), primary_key=True)
    maker = Column(String(), unique=True, nullable=False)

    models = relationship("Model", backref=backref("models"))

    def __repr__(self):
        return f"Maker(id={self.id}, " + f"maker={self.maker})"


# - class Model: Represents car models with fields for id,
# model name, year,engine type, price, and a foreign key maker_id
# to link to a Maker.
class Model(Base):
    __tablename__ = "models"

    id = Column(Integer(), primary_key=True)
    model = Column(String(), nullable=True)
    year = Column(Integer(), nullable=True)
    engine = Column(Integer(), nullable=True)
    price = Column(
        Float(),
    )

    maker_id = Column(Integer(), ForeignKey("makers.id"))

    def __repr__(self):
        return (
            f"Model(id={self.id}, "
            + f"model={self.model}, "
            + f"year={self.year} "
            + f"engine={self.engine},"
            + f"price={self.price} "
            + f"maker_id={self.maker_id})"
        )
