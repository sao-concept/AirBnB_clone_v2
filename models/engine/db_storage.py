#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import datetime
from os import getenv
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """Database Engine for AirBnB project"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize method"""
        connection_string = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')
        )
        self.__engine = create_engine(connection_string, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test' and getenv('HBNB_MYSQL_USER') == 'root':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, class_name=None):
        """Returns a dictionary with all objects of the specified class"""
        if class_name:
            cls = self.classes().get(class_name)
            if cls:
                return {f"{type(obj).__name__}.{obj.id}": obj for obj in self.__session.query(cls).all()}
            else:
                print(f"Invalid class name: {class_name}")
                return {}
        else:
            all_objects = {}
            for cls in self.classes().values():
                all_objects.update({f"{type(obj).__name__}.{obj.id}": obj for obj in self.__session.query(cls).all()})
            return all_objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session if obj is not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create the current database session from the engine using a sessionmaker"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))()

    def close(self):
        """Remove the session"""
        self.__session.close()

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel

        model_classes = {cls.__name__: cls for cls in BaseModel.__subclasses__()}
        return model_classes
