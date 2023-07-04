import os
from sqlalchemy import create_engine
 
user = os.getenv('DB_USERNAME', 'user')
password = os.getenv('DB_PASSWORD', '')
host = os.getenv('DB_HOST', '127.0.0.1')
port = os.getenv('DB_PORT', 3306)
database = os.getenv('DB_DATABASE', '')

DATABASE_URL = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
 
def get_connection():
    return create_engine(DATABASE_URL)