import os, sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Categorys(Base):
	__tablename__ = 'categorys'
	id = Column(Integer, primary_key=True)
	cat_name = Column(String(250), nullable=False)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
		}

class CatItems(Base):
	__tablename__ = 'cat_item'
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	categorys_id = Column(Integer, ForeignKey('categorys_id'))
	categorys = relationship(Categorys)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'description': self.description,
			'id': self.id,
		}

engine = create_engine('sqlite:///waylandDatabase.db')
Base.metadata.create_all(engine)
