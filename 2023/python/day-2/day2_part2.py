import pprint

pp = pprint.PrettyPrinter(indent=4)

solution_2 = 0

with open("input.txt") as input_file:
    for line in input_file:
        # Extract all the values
        title_and_contents = line.split(":")
        title = title_and_contents[0]
        contents = title_and_contents[1]
        game_number = title.split(' ')[1]
        cube_sets = contents.split(';')

        min_cube_quantity = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for cube_set in cube_sets:
            cubes = cube_set.split(",")

            for cube in cubes:
                cube_stripped = cube.strip()
                cube_details = cube_stripped.split(" ")
                cube_color = cube_details[1].strip()
                cube_quantity = int(cube_details[0].strip())

                if int(cube_quantity) > min_cube_quantity[cube_color]:
                    min_cube_quantity[cube_color] = cube_quantity

        pp.pprint(line)
        pp.pprint(min_cube_quantity)
        set_of_cubes_power = 1

        for quantity in min_cube_quantity.values():
            set_of_cubes_power = set_of_cubes_power * quantity

        solution_2 += set_of_cubes_power


pp.pprint(solution_2)