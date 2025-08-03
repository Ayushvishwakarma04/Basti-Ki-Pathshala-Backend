from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from database.database import get_session, create_db_and_tables
from models.models import User, UserCreate

app = FastAPI(title="Basti Ki Pathshala Foundation")

@app.on_event("startup")
def on_startup():
    #run db when app runs
    create_db_and_tables()

@app.post("/register", response_model=User)
def register_user(
    user_create: UserCreate,
    session: Session = Depends(get_session)
):
    # To Register new user
    existing_user = session.exec(select(User).where(User.email == user_create.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists."
        )
    db_user = User.from_orm(user_create)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get("/users", response_model=List[User])
def get_all_users(
    session: Session = Depends(get_session)
):
    # Endpoint is public but if ask we can fix it using secret key with jwt
    users = session.exec(select(User)).all()
    return users
