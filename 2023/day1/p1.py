import sys
import regex as re

calibration_sum = 0
str_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Lookup value if word is found
str_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4", 
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
# Open input text file and read line by line
with open(sys.argv[1], 'r') as input_file:
    # Search each line for the first digit and last digit using regex magic
    for line in input_file:
        pattern = ('|'.join(str_list))
        digitOrWordSearch = re.findall(pattern, line, overlapped=True)
        firstHit = digitOrWordSearch[0]
        lastHit = digitOrWordSearch[-1]

        # Check if we found a word instead of a digit
        if firstHit in str_dict:
            firstHit = str_dict.get(firstHit)

        if lastHit in str_dict:
            lastHit = str_dict.get(lastHit)

        # Concat digits and cast to int, adding the new int to the sum
        digits = firstHit + lastHit
        digits = int(digits)
        calibration_sum += digits

print(calibration_sum)

