import time
import functools
import logging
import argparse
  

class ClassWithDecorator:
    def __init__(self, notes) -> None:
        self._notes = notes
         
    def doTwice(func):
        """Print the function signature and return value"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self = args[0]
            args_repr = [repr(a) for a in args[1:]]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            logging.debug(f"function {func.__name__} called with args {signature}")
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
    parser = argparse.ArgumentParser(prog='logging.py')
    parser.add_argument('-log',
                     '--loglevel',
                     default='warning',
                     choices=['debug', 'info', 'warning'],
                     help='Provide logging level. Example --loglevel debug, default=warning')

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper())
    logging.info( 'Logging now setup.' )
    main()