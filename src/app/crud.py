from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(id=user.id, email=user.email, first_name=user.first_name, last_name=user.last_name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user