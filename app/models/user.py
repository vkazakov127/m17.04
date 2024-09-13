# -*- coding: utf-8 -*-
# /app/models/user.py
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates='users')


# Для самопроверки
from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
