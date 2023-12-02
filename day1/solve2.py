# Turn a line of input text into an array of all contained digits as strings.  (removes letters)
def getdigits(line : str):
    digits = []
    for char in line:
        if char.isnumeric():
            digits += [char]
    return digits

# Turn the array given by getdigits into an integer of the first and last digits contained.
def getnum(digits : list):
    return int(digits[0] + digits[-1])

# Process a line
def processline(line : str):
    digits = getdigits(line)
    return getnum(digits)

# Change all string versions of numbers into digits
def changetonums(line : str):
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    return line

# Read input
text = open("input.txt", "r")
lines = text.readlines()
text.close()

# Initialize variables
nums = []
answer = 0

# Process all the lines
for line in lines:
    nums += [processline(changetonums(line))]

# Add all numbers together
for num in nums:
    answer += num

# Print answer
print(answer)