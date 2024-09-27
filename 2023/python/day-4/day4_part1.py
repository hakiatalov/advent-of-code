import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

solution = 0

with open("input.txt") as input_file:
  for line in input_file:
    card_value = 0

    winning_numbers_string = re.findall(r"(?<=:\s)(.*?)(?=\s\|)", line)
    winning_numbers = re.findall(r"\d+", winning_numbers_string[0])
    
    my_numbers_string = re.findall(r"(?<=\|\s)(.*?)(?=$)", line)
    my_numbers = re.findall(r"\d+", my_numbers_string[0])

    intersection = [i for i in my_numbers if i in winning_numbers]
    if len(intersection) > 0:
      for i, num in enumerate(intersection):
        if i == 0:
          card_value += 1
          continue
        card_value *= 2
    
    solution += card_value

print(solution)