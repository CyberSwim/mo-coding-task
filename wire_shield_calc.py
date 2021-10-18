"""Calculates amount of wiring and shielding required for a small
weather satellite."""

from os import path

# Specify the location of data here
# Leave blank to default to `input.txt`
input_file = ""


def import_data(file_name):
    """Imports and formats data from text file.

    Defaults to "input.txt" if no other path is specified.

    Line breaks are removed and each element is added to a list.
    
    """

    if path.exists(file_name):
        with open(file_name) as f:
            raw_data = f.read()
            input_data = raw_data.split("\n")
            return input_data

    # Handles blank or incorrect file path, defaults to input.txt
    else:
        print ("File not found \'" + file_name + "\', defaulting to \'input.txt\'")

        if path.exists(".\input.txt") == False:
            with open("input.txt", 'w') as f:
                print("Creating new file \'input.txt\' as file did not exist.")

        return import_data(".\input.txt")


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


def area_calc(dimensions, type):
    """Calculates the total area of a cuboid when given a
    sorted list of the dimensions.

    If `type` "shield" or "wire" is passed, total area will include
    the area of extra provisioned material.
    
    """

    total = 0

    height = dimensions[0]
    width = dimensions[1]
    length = dimensions[2]

    small_area = height * width
    mid_area = height * length
    large_area = width * length
    
    if type == "shield":
        total = (3 * small_area) + (2 * mid_area) + (2 * large_area)
    
    elif type == "wire":
        volume = height * width * length
        total = volume + (2 * height) + (2 * width)

    return total


def calculate_result(file_path):
    """Calculates the total sum of shielding and wiring needed from
    a given data set.
    
    """
    
    shield = []
    wire = []

    data = import_data(file_path)

    # Handles empty files
    if len(data[0]) < 1:
        print ("No data found in \"input.txt\"")
        return None

    for item in data:
        shield.append(area_calc(parse_numbers(item), "shield"))
        wire.append(area_calc(parse_numbers(item), "wire"))
    
    total_shield = sum(shield)
    total_wire = sum(wire)

    print ("Total shield area:\n" + str(total_shield) + "\n")
    print ("Total wire area:\n" + str(total_wire) + "\n\n")

    return total_shield, total_wire


# Execute program
calculate_result (input_file)