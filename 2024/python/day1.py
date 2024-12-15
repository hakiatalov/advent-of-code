import sys
import re

def main():
    lines = []

    with open(sys.argv[1]) as f:
        lines = f.read().strip().split("\n")

    part1(lines)


def part1(lines):
    result_part1 = 0
    result_part2 = 0
    right_list = []
    left_list = []

    p = re.compile("\d+")

    for l in lines:
        matches = p.findall(l)
        right_list.append(int(matches[0]))
        left_list.append(int(matches[1]))
            
    right_list.sort()
    left_list.sort()

    for i in range(len(right_list)):
        result_part1 += abs(right_list[i] - left_list[i])
        result_part2 += left_list[i] * right_list.count(left_list[i])


    print(f"Part 1 result: {result_part1}")
    print(f"Part 2 result: {result_part2}")
    

main()