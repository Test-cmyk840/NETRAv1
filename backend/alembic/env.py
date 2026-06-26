from logging.config import fileConfig

from alembic import context

from sqlalchemy import pool

from sqlalchemy.ext.asyncio import async_engine_from_config

from app.core.config import settings

from app.db.base import Base

config = context.config

config.set_main_option(
    "sqlalchemy.url",
    settings.database_url,
)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
