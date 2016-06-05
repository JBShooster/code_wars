from string import *

def alphanumeric(string):
    if len(string) == 0:
        return False
    for x in string:
        if x not in ascii_letters and x not in digits:
            return False
    return True