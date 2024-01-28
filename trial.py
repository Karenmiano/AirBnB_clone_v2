from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import environ
from models.state import State

env = environ.get('HBNB_ENV')
user = environ.get('HBNB_MYSQL_USER')
passwd = environ.get('HBNB_MYSQL_PWD')
host = environ.get('HBNB_MYSQL_HOST')
db = environ.get('HBNB_MYSQL_DB')
store = environ.get('HBNB_TYPE_STORAGE')       

url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(user, passwd, host, db)
engine = create_engine(url, pool_pre_ping=True)

Session = sessionmaker(bind=engine, expire_on_commit=False)
session = Session()
new_state = State(name = "Washington")

session.add(new_state)
session.close()

state = session.query(State).filter(State.name == "Washington").first()

print(state.name)
