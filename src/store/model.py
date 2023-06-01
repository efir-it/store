from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, ForeignKey

from sqlalchemy.orm import relationship


metadata = MetaData()

store = Table(
    "store",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(200), nullable=False),
    Column("address", String(500)),
    Column("separated", Boolean),
    Column("hide", Boolean)
)

