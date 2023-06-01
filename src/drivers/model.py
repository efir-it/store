from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, ForeignKey

from sqlalchemy.orm import relationship

metadata = MetaData()

drivers = Table(
    "drivers",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(200), nullable=False),
    Column("position_save", String(200)),
    Column('type_device_id', Integer, ForeignKey('type_device.id')),
    Column("model_device", String(200))
)

