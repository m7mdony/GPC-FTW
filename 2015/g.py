

def  calculate(transactions,least_transactions,substring_length):
    substrings=[]
    
    uniqueLetters=""
 
    for i in range(len(transactions)):
        transaction=transactions[i][0]
        
        for j in range(len(transaction)):
            if transaction[j] not in uniqueLetters:
               
                uniqueLetters+=transaction[j]
    print(uniqueLetters)
    
    for i in range(len(uniqueLetters)-k+1):
        string = uniqueLetters[i:i+k]
        substrings.append(string)
    print(substrings)
    return

path = "transaction.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)


counter=0
transactions=[]
for i in range(len(lines)):
    if i == counter:
        #new test case
        #set the counter of the line of the new testcase
        counter+= int(lines[i][0])+2
    elif len(lines[i])==1:
        #get the transaction
        transactions.append(lines[i])
    else:
        #get s and k 
        s= int(lines[i][0])
        k= int(lines[i][1])
        
        #start calculating 
        answer = calculate(transactions,s,k)