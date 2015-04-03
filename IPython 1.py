config = 'development.ini'
from pyramid.paster import get_appsettings
settings = get_appsettings(config)
from sqlalchemy import engine_from_config
engine = engine_from_config(settings, 'sqlalchemy.')
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
from learning_journal.models import MyModel
session.query(MyModel).all()
