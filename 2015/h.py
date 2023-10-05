def zero(cord,map):
    print(cord)
    paths=[
          [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+0],
          [cord[0]+1,cord[1]+2],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+0],
          [cord[0]+3,cord[1]+2],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],
          [cord[0]+4,cord[1]+2]]
    
    print([cord[0]+0,cord[1]+1])
    
    for neighbor_i,neighbor_j in paths:
    
        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for zero with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="0":
                print("not zero")
                print(map[neighbor_i][neighbor_j])
                return False 
        else:
            return False
    return True
def one(cord,map):
    paths=[
          [cord[0]+1,cord[1]+0],
          [cord[0]+1,cord[1]-1],
          [cord[0]+2,cord[1]+0],
          [cord[0]+3,cord[1]+0],
          [cord[0]+4,cord[1]+-1],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],]
    
    for neighbor_i,neighbor_j in paths:

        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for one with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="1":
                print("not one")
                print(map[neighbor_i][neighbor_j])
                return False  
        else:
            return False
    return True
def two(cord,map):
    paths=[
          [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+2],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+1],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+0],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],
          [cord[0]+4,cord[1]+2]]
    
    for neighbor_i,neighbor_j in paths:

        # Check if the neighbor is within the bounds of the map
        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for two with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="2":
                print("not two")
                print(map[neighbor_i][neighbor_j])
                return False
        else:
            return False 
    return True
def three(cord,map):
    paths=[
          [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+2],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+1],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+2],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],
          [cord[0]+4,cord[1]+2]]
    
    for neighbor_i,neighbor_j in paths:

        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for three with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="3":
                print("not three")
                print(map[neighbor_i][neighbor_j])
                return False
        else:
            return False 
    return True
def four(cord,map):
    paths=[
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+0],
          [cord[0]+1,cord[1]+2],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+1],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+2],
          [cord[0]+4,cord[1]+2],]
    
    for neighbor_i,neighbor_j in paths:

        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for four with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="4":
                print("not four")
                print(map[neighbor_i][neighbor_j])
                return False 
        else:
            return False
    return True
def five(cord,map):

    paths=[
          [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+0],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+1],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+2],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],
          [cord[0]+4,cord[1]+2]]
    
    for neighbor_i,neighbor_j in paths:

        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for five with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="5":
                print("not five")
                print(map[neighbor_i][neighbor_j])
                return False 
        else:
            return False
    return True
def six(cord,map):
    paths=[
          [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+0],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+1],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+2],
          [cord[0]+3,cord[1]+0],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],
          [cord[0]+4,cord[1]+2]]
    
    for neighbor_i,neighbor_j in paths:
        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for six with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="6":
                print("not six")
                print(map[neighbor_i][neighbor_j])
                return False
        else:
            return False 
    return True
def seven(cord,map):
    paths=[
          [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+2],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+2],
          [cord[0]+4,cord[1]+2]]
    
    for neighbor_i,neighbor_j in paths:

        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for sevem with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="7":
                print("not seven")
                print(map[neighbor_i][neighbor_j])
                return False
        else:
            return False  
    return True
def eight(cord,map):
    paths=[
         [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+0],
          [cord[0]+1,cord[1]+2],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+1],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+2],
          [cord[0]+3,cord[1]+0],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],
          [cord[0]+4,cord[1]+2]]
    
    for neighbor_i,neighbor_j in paths:

        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for eight with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="8":
                print("not eight")
                print(map[neighbor_i][neighbor_j])
                return False  
        else:
            return False
    return True
def nine(cord,map):

    paths=[
          [cord[0]+0,cord[1]+1],
          [cord[0]+0,cord[1]+2],
          [cord[0]+1,cord[1]+0],
          [cord[0]+1,cord[1]+2],
          [cord[0]+2,cord[1]+0],
          [cord[0]+2,cord[1]+1],
          [cord[0]+2,cord[1]+2],
          [cord[0]+3,cord[1]+2],
          [cord[0]+4,cord[1]+0],
          [cord[0]+4,cord[1]+1],
          [cord[0]+4,cord[1]+2]]
    
    for neighbor_i,neighbor_j in paths:
        
        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_i < len(map) and 0 <= neighbor_j < len(map[0][0]):
            print("check for nine with " +map[neighbor_i][0][neighbor_j])
            if map[neighbor_i][0][neighbor_j]!="9":
                print("not nine")
                print(map[neighbor_i][neighbor_j])
                return False 
        else:
            print("in else")
            return False
    return True


def calculate(shape_i,shape_j,maps):

    list=[0,0,0,0,0,0,0,0,0,0]
    for i in range(len(maps)):
        map=maps[i][0]
        for j in range(len(map)):

            if map[j]=="0" and zero([i,j],maps):
                list[0]+=1
            elif map[j]=="1" and one([i,j],maps):
                list[1]+=1
            elif map[j]=="2" and two([i,j],maps):
                list[2]+=1
            elif map[j]=="3" and three([i,j],maps):
                list[3]+=1
            elif map[j]=="4" and four([i,j],maps):
                list[4]+=1
            elif map[j]=="5" and five([i,j],maps):
                list[5]+=1
            elif map[j]=="6" and six([i,j],maps):
                list[6]+=1
            elif map[j]=="7" and seven([i,j],maps):
                list[7]+=1
            elif map[j]=="8" and eight([i,j],maps):
                list[8]+=1
            elif map[j]=="9" and nine([i,j],maps):
                list[9]+=1
    return list
        
path = "pattern.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)





############################create the paths##################
#############################################################









counter=1
map=[]
for i in range(1,len(lines)):
    line = lines[i]
    if i ==counter:
        counter+=int(line[0])+1
        shape_i=int(line[0])
        shape_j=int(line[1])
    else:
        map.append(line)
        if i+1==counter:
            #start calculating
            answer = calculate(shape_i,shape_j,map)
            print(answer)
            map=[]
    
        