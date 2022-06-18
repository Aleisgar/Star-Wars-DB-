import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password= Column(Integer, unique=False, nullable=False)
    id_user = relationship('favorites', backref='user', lazy=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'),nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'),nullable=True) 
    ship_id = Column(Integer, ForeignKey('ships.id'),nullable=True)
         
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    eye_color = Column(String(30), unique=False, nullable=False)
    hair_color = Column(String(30), unique=False, nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    ships_id = Column(Integer, ForeignKey('ships.id'),nullable=False)
    favorite_character = relationship('favorites', backref='character', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    population = Column(Integer, unique=False, nullable=False)
    characters = relationship('character', backref='planet', lazy=True)
    favorite_planet = relationship('favorites', backref='planet', lazy=True)
    

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    model = Column(String(30), unique=False, nullable=False)
   
  

    # def __repr__(self):
    #     return '<User %r>' % self.username

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')