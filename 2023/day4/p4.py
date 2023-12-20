import sys

list_win = []
list_my_num = []
sum_cards = 0

# Part 1
print("PART 1 ------------------------------------------------------------")
with open(sys.argv[1], 'r') as input_file:
    for line in input_file.readlines():
        split_line = line.split("|")

        # Handle first part of line
        winning_numbers = split_line[0].split(":")[1]
        list_win = winning_numbers.strip().split(" ")
        # Handle second part of line
        my_numbers = split_line[1]
        list_my_num = my_numbers.strip().split(" ")
        # Remove middle whitespace
        remove_char = ""
        while(remove_char in list_win):
            list_win.remove(remove_char)

        while(remove_char in list_my_num):
            list_my_num.remove(remove_char)

        # Find all matches between your numbers and the winning numbers
        count = 1
        line_total = 0
        for winning_num in list_win:
            if winning_num in list_my_num:
                if count == 1:
                    line_total += 1
                else:
                    line_total *= 2
                count += 1
        # print("Line total: ", line_total)      
        sum_cards += line_total  
        # print("--------------------------------------------")
print("Total 1: ", sum_cards)

print("PART 2 ------------------------------------------------------------")
# Part 2
counts = [1]
with open(sys.argv[1], 'r') as input_file:
    counts = counts * len(input_file.readlines())

with open(sys.argv[1], 'r') as input_file:
    for line_index, line in enumerate(input_file.readlines()):
        split_line = line.split("|")

        # Handle first part of line
        winning_numbers = split_line[0].split(":")[1]
        list_win = winning_numbers.strip().split(" ")
        # Handle second part of line
        my_numbers = split_line[1]
        list_my_num = my_numbers.strip().split(" ")
        # Remove middle whitespace
        remove_char = ""
        while(remove_char in list_win):
            list_win.remove(remove_char)

        while(remove_char in list_my_num):
            list_my_num.remove(remove_char)

        # Find all matches between your numbers and the winning numbers
        num_matches = 0 
        for winning_num in list_win:
            if winning_num in list_my_num:
                num_matches += 1
        # Add all winning matches (copies) to originals
        first_index = line_index + 1
        for i in range(first_index, first_index + num_matches):
            counts[i] += counts[line_index]
print("Total 2: ", sum(counts))