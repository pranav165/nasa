# Utility functions

def check_in_range(value, min, max):
    """
    :param value: Value to be checked
    :param min: Minimum range
    :param max: Maximum range
    :return: Boolean
    """
    if isinstance(value, str):
        value = float(value)
    if min <= value <= max and round(value, 2) == value:
        return True
    return False
