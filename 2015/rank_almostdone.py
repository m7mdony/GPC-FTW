def calculate(num_of_questions,num_of_teams,teams):

    totalTime={}
    for team in teams:
        score={}
        # {
        # quesion num:{
        #     tries:number
        #     state:bool
        #     time:number
        # }
        # }
        #initli the variables prv question to the first question of the list and the state to be unsolved
        previousQuestion=""
        previousState=True
     
        for i in range(len(teams[team])):

            if teams[team][i][1] != previousQuestion:
               ## if the teams[team] didnt end up solving the question dont calculate the ti
                if not previousState:
                    del score[previousQuestion]
               
                previousQuestion=teams[team][i][1]
                if teams[team][i][4]=='i':
                    previousState=False
                elif teams[team][i][4]=="c":
                    previousState=True
                    
                    
                score[previousQuestion]={"tries":1,"state":False}
                
                #add the number of tries to the hashmap of the question
                if teams[team][i][4]=='i':
                    score[previousQuestion]["state"]=False
                elif teams[team][i][4]=="c":
                    score[previousQuestion]["state"]=True
                    score[previousQuestion]["time"]=int(teams[team][i][3])
                
            else:
                
                if teams[team][i][4]=='i':
                    previousState=False
                elif teams[team][i][4]=="c":
                    previousState=True
                #add the number of tries to the hashmap of the question
                score[previousQuestion]["tries"]+=1
                if teams[team][i][4]=='i':
                    score[previousQuestion]["state"]=False
                elif teams[team][i][4]=="c":
                    score[previousQuestion]["state"]=True
                    score[previousQuestion]["time"]=int(teams[team][i][3])

        if not previousState:
            del score[previousQuestion]

        #caclcuatet hte total time
        time=0
        for key in score:
            time+=((score[key]["tries"]-1)*20)+score[key]["time"]

        totalTime[team]=time


    teamsID=sorted(teams.keys())
    teams

    
    
    return totalTime
path = "rank.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        lines.append(line_values)
        

teams={}
for i  in range(len(lines)):
    line=lines[i]
    if len(line)==2:
        #start of a new testcase
        num_of_teams=int(line[0])
        num_of_questions=int(line[1])
    else:
        #store data of the question for the specifc team
        if line[2] not in teams:
            #if doesnt exist make a key and add the question to the key
            teams[line[2]]=[]
            teams[line[2]].append(line)
        else:
            #else just add the qustion to the key
            teams[line[2]].append(line)
        
        #if its the last line end the question
        if i==len(lines)-1:
            answer= calculate(num_of_questions,num_of_teams,teams)
            keys= []
            for key in answer:
                keys.append(key)
            for i in range(1,len(answer.keys())+1):
                print(str(i)+" "+ str(keys[i-1])+" "+ str(answer[keys[i-1]]))
            break
        #if its the last line before the start of a new testcase start calculating
        if len(lines[i+1])==2:
            answer= calculate(num_of_questions,num_of_teams,teams)
            keys= []
            for key in answer:
                keys.append(key)
            for i in range(1,len(answer.keys())+1):
                print(str(i)+" "+ str(keys[i-1])+" "+ str(answer[keys[i-1]]))
            print("should answer")