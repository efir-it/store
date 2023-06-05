from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, Float, ForeignKey

from sqlalchemy.orm import relationship

metadata = MetaData()

type_device = Table(
    "quantity_products",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String, nullable=False)
)

