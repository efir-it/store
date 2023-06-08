import os
import sys
from logging.config import fileConfig

from alembic import context
from setuptools import setup, find_packages
from sqlalchemy import engine_from_config
from sqlalchemy import pool

setup(
    name='core',
    packages=find_packages(),
)

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from core.settings import Base

from core.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# from ..src.type_device.model import Base as metadata_type_device
# from src.devices.model import metadata as metadata_devices
# from ..src.drivers.model import metadata as metadata_drivers
# from src.quantity_products.model import metadata as metadata_quantity_products
# from src.rmk.model import metadata as metadata_rmk
# from src.store.model import metadata as metadata_store

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

section = config.config_ini_section
config.set_section_option(section, 'DB_HOST', DB_HOST)
config.set_section_option(section, 'DB_PASS', DB_PASS)
config.set_section_option(section, 'DB_USER', DB_USER)
config.set_section_option(section, 'DB_NAME', DB_NAME)
config.set_section_option(section, 'DB_PORT', DB_PORT)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = [metadata_type_device, metadata_devices, metadata_drivers, metadata_quantity_products, metadata_rmk,
#                    metadata_store]
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
