from sqlalchemy.orm import Session
import schemas
import models



def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(name=skill.name, demand_level=0)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill
