from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Update with your MySQL credentials (usually 'root' and your password)
DB_USER = "root"
DB_PASS = "04rotdea"  # <--- Your actual password is now here
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "hcp_crm"
# Connection string for MySQL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255)) # MySQL requires lengths for indexed strings
    topics = Column(Text)
    sentiment = Column(String(50))
    date = Column(String(50))
    materials = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)