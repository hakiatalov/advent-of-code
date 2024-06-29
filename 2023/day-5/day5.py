import sys
import re
import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

# Getting the file and lines
input = open(sys.argv[1]).read().strip()
lines = input.split("\n")

# Declaring required data structures
seed_list = []
data_map = defaultdict(lambda: defaultdict(int))
headers = [
  "seeds",
  "seed-to-soil map",
  "soil-to-fertilizer map",
  "fertilizer-to-water map",
  "water-to-light map",
  "light-to-temperature map",
  "temperature-to-humidity map",
  "humidity-to-location map"
]

# Helper functions
def extract_numbers(data, heading):
  if heading == "humidity-to-location map":
    pattern = rf"({heading}):\s*((?:\d+\s*)+)"
  else:  
    pattern = rf"({heading}):\s*((?:\d+\s*)+)(?=\n\n)"
  match = re.findall(pattern, data)
  match_lines = match[0][1].split('\n')
  return match_lines

# Data extraction
for header in headers:
  match_lines = extract_numbers(input, header)
  data_map[header] = match_lines

pp.pprint(data_map)