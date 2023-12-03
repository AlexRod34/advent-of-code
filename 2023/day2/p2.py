import sys

# Part 1
max_blues = 14
max_greens = 13
max_reds = 12
sum_game_numbers = 0

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        # Split to separate game number and hands in single games
        current_line = line.split(":")
        game_number = current_line[0].split()[1]
        current_game_hands = current_line[1].split(";")
        valid_flag  = True
        # Iterate over each sub-game shown in a single game
        for sub_game in current_game_hands:
            num_colors = sub_game.split(",")
            # Iterate over each number color pair in each 
            for num_color in num_colors:
                number = int(num_color.split()[0])
                color = num_color.split()[1]

                # Check against each max of colors in this current subgame
                if color == "blue" and number > max_blues :
                    valid_flag = False
                    break
                elif color == "red" and number > max_reds:
                    valid_flag = False
                    break
                elif color == "green" and number > max_greens:
                    valid_flag = False
                    break
            
        if valid_flag:
            sum_game_numbers += int(game_number)
    
print("Part 1: " + str(sum_game_numbers))


# Part 2
sum_power = 0 
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        # Split to separate game number and hands in single games
        current_line = line.split(":")
        game_number = current_line[0].split()[1]
        current_game_hands = current_line[1].split(";")

        min_blues_in_game = 0
        min_greens_in_game = 0
        min_reds_in_game = 0

        # Iterate over each sub-game shown in a single game
        for sub_game in current_game_hands:
            num_colors = sub_game.split(",")
            # Iterate over each number color pair in each 
            for num_color in num_colors:
                number = int(num_color.split()[0])
                color = num_color.split()[1]

                if color == "blue" and number > min_blues_in_game:
                    min_blues_in_game = number
                elif color == "red" and number > min_reds_in_game:
                    min_reds_in_game = number
                elif color == "green" and number > min_greens_in_game:
                    min_greens_in_game = number
        power_of_cubes = min_blues_in_game * min_reds_in_game * min_greens_in_game
        sum_power += power_of_cubes
    
print("Part 2: " + str(sum_power))