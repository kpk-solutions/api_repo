from pydantic import BaseModel

class SkillBase(BaseModel):
    name: str

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    demand_level: int

    class Config:
        orm_mode = True
