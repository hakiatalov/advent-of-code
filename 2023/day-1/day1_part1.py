"""
On each line, the calibration value can be found by combining the
first digit and the last digit (in that order) to form a single two-digit number

Iterate through the file line by line.
Need a list and keep pushing all the digits into the list.
Then go through each item and concatenate the first and last, parse into an int, and add to total.

"""

calibration_values = []
sum_of_calibration_values = 0

# Open the file
with open("input.txt") as input_file:
    for line in input_file:
        number_list = []
        for ch in line:
            if ch.isnumeric():
                number_list.append(ch)
        calibration_values.append(number_list)

for value in calibration_values:
    first = value[0]
    last = value[-1]
    combined = int(str(first) + str(last))
    sum_of_calibration_values += combined

print(sum_of_calibration_values)