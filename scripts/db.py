import sqlite3

from sqlalchemy import (
    BigInteger, Integer, String, Float, ForeignKey, create_engine, Date, select, delete,
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship, Session
)
import datetime


class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""


class Advertisements(Base):
    __tablename__ = "Advertisements"
    __table_args__ = {'sqlite_autoincrement': True}

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    brand: Mapped[str] = mapped_column(String(30), default=None, nullable=True)
    model: Mapped[str] = mapped_column(String(30), default=None, nullable=True)
    automatic: Mapped[int] = mapped_column(Integer, default=None, nullable=True)
    year: Mapped[int] = mapped_column(Integer, default=None, comment='production year', nullable=True)
    kms: Mapped[int] = mapped_column(Integer, default=None, comment='date added to bazos', nullable=True)
    date: Mapped[Date] = mapped_column(Date, default=None, nullable=False)
    price: Mapped[float] = mapped_column(Float, default=None, nullable=True)

SQLALCHEMY_URI = 'sqlite:///db.sqlite'
engine = create_engine(SQLALCHEMY_URI, echo=True, echo_pool="debug")
Base.metadata.create_all(engine)



def add_ad_to_db(url, price):
    with Session(engine) as session:
        advertisement = Advertisements(url, price=price, date=datetime.date.today())
        session.add(advertisement)
        session.commit()
        print("added")


def is_ad_in_db(url):
    with Session(engine) as session:
        stmt = select(Advertisements).where(Advertisements.url == url)
        result = session.execute(stmt).scalar()

        if result is None:
            print(False)
            return False
        else:
            print(True)
            return True


# if __name__ == '__main__':
#     SQLALCHEMY_URI = 'sqlite:///db.sqlite'
#     engine = create_engine(SQLALCHEMY_URI, echo=True, echo_pool="debug")
#     Base.metadata.create_all(engine)