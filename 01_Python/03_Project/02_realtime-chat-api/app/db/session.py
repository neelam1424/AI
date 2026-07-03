from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# engine =connection manager [responsible for fatsapi -> postgresql communication]
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True
)

# this create sessions
AsyncSessionLocal = async_sessionmaker(
    bind = engine,
    class_= AsyncSession,
    expire_on_commit=False
)


# database dependency
# purpose:- to create session, yield session, close session

# Route starts
#     ↓
# get_db()
#     ↓
# Create Session
#     ↓
# yield session
#     ↓
# Route receives session


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session