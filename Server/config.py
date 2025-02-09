from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Config:
    # MySQL database connection URL
    DATABASE_URL = "mysql+pymysql://root:*october2020@localhost/nomad_database"
    
    # Create the SQLAlchemy engine
    engine = create_engine(DATABASE_URL)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    @staticmethod
    def get_db():
        db = Config.SessionLocal()
        try:
            yield db
        finally:
            db.close()

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app