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

        # Edge cases (check first?)
        # Check top left corner - can check bottom, right down
        # if row == 0 and col == 0:

        # # Check bottom left corner - can check top, right up
        # if row == num_rows - 1 and col == 0:

        # # Check top right corner -  can check bottom, left down
        # if row == 0 and col == num_cols - 1:

        # # Check bottom right corner - can check top, left up
        # if row == num_rows - 1 and col == num_cols - 1:
    return False
    # print(grid[row][start_col:end_col + 1])


schematic = []
symbols = ["+"]
with open(sys.argv[1], 'r') as input_file:
    for line in input_file.readlines():
        schematic.append(line.strip())

index_row = 0
isPartNumber = False
sum_part_number = 0
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
                print(start_num_index)
                # print(schematic[index_row][index_col])
            # Keep track of the ending index of a number in a row
            if schematic[index_row][index_col].isdigit() and index_col > end_num_index:
                end_num_index = index_col
                print(end_num_index)
            # Check next element in grid, if not a digit or if out of bounds, we have our start and finish bounds so let's check this numbers adjacent elements
            if index_col == len(row) - 1 or (index_col < len(row) - 1 and not schematic[index_row][index_col + 1].isdigit()):
                print(str(start_num_index) + ":" + str(end_num_index))
                isPartNumber = checkAdjacents(schematic, index_row, start_num_index, end_num_index)
                if isPartNumber:
                    partNumber = schematic[index_row][start_num_index:end_num_index + 1]
                    print("Found a part number: " + partNumber)
                    sum_part_number += int(partNumber)
                # Reset indices after parsing one number on the current row
                print("RESET")
                start_num_index = 99999
                end_num_index = -1

        # Check if current char is a digit, if so mark fist index of char
        # Check if next char is digit without going indexoutofbounds
        # If next char is not a digit, time to check all adjacent chars for symbols (not a digit and not a period) based on the start and end indices
        index_col +=1
    index_row +=1
print(sum_part_number)
