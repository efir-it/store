from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean, MetaData

metadata = MetaData()

rmk = Table(
    "rmk",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(100), nullable=False),
    Column('store_id', Integer, ForeignKey('store.id')),
)
