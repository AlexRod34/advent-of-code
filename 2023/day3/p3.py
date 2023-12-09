import sys

# Part 1
def checkAdjacents(grid, row, start_col, end_col):
    num_rows = len(grid)
    num_cols = len(grid[0])
    print("checking adjacents")
    for col in range(start_col, end_col + 1):
        # Check left
        if col > 0:
            if not grid[row][col - 1].isdigit() and grid[row][col - 1] != ".":
                print("Found a symbol to the left!")
                return True
        # Check left down
        if row == 0 and col == num_cols - 1 or row < num_rows - 1 and col > 0:
            if not grid[row + 1][col - 1].isdigit() and grid[row + 1][col - 1] != ".":
                print("Found a symbol to the left down!")
                return True
        # Check left up
        if  row == num_rows - 1 and col == num_cols - 1 or row > 0 and col > 0:
            if not grid[row - 1][col - 1].isdigit() and grid[row - 1][col - 1] != ".":
                print("Found a symbol to the left up!")
                return True
        # Check right
        if col < num_cols - 1:
            if not grid[row][col + 1].isdigit() and grid[row][col + 1] != ".":
                print("Found a symbol to the right!")
                return True
        # Check right down
        if row == 0 and col == 0 or row < num_rows - 1 and col < num_cols - 1:
            if not grid[row + 1][col + 1].isdigit() and grid[row + 1][col + 1] != ".":
                print("Found a symbol to the right down!")
                return True
        # Check right up
        if row == num_rows - 1 and col == 0 or row > 0 and col < num_cols - 1:
            if not grid[row - 1][col + 1].isdigit() and grid[row - 1][col + 1] != ".":
                print("Found a symbol to the right up!")
                return True

        # Check top
        if (row == num_rows - 1 and col == 0) or (row == num_rows - 1 and col == num_cols - 1) or row > 0: 
            if not grid[row - 1][col].isdigit() and grid[row - 1][col] != ".":
                print("Found a symbol to the top!")
                return True
        
        # Check bottom
        if row == 0 and col == 0 or row == 0 and col == num_cols - 1 or row < num_rows - 1:
            if not grid[row + 1][col].isdigit() and grid[row + 1][col] != ".":
                print("Found a symbol to the bottom!")
                return True
    return False

# Part 2
def checkGears(grid, row, start_col, end_col):
    num_rows = len(grid)
    num_cols = len(grid[0])
    print("checking gears")
    for col in range(start_col, end_col + 1):
        # Check left
        if col > 0:
            if grid[row][col - 1] == "*":
                print("Found a gear to the left!")
                key = str(row) + "," + str(col - 1)
                return key
        # Check left down
        if row == 0 and col == num_cols - 1 or row < num_rows - 1 and col > 0:
            if grid[row + 1][col - 1] == "*":
                print("Found a gear to the left down!")
                key = str(row + 1) + "," + str(col - 1)
                return key
        # Check left up
        if  row == num_rows - 1 and col == num_cols - 1 or row > 0 and col > 0:
            if grid[row - 1][col - 1] == "*":
                print("Found a gear to the left up!")
                key = str(row - 1) + "," + str(col - 1)
                return key
        # Check right
        if col < num_cols - 1:
            if grid[row][col + 1] == "*":
                print("Found a gear to the right!")
                key = str(row) + "," + str(col + 1)
                return key
        # Check right down
        if row == 0 and col == 0 or row < num_rows - 1 and col < num_cols - 1:
            if grid[row + 1][col + 1] == "*":
                print("Found a gear to the right down!")
                key = str(row + 1) + "," + str(col + 1)
                return key
        # Check right up
        if row == num_rows - 1 and col == 0 or row > 0 and col < num_cols - 1:
            if grid[row - 1][col + 1] == "*":
                print("Found a gear to the right up!")
                key = str(row - 1) + "," + str(col + 1)
                return key
        # Check top
        if (row == num_rows - 1 and col == 0) or (row == num_rows - 1 and col == num_cols - 1) or row > 0: 
            if grid[row - 1][col] == "*":
                print("Found a gear to the top!")
                key = str(row - 1) + "," + str(col)
                return key
        
        # Check bottom
        if row == 0 and col == 0 or row == 0 and col == num_cols - 1 or row < num_rows - 1:
            if grid[row + 1][col] == "*":
                print("Found a gear to the bottom!")
                key = str(row + 1) + "," + str(col)
                return key
    return '0'


schematic = []
gear_dict = dict()

with open(sys.argv[1], 'r') as input_file:
    for line in input_file.readlines():
        schematic.append(line.strip())

index_row = 0
isPartNumber = False
gearPos = '0'
sum_part_number = 0
sum_gear_ratio = 0
for row in schematic:
    index_col = 0
    start_num_index = 99999
    end_num_index = -1
    for col in row:
        # If char is a period, continue
        if schematic[index_row][index_col] == "." or not schematic[index_row][index_col].isdigit():
            print("Found a period or symbol, skipping")
        else:
            print(schematic[index_row][index_col])
            # Get the starting index of a number in a row
            if schematic[index_row][index_col].isdigit() and index_col < start_num_index:
                start_num_index = index_col
            # Keep track of the ending index of a number in a row
            if schematic[index_row][index_col].isdigit() and index_col > end_num_index:
                end_num_index = index_col
            # Check next element in grid, if not a digit or if out of bounds, we have our start and finish bounds so let's check this numbers adjacent elements
            if index_col == len(row) - 1 or (index_col < len(row) - 1 and not schematic[index_row][index_col + 1].isdigit()):
                # Part 1:
                isPartNumber = checkAdjacents(schematic, index_row, start_num_index, end_num_index)
                if isPartNumber:
                    partNumber = schematic[index_row][start_num_index:end_num_index + 1]
                    print("Found a part number: " + partNumber)
                    sum_part_number += int(partNumber)
                # Part 2
                gearPos = checkGears(schematic, index_row, start_num_index, end_num_index)
                if gearPos != '0':
                    partNumber = schematic[index_row][start_num_index:end_num_index + 1]
                    print("Found a part number: " + partNumber + " at: " + gearPos)
                    if gearPos not in gear_dict:
                        gear_dict[gearPos] = []
                    gear_dict[gearPos].append(partNumber)
                # Reset indices after parsing one number on the current row
                start_num_index = 99999
                end_num_index = -1
        index_col +=1
    index_row +=1

print("Part 1: " + str(sum_part_number))

# Multiply and sum up all gear ratios found with a common * as the adjacent symbol
# Note: What if there is:
# 755..
# ..*..
# .123.
# ..*..
# ..555
# I think input does not allow back to back part numbers with adjacent gears - otherwise how would we know which numbers to multiply?
for key, value in gear_dict.items():
    curr_ratio = 1
    if len(value) > 1:
        print(key, ":", value)
        for num in value:
            curr_ratio *= int(num)
        sum_gear_ratio += curr_ratio
print("Part 2:" + str(sum_gear_ratio))
