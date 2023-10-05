def calculate(num_of_courses,student_course):
    course_map={}
    unique_courses=[]
    #add lists for all the courses taken by a student
    for map in student_course:
        if map[1] not in unique_courses:
            unique_courses.append(map[1])
        #if the student doesnt exist add it
        if map[0] not in course_map:

            course_map[map[0]]=[map[1]]
         
        else:
            #if the student doesnt exist for the course add him
            if map[1] not in course_map[map[0]]:
                course_map[map[0]].append(map[1])
            #if the student already registerd skip the record
            else:
                continue
                
   
 
    
    length= len(unique_courses)
    graph= [['0' for i in range(length)] for j in range(length)]
    
    for i in range(length):
        for j in range(length):
            if i ==j:
                continue
            else:
                for key in course_map:
                    if unique_courses[i] in course_map[key] and unique_courses[j] in course_map[key]:
                        graph[i][j]='1'
                        graph[j][i]='1'
       
                
    return graph
path = "graph.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        lines.append(line_values)

path = "graph.out"
lines2=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        lines2.append(line_values)
counter2=0
counter=0
num_of_courses=0
got_courses=0
student_course=[]
for i in range(len(lines)):
        print("hi")
        if lines[i][0]=="0":
            break
        elif len(lines[i])==1:
            num_of_courses=int(lines[i][0])
            
        else:

            student_course.append(lines[i])
            got_courses+=1
            if(got_courses==num_of_courses):
                #start calculating
                answer= calculate(num_of_courses,student_course)
                for row in answer:
                    answerline=""
                    print(row)
                    if row!= lines[counter2]:
                        print("mistake")
                        print(lines2[counter2])
                        break
                    counter2+=1
                got_courses=0
                student_course=[]
                
                print("")
