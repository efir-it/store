# from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, ForeignKey
#
# from sqlalchemy.orm import relationship
#
#
# metadata = MetaData()
#
# store = Table(
#     "store",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column("name", String(200), nullable=False),
#     Column("address", String(500)),
#     Column("separated", Boolean),
#     Column("hide", Boolean)
# )
#

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    rmk = relationship('Rmk', back_populates='store', backref="rmk")
