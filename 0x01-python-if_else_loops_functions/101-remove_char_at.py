#!/usr/bin/python3
def remove_char_at(str, n):
    """This function creates a copy of the string, deletes
    a position of the passed string and returns a string
    without the deleted position."""
    new_str = ""

    for i in range(len(str)):
        if i != n:
            new_str += str[i]

    return new_str
