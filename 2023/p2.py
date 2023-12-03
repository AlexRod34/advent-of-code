# Read in text file with games as each line
# In each line, parse the Game number, and the number of green, blue, red cubes with their corresponding numbers
# In each line, check the total of green, blue, red cubes to see if the numbers are <= to 12 red, 13 green, and 14 blue cubes
# If the condition is satisfied, add the Game number to a running sum
import sys

max_blues = 14
max_greens = 13
max_reds = 12
sum_game_numbers = 0

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        # Split to separate Game number and hands in single games
        current_line = line.split(":")
        game_number = current_line[0].split()[1]
        current_game_hands = current_line[1].split(";")
        valid_flag  = True
        # Iterate over each hand shown in a single game
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
    
print(sum_game_numbers)

