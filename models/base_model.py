#!/usr/bin/python3
""" base_model """

import models
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ instantiate new base model object
            using values provided either with Kwags
            or without kwargs
        """

        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for i in kwargs:
                if i == "created_at" or i == "updated_at":
                    date = datetime.strptime(kwargs[i], time_form)
                    self.__dict__[i] = date
                else:
                    self.__dict__[i] = kwargs[i]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        models.storage.save()

    # @property
    # def email(self):
    #     return self.email

    # @property
    # def password(self):
    #     return self.password

    # @property
    # def first_name(self):
    #     return self.first_name

    # @property
    # def last_name(self):
    #     return self.last_name

    def __str__(self):

        """ __str__ """
        cname = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return ("[{}] ({}) {}".format(cname, id, dict))

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dict representation of a Rectangle"""
        # time_form = "%Y-%m-%dT%H:%M:%S.%f"
        # return {
        #     "id": self.id,
        #     "created_at": self.created_at.isoformat(),
        #     "updated_at": self.updated_at.isoformat(),
        #     "myNum": self.myNum,
        #     "name": self.name,
        #     "__class__": self.__class__.__name__
        # }
        # limitation: if myNum or name is not set, accessing
        # them in later stages will raise error
        tempDict = self.__dict__.copy()
        tempDict["created_at"] = tempDict["created_at"].isoformat()
        tempDict["updated_at"] = tempDict["updated_at"].isoformat()
        tempDict["__class__"] = self.__class__.__name__
        return tempDict
