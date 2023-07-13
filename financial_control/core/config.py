from os import getenv

from dotenv import load_dotenv

load_dotenv()

class Settings():
    # Application
    APP_NAME: str = getenv('APP_NAME')
    
    # Database
    DB_USERNAME: str = getenv('DB_USERNAME', 'user')
    DB_PASSWORD: str = getenv('DB_PASSWORD', '')
    DB_HOST: str = getenv('DB_HOST', '127.0.0.1')
    DB_PORT: str = getenv('DB_PORT', 3306)
    DB_DATABASE: str = getenv('DB_DATABASE', '')
    DATABASE_URL: str = f'mysql+aiomysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    
    # Security
    ALGORITHM = "HS256"
    SECRET_KEY: str = getenv("SECRET_KEY") # openssl rand -hex 32
    TOKEN_EXPIRE_MINUTES: int = int(getenv("TOKEN_EXPIRE_MINUTES"))
    
settings = Settings()