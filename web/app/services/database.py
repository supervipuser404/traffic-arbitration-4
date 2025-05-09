from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from contextlib import asynccontextmanager

from config.settings import settings  # Импортируем объект settings

# Create async engine with connection pool
engine = create_async_engine(
    settings.DATABASE_URL,  # Используем settings.DATABASE_URL
    echo=True,  # Логирование SQL-запросов для отладки
    pool_size=5,
    max_overflow=10
)

# Create session factory with connection pool
async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


@asynccontextmanager
async def get_db():
    session = async_session_factory()
    try:
        yield session
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise e
    finally:
        await session.close()
