from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, Float, ForeignKey

from sqlalchemy.orm import relationship

metadata = MetaData()

quantity_products = Table(
    "quantity_products",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String, nullable=False)
)

