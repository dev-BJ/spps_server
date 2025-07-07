from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

load_dotenv()

DEV_MODE = os.getenv("DEV_MODE", "False").lower() in ("true", "1", "t") 
print(f"DEV_MODE: {DEV_MODE}")

db = None

try:
    db = create_engine("postgresql://root:root@localhost:5432/spps_db")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    db = None

