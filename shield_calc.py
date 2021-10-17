"""Calculates amount of wiring and shielding required for a small
weather satellite."""


def import_data(filePath = ".\input.txt"):
    """Imports and formats data from text file.

    Defaults to "input.txt" if no other path is specified.

    Line breaks are removed and each element is added to a list.
    
    """

    raw_data = open(filePath).read()
    input_data = raw_data.split("\n")

    return input_data


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


def area_calc(dimensions):
    """Calculates the total area of a cuboid when given a
    sorted list of the dimensions.
    
    """

    small_area = dimensions[0] * dimensions[1]
    mid_area = dimensions[0] * dimensions[2]
    large_area = dimensions[1] * dimensions[2]
    
    total_area = (2 * small_area) + (2 * mid_area) + (2 * large_area)
    return total_area


def shield_contingency_calc(dimensions):
    return dimensions[0] * dimensions[1]

def wire_contingency_calc(dimensions):
    return (2 * dimensions[0]) + (2 * dimensions[1])