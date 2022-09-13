import time
import functools
  

class ClassWithDecorator:
    def __init__(self, notes) -> None:
        self._notes = notes
         
    def doTwice(func):
        """Print the function signature and return value"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self = args[0]
            func(*args, **kwargs)
            func(*args, **kwargs)
            return 
        return wrapper

    @doTwice
    def some_event(self, event):
        print("Some event occured ", event)
        return event
    
    @property
    def notes(self):
        """
        Example of a property getter 
        """
        return self._notes
    
    @notes.setter
    def notes(self, notes):
        """
        Example of a property setter 
        """
        self._notes = notes

def main():
    print("starting")
    Z = ClassWithDecorator(["My_Notes"])
    #Call getter
    print(Z.notes)

    #Setter
    Z.notes = ["my new notes"]
    Z.some_event("E !")
        
if __name__ == "__main__":
    main()
    