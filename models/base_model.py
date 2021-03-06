#!/usr/bin/python3
'''module: base_model
creates class BaseModel which defines all common attributes/methods
for other classes
'''
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    '''class:  defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''constructor:
        sets attributes for id and created_at
        '''
        t = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            self.__dict__ = kwargs
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                    kwargs.get("created_at"), t)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs.get("updated_at"), t)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        ''' public method:
        updates current datetime
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        ''' public method:
        returns dictionary containing all key/values
        '''
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = str(self.created_at.isoformat())
        if "updated_at" in copy_dict:
            copy_dict["updated_at"] = str(self.updated_at.isoformat())

        return (copy_dict)

    def __str__(self):
        '''print result
        '''
        return ('[{0}] ({1}) {2}'.format(
            self.__class__.__name__, self.id, self.__dict__))
