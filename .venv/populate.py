from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Resource_shutdowns, Base

engine = create_engine('sqlite:///shutdowns.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#first_entry = Resource_shutdowns(recording_date='2025-04-20', adress='Ноавая, д. 20', type_of_resource='Электроснабжение', shutdown_date='2025-04-21', renewal_date='2025-04-22')
#session.add(first_entry)
#session.commit()

