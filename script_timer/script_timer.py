from time import time 
import os 

def _convertTime(start:float, end:float) -> str:
    """
    Converts delta time to hours, minutes, or seconds.

    Args:
        start (float): start time
        end(float): end time

    Returns:
        delta_time (str)
    """

    delta_time = end-start 

    # convert to hours
    if delta_time // 3600 > 0:
        delta_time = delta_time/3600
        delta_time = "{:.3f} Hours".format(delta_time) 
    # convert to minutes
    elif delta_time // 60 > 0:
        delta_time = delta_time/60
        delta_time = "{:.3f} Minutes".format(delta_time)
    # keep seconds
    else: 
        delta_time = "{:.3f} Seconds".format(delta_time)

    return delta_time


def timer(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        delta_time = _convertTime(start, end)
        print('{} executed in {}.'.format(f.__name__, delta_time))
        return result
    return wrapper


class scriptTime:

    def __init__(self, file):
        self.start = time()
        self.file = os.path.basename(file)

    def end(self):
        end = time()
        delta_time = _convertTime(self.start, end)
        print(f"{self.file} executed in {delta_time}.")
        return None