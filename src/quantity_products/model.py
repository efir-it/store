from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, Float, ForeignKey

from sqlalchemy.orm import relationship

metadata = MetaData()

quantity_products = Table(
    "quantity_products",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('store_id', Integer, ForeignKey('store.id')),
    Column("count", Float, nullable=False)
)

