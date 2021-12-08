from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///./tutorial.db"
# engine = create_engine(     
#   SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
# )
engine = create_engine("postgresql://postgres:postgres@localhost/teste2")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()