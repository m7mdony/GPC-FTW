import time
def calculate(base):
    a, b = 0, 1
    period = 0
    while True:
        a, b = b, (a + b) % base

        period += 1
        if a == 0 and b == 1:
            return period
file_path = 'pisano.in'

# Initialize an empty list to store the 1lines
lines = []
# Open the file for reading
with open(file_path, 'r') as file:
    # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = [int(value) for value in line.strip().split()]
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)
     
for line in lines:
    if line[0]==0:
        break
    else:
        answer = calculate(line[0])
        print(answer)
        