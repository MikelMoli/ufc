from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Events(Base):
    """UFC Event"""

    __tablename__ = 'events'

    id_event = A seguir mañana
