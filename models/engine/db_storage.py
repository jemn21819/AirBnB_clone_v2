#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.user import User
from models.city import City
from os import getenv


class DBStorage:
    """ New engine database"""
    __engine = None
    __session = None

    def __init__(self):
        """Init DBStorage class"""
        MySQL_user = getenv('HBNB_MYSQL_USER')
        MySQL_password = getenv('HBNB_MYSQL_PWD')
        MySQL_host = getenv('HBNB_MYSQL_HOST')
        MySQL_database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MySQL_user,
                                             MySQL_password,
                                             MySQL_host,
                                             MySQL_database, pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return all the objects in a dictionary"""
        dict_obj = {}
        if cls:
            for objs in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(objs.__class__.__name__, objs.id)
                dict_obj[key] = objs
        else:
            for sub_cls in Base.__subclasses__():
                for objs in self.__session.query(sub_cls).all():
                    key = "{}.{}".format(objs.__class__.__name__, objs.id)
                    dict_obj[key] = objs
        return dict_obj

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """this is to close the session"""
        self.__session.remove()

    def close(self):
        """close the session callin the remove attribute"""
        self.__session.close()
