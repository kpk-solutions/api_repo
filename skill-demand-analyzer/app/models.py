from sqlalchemy import Column, Integer, String
from database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    demand_level = Column(Integer)
