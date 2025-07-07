from curses import meta
from enum import auto, unique
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, ForeignKey, MetaData, Table, Column, Integer, String, Float
# from sqlalchemy.orm import Session

load_dotenv()

DEV_MODE = os.getenv("DEV_MODE", "False").lower() in ("true", "1", "t")
DEV_DB_URL = os.getenv("DEV_DB_URL", "postgresql://root:root@localhost:5432/spps_db")
PRODUCTION_DB_URL = os.getenv("PRODUCTION_DB_URL", "postgres://neon_db:root@localhost:5432/neon_db")

_db = None

try:
    _db = create_engine("" + (DEV_DB_URL if DEV_MODE else PRODUCTION_DB_URL))
except Exception as e:
    print(f"Error connecting to the database: {e}")
    _db = None

metadata = MetaData()

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("email", String),
    Column("gender", String),
    Column("date_of_birth", String),
    Column("user_id", String, unique=True),
    Column("password", String, default="1234567"),
    Column("department", String),
    Column("role", String),
    # autoload_with=_db,
)

Courses = Table(
    "courses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("course_code", String, unique=True),
    Column("course_title", String),
    Column("lecturer_id", String, ForeignKey("users.user_id")),
    # autoload_with=_db,
)

Student_Offered_Courses = Table(
    "student_offered_courses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", String, ForeignKey("users.user_id")),
    Column("course_id", String, ForeignKey("courses.course_code")),
    Column("semester", String),
    Column("session", String),
    # autoload_with=_db,
)

Student_Grade = Table(
    "student_grade",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", String, ForeignKey("users.user_id")),
    Column("lecturer_id", String, ForeignKey("users.user_id")),
    Column("course_code", String, ForeignKey("courses.course_code")),
    Column("semester", String),
    Column("session", String),
    Column("course_unit", Integer),
    Column("ca_score", Integer),
    Column("exam_score", Integer),
    Column("total_score", Integer),
    Column("letter_grade", String),
    Column("weight", Float)
    # autoload_with=_db,
)

# Student_Gpa = Table(
#     "student_gpa",
#     metadata,
#     Column("student_id", String, ForeignKey("users.user_id")),
#     Column("semester", String),
#     Column("session", String),
#     Column("gpa", Float),
#     # autoload_with=_db,
# )

metadata.create_all(_db)

async def execute(query: str, params):
    if _db is None:
        raise Exception("Database connection not established.")
    with _db.connect() as conn:
        return conn.execute(query, (params if not params else {}))
