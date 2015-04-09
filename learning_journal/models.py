from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    DateTime
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )
from datetime import datetime

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(length=255), nullable=False)
    body = Column(Text, nullable = True)
    created = Column(DateTime, default=datetime.utcnow())
    edited = Column(DateTime, default=datetime.utcnow())

    @classmethod
    def all(cls):
        return session.query(cls).filter().order_by()


    @classmethod
    def by_id(cls, entryid):
        return session.query(cls).filter(cls.id==entryid).last()

Index('my_index', Entry.title, unique=True, mysql_length=255)
