# from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, ForeignKey
#
# from sqlalchemy.orm import relationship
#
# metadata = MetaData()
#
# devices = Table(
#     "devices",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column("name", String(200), nullable=False),
#     Column('rmk_id', Integer, ForeignKey('rmk.id')),
#     Column('type_device_id', Integer, ForeignKey('type_device.id'), unique=True),
#     Column("hide", Boolean),
# )
#


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from ..drivers.model import drivers_devices
from ..database import Base
# Base = declarative_base()


class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    hide = Column(Boolean)

    drivers = relationship('drivers',
                           backref='devices',
                           secondary=drivers_devices,
                           # back_populates="devices"
                           )

    rmk_id = Column(Integer, ForeignKey('rmk.id'))

    type_device_id = Column(Integer, ForeignKey('type_device.id'))
