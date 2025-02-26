#Command Design Pattern - used to turn a request into an object that contains all information about the request
#- allows the sender to pass requests as method arguments, or queue a request’s execution, and support undoable operations
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass