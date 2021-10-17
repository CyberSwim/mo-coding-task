"""Calculates amount of wiring and shielding required for a small
weather satellite."""

from os import path

# Specify the location of data to be read
filePath = ""


def import_data(fileName = ".\input.txt"):
    """Imports and formats data from text file.

    Defaults to "input.txt" if no other path is specified.

    Line breaks are removed and each element is added to a list.
    
    """

    if path.exists(fileName):
        with open(fileName) as f:
            raw_data = f.read()

        input_data = raw_data.split("\n")
        return input_data
    
    else:
        raise FileNotFoundError


def parse_numbers(input_string):
    """Separates each number from an input string and returns
    a sorted list.
    
    """

    separated_numbers = []
    split_string = input_string.split('x')

    for number in split_string:
        separated_numbers.append(int(number))

    separated_numbers.sort()

    return separated_numbers


def area_calc(dimensions, type = ""):
    """Calculates the total area of a cuboid when given a
    sorted list of the dimensions.

    If `type` "shield" or "wire" is passed, total area will include
    the area of extra provisioned material.
    
    """

    small_area = dimensions[0] * dimensions[1]
    mid_area = dimensions[0] * dimensions[2]
    large_area = dimensions[1] * dimensions[2]
    
    total_area = (2 * small_area) + (2 * mid_area) + (2 * large_area)

    if type == "shield":
        total_area += small_area
    
    elif type == "wire":
        total_area += (2 * dimensions[0]) + (2 * dimensions[1])

    return total_area