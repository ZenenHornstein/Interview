import logging
import functools
    
def logged(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        value = func(*args, **kwargs)
        logging.debug(f"function {func.__name__} called with args {signature} returned {value}")
        return 
    return wrapper