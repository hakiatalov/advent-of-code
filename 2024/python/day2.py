import sys
import re
import copy

def main():
  lines = []

  with open(sys.argv[1]) as f:
    lines = f.read().strip().split('\n')

  part1(lines)
  

def part1(lines):
  p = re.compile('\d+')
  result = 0

  for line in lines:
    levels = p.findall(line)
    safe = checkSafety(levels)    

    if safe:
      result += 1
    else:
      if part2(levels):
        result += 1
    
  print(f'Part 1 Result: {result}')


def part2(levels) -> bool:
  # remove each element and check the safety again
  for i in range(len(levels)):
    arrayCopy = copy.deepcopy(levels)
    del arrayCopy[i]
    safe = checkSafety(arrayCopy)
    if safe:
      break
  
  return safe


def checkSafety(levels) -> bool:
  safe = True
  increasing = False
  decreasing = False

  # figure out if increasing or decreasing
  if int(levels[0]) - int(levels[1]) > 0:
    increasing = True
  else:
    decreasing = True

  for i in range(len(levels)):
    if i == 0:
      continue

    difference = int(levels[i - 1]) - int(levels[i])
    if abs(difference) == 0 or abs(difference) > 3:
      safe = False
      break

    if difference > 0 and decreasing:
      safe = False
      break

    if difference < 0 and increasing:
      safe = False
      break

  return safe


main()