import sys

list_win = []
list_my_num = []
sum_cards = 0
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
        print("Line total: ", line_total)      
        sum_cards += line_total  
        print("--------------------------------------------")
print("Total: ", sum_cards)