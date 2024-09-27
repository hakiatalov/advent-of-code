import pprint

pp = pprint.PrettyPrinter(indent=4)

bag_contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}

solution_1 = 0

with open("input.txt") as input_file:
    for line in input_file:
        # Extract all the values
        valid_game = True
        title_and_contents = line.split(":")
        title = title_and_contents[0]
        contents = title_and_contents[1]
        game_number = title.split(' ')[1]
        cube_sets = contents.split(';')

        for cube_set in cube_sets:
            cubes = cube_set.split(",")
            for cube in cubes:
                cube_stripped = cube.strip()
                cube_details = cube_stripped.split(" ")
                cube_color = cube_details[1].strip()
                cube_quantity = int(cube_details[0].strip())

                if int(cube_quantity) > bag_contents[cube_color]:
                    valid_game = False

        if valid_game:
            solution_1 += int(game_number)

pp.pprint(solution_1)