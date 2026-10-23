from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/training_db"
DATABASE_URL = "postgresql+psycopg2://st_db_3fzo_user:Mj7smphUjNB93JEv0L130IRZ0Hs35fuZ@dpg-dbdm6c8n74is73996ev0-a.ohio-postgres.render.com/st_db_3fzo"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()