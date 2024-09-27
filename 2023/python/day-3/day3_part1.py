import pprint
import re
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

symbol_coordinates = defaultdict(list)
number_coordinates = []
solution = 0

with open("input.txt") as input_file:
    for line_number, line in enumerate(input_file):
        
        for symbol in re.finditer("[^\d\.\n]", line):
            symbol_coordinates[line_number + 1].append(symbol.start())
        
        for number in re.finditer("\d+", line):
            coordinate = {
                "number": number.group(),
                "line_number": line_number + 1,
                "start": number.start(),
                "end": number.end()
            }
            number_coordinates.append(coordinate)

for coordinates in number_coordinates:
        number = coordinates["number"]
        line_numbers = [coordinates["line_number"] - 1, coordinates["line_number"], coordinates["line_number"] + 1]
        indexes =  list(range(coordinates["start"] - 1, coordinates["end"] + 1, 1))

        for line_number in line_numbers:
            symbol_indexes = symbol_coordinates.get(line_number)
            if symbol_indexes is not None:
                intersection = [i for i in symbol_indexes if i in indexes]
                if len(intersection) > 0:
                    solution += int(number)

    
pp.pprint(solution)