import pprint
import re
from collections import defaultdict
import math

pp = pprint.PrettyPrinter(indent=4)

symbol_coordinates = defaultdict(list)
number_coordinates = []
solution = 0

with open("input.txt") as input_file:
    for line_number, line in enumerate(input_file):
        
        for symbol in re.finditer("\*", line):
            symbol_coordinates[f"[{line_number + 1}, {symbol.start()}]"] = []
        
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
            for index in indexes:
                key_to_check = f"[{line_number}, {index}]"
                symbol_match = symbol_coordinates.get(key_to_check)
                if symbol_match is not None:
                    symbol_coordinates[key_to_check].append(int(number))

for number_list in symbol_coordinates.values():
    if len(number_list) > 1:
        solution += math.prod(number_list)
          
    
pp.pprint(solution)