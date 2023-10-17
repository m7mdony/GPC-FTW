def calculate(length,row1,row2):
    print(length,row1,row2)
    return

lines=[]
with open("table.in","r") as file:
    for line in file:
        values = line.strip().split()
        lines.append(values)

print(lines)
row1=[]
row2=[]
for i in range(0,len(lines),7):
    length= int(lines[i][0])
    row1.append(lines[i+1])
    row1.append(lines[i+2])
    row1.append(lines[i+3])
    row2.append(lines[i+4])
    row2.append(lines[i+5])
    row2.append(lines[i+6])
    
    answer = calculate(length,row1,row2)
    row1=[]
    row2=[]