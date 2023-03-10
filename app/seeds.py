from models import User
from db import Session, Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

db.add_all([
    User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
    User(username='jwilloughway1',
         email='rmebes1@sogou.com', password='password123'),
    User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
    User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit()

db.close()