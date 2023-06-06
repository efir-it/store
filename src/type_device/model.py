# from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, Float, ForeignKey
#
# from sqlalchemy.orm import relationship
#
# metadata = MetaData()
#
# type_device = Table(
#     "quantity_products",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column("name", String, nullable=False)
# )
#


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TypeDevice(Base):
    __tablename__ = 'type_device'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)

    device = relationship("Device", back_populates="type_device", uselist=False)
