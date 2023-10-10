def calculate(line):

    sentence_list = [char for char in line[0]]

    list=[]
    list.append(line[0])
    for i in range(len(sentence_list)-1):
        char = sentence_list.pop(0)
        sentence_list.append(char)
        sentence= "".join(sentence_list)
        list.append(sentence)
    list.sort()
    return list.index(line[0])

with open("sorter.answer","w"):
    pass

lines=[]

with open("sorter.in","r")as file:
    for line in file:
        value = line.split("\n")
        lines.append(value)

lines.pop(0)


for line in lines:
    answer = calculate(line)
    with open("sorter.answer","a") as file:
        file.write(str(answer)+"\n")
    