#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, query, scoped_session


class DBStorage():
    __engine = None
    __session = None
    classes_list = (User, State, City, Amenity, Place, Review)

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "this method must return a dictionary with requested info"
        objects = []
        if cls is None:
            for class_name in self.classes_list:
                for obj in self.__session.query(class_name).all():
                    values[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            objects = self.__session.query(cls).all()
        obj_dict = {}
        for obj in objects:
            key = f"{type(obj).__name__}.{obj.id}"
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def save(self):
        """saves changes to session"""
        self.__session.commit()

    def close(self):
        self.__session.close()
