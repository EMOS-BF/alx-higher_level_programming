#!/user/bin/python3
"""
function that return true if the class is an instance of  specified class ; otherwise False
"""
def is_same_class(obj, a_class):

    """
    Args:
 - obj: object to look at 
 - a_class: class to verify the instance of class
    """
    return True if type(obj) is a_class else False 

