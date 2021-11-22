from datetime import datetime
import os

def only_morning(func):
    def wrapper():
        if 7 <= datetime.now().hour < 12:
            func()
        else:
            raise Exception("Not allowed at afternoon")  # Hush, the neighbors are asleep
    return wrapper


@only_morning
def say_whee():
    print("Whee!")


say_whee()
