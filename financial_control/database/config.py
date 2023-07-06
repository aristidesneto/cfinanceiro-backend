from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
 
user = getenv('DB_USERNAME', 'user')
password = getenv('DB_PASSWORD', '')
host = getenv('DB_HOST', '127.0.0.1')
port = getenv('DB_PORT', 3306)
database = getenv('DB_DATABASE', '')

DATABASE_URL = f'mysql+aiomysql://{user}:{password}@{host}:{port}/{database}'

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)