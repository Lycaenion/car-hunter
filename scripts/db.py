import sqlite3

from sqlalchemy import (
    BigInteger, Integer, String, Float, ForeignKey, create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship, Session
)


class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""


class Advertisement(Base):
    __tablename__ = "Advertisements"
    __table_args__ = {'sqlite_autoincrement': True}

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    brand: Mapped[str] = mapped_column(String(30), default=None, nullable=True)
    model: Mapped[str] = mapped_column(String(30), default=None, nullable=True)
    automatic: Mapped[int] = mapped_column(Integer, default=None, nullable=True)
    year: Mapped[int] = mapped_column(Integer, default=None, comment='production year', nullable=True)
    kms: Mapped[int] = mapped_column(Integer, default=None, nullable=True)
    price: Mapped[float] = mapped_column(Float, default=None, nullable=True)


if __name__ == "__main__":

    SQLALCHEMY_URI = 'sqlite:///db.sqlite'
    engine = create_engine(SQLALCHEMY_URI, echo=True, echo_pool="debug")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for i, url in enumerate(["kvak.com", "wooof.con", "miau.net"]):
            advertisement = Advertisement(url=url, price=(i+1)*10000.3)
            session.add(advertisement)
        session.commit()

