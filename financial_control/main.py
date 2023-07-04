import uvicorn
import sqlalchemy as db
from fastapi import FastAPI

from financial_control.routers import route
from financial_control.database.config import get_connection

app = FastAPI()

app.include_router(route.api)
app.include_router(route.web)

try:
    engine = get_connection()
    conn = engine.connect()
    print(f"Connection to the for user created successfully.")
    metadata = db.MetaData()
    
    users = db.Table('users', metadata, autoload_with=engine)
    query = db.select(users).where(users.columns.id == 2)
    
    print(query)
    result = conn.execute(query)
    print(result.fetchall())   
except Exception as ex:
    print("Connection could not be made due to the follDowing error: \n", ex)

if __name__ == '__main__':
    uvicorn.run(app)