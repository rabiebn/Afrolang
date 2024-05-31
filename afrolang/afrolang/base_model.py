"""
This Model defines BaseModel class:
a blueprint for all classes
"""
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """BaseModel class"""

    def __init__(self) -> None:
        """Initialization of base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """String representation"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)
    
    def update(self):
        """
        Updates the object and set its update_at with the current datetime.
        """
        pass

    def delete(self):
        """
        Deletes an object
        """
        pass


