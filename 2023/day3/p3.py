import sys

schematic = []
symbols = ["+"]
with open(sys.argv[1], 'r') as input_file:
    for line in input_file.readlines():
        schematic.append(line.strip())

index_row = 0
for row in schematic:
    index_col = 0
    for col in row:
        # print("row: " + str(index_row) + " " + "col: " + str(index_col))
        print("my [i][j] value:" + schematic[index_row][index_col])
        index_col +=1

    index_row +=1