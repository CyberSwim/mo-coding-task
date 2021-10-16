# import the input file as a list
# separate the width/length/depth
# convert to int
# sort smallest -> largest
# add to new list

# calculate 2 * area of each
# add together
# calculate contingency for shielding and add to p1 answer
# calculate contingency for wires and add to p2 answer

def import_data(filePath):
    raw_data = open(filePath).read()
    input_data = raw_data.split("\n")

    return input_data

def parse_numbers(input_string):
    separated_numbers = []
    split_string = input_string.split('x')

    for number in split_string:
        separated_numbers.append(int(number))

    separated_numbers.sort()

    return separated_numbers

def area_calc(dimensions):
    
    return

def shield_contingency_calc(dimensions):
    return

def wire_contingency_calc(dimensions):
    return