class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Full(Exception):
    """Error attempting to push elements when the container reached max cap."""
    pass
