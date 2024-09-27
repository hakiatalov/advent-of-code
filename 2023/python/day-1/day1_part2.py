import re
import pprint
from collections import defaultdict

"""
On each line, the calibration value can be found by combining the
first digit and the last digit (in that order) to form a single two-digit number

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
"""

pp = pprint.PrettyPrinter(indent=4)

# Valid written digits. (word, key for map)
valid_digit_strings = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9")
]

# Declare required data structures
digit_occurrences_map = defaultdict(lambda: defaultdict(list))
calibration_values = []
sum_of_calibration_values = 0

# Open the file
with open("input.txt") as input_file:
    for line in input_file:
        # Find all the written digits
        for digit_string in valid_digit_strings:
            for match in re.finditer(digit_string[0], line):
                digit_occurrences_map[line][digit_string[1]].append(match.span()[0])

        # Find all the actual digits
        for i, ch in enumerate(line):
            if ch.isnumeric():
                digit_occurrences_map[line][ch].append(i)

# Loop through dict to find first and last occurrences of digits
for line, digit_data in digit_occurrences_map.items():
    first_digit = []
    last_digit = []

    for digit, indexes in digit_data.items():
        for index in indexes:
            # Handles first occurrence
            if len(first_digit) == 0:
                first_digit.insert(0, digit)
                first_digit.insert(1, index)

            # Handles first occurrence
            if len(last_digit) == 0:
                last_digit.insert(0, digit)
                last_digit.insert(1, index)

            # Compare index of first digit
            if index < first_digit[1]:
                first_digit[0] = digit
                first_digit[1] = index

            # Compare index of last digit
            if index > last_digit[1]:
                last_digit[0] = digit
                last_digit[1] = index

    calibration_values.append((first_digit[0], last_digit[0]))

# Calculate the sum
for value in calibration_values:
    first = value[0]
    last = value[-1]
    combined = int(str(first) + str(last))
    sum_of_calibration_values += combined

print(sum_of_calibration_values)