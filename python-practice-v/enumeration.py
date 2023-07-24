"""
Enum is short for enumeration, and is a data type used in programming languages to define a list of named values.
Enums are commonly used in programming to represent a set of predefined constants, such as days of the week,
colors, or other values that don't change, such as the four cardinal directions (north, south, east, west).
"""
from enum import Enum

class season(Enum):
    WINTER = 1
    SUMMER = 2
print(season.SUMMER)
result = [s for s in season]
print(result)