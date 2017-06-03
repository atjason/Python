from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'

  id = Column(String(2), primary_key=True)
  name = Column(String(20))

engine = create_engine("sqlite:///tmp.db")
DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(id='2', name='Michael')
session.add(new_user)

user = session.query(User).filter(User.id=='2').one()
print 'id: ', user.id
print 'name: ', user.name

session.commit()
session.close()

