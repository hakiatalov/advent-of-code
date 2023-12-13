import re
from collections import defaultdict

# {card number: number of instances}
card_instances = defaultdict(int)

with open("input.txt") as input_file:
  for index, line in enumerate(input_file):
    card_number = index + 1
    card_instances[card_number] = 1

with open("input.txt") as input_file:
  for index, line in enumerate(input_file):
    card_number = index + 1
    card_value = 0

    winning_numbers_string = re.findall(r"(?<=:\s)(.*?)(?=\s\|)", line)
    winning_numbers = re.findall(r"\d+", winning_numbers_string[0])
    
    my_numbers_string = re.findall(r"(?<=\|\s)(.*?)(?=$)", line)
    my_numbers = re.findall(r"\d+", my_numbers_string[0])

    number_of_winners = len([i for i in my_numbers if i in winning_numbers])

    for i in range(card_instances[card_number]):
      for j in range(1, number_of_winners + 1, 1):
        if card_instances.get(card_number + j) is not None:
          card_instances[card_number + j] += 1
    
solution = sum(card_instances.values())

print(solution)