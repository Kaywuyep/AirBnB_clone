#!/usr/bin/python3
"""a base model for my web application"""
import uuid
from datetime import datetime
import models
# from models.__init__ import storage


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialization
        Args:
            *args: Not used
            **kwargs: Key-value pairs of attributes and their values
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    # using the isoformat()
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            # If kwargs is empty, create id and created_at
            self.id = str(uuid.uuid4())  # uuid - Universally Unique Identifier
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # Add the instance to storage

    @classmethod
    def all(cls):
        """an all clas method"""
        return cls.instances

    @classmethod
    def get_count(cls):
        """ retrieve number of instances in a class"""
        return cls.count

    def __str__(self):
        """
        Return an unofficial  user friendly representation
        of the isinstance in other words, a brief description of our model
        """
        return "[{}] ({}) {}"\
            .format(self.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime. simply put; whenever a change is made
        update the time it happened
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values of
         __dict__ of the instance
         or say the details of what the model should look like,
         its attributes like ID, creation time, and update time, then
         write the class name(the type of model)
         isoformat() basically gives you a string representation of the
         datetime object in the ISO 8601 format which is a
         standardized way of expressing time, especially if you're dealing
         with data exchange or serialization where a consistent fmt is crucial
        """
        Dict = self.__dict__.copy()
        Dict['__class__'] = self.__name__
        Dict['created_at'] = self.created_at.isoformat()
        Dict['updated_at'] = self.updated_at.isoformat()
        return Dict
