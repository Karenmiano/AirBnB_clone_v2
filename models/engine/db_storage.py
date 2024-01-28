#!/usr/bin/python3
"""Only one class DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import environ
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Defines database storage for the project"""
    __engine = None
    __session = None
    classes = [BaseModel, Amenity, City, Place, Review, State, User]

    def __init__(self):
        """Creates connection to the database"""
        env = environ.get('HBNB_ENV')
        user = environ.get('HBNB_MYSQL_USER')
        passwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        store = environ.get('HBNB_TYPE_STORAGE')

        url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(user, passwd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieves records from table or tables if cls is None"""
        objs = {}
        if cls:
            required = self.__session.query(cls)
            for obj in required:
                objs.update({f'{obj.__class__.__name__}.{obj.id}': obj})
        else:
            for cls in classes[1:]:
                required = self.__session.query(cls)
                for obj in required:
                    objs.update({f'{obj.__class__.__name__}.{obj.id}': obj})
        return objs

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def close(self):
        """Removes scoped session"""
        self.__session.close()

    def delete(self, obj=None):
        """Mark object for deletion in next commit"""
        if obj:
            self.__session.delete(obj)

    def save(self):
        """Commit all changes to current db session"""
        self.__session.commit()

    def reload(self):
        """Reloads state and creates a session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
