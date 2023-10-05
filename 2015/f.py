def check(rocket_top_left,rocket_top_right,rocket_bottom_left,rocket_bottom_right,reigon_top_left,reigon_top_right,reigon_bottom_left,reigon_bottom_right):
    
    if rocket_top_left < reigon_top_left or square2[1][0] < square1[0][0] or square1[1][1] < square2[0][1] or square2[1][1] < square1[0][1]:
        # Squares do not overlap
        return 0
    return
    
def calculate(reigons,rocket_x,rocket_y,distraction):
    print(reigons,rocket_y,rocket_x,distraction)
    rocket_top_left=[rocket_x-(distraction/2),rocket_y-(distraction/2)]
    rocket_top_right=[rocket_x+(distraction/2),rocket_y-(distraction/2)]
    rocket_bottom_left=[rocket_x-(distraction/2),rocket_y+(distraction/2)]
    rocket_bottom_right=[rocket_x+(distraction/2),rocket_y+(distraction/2)]
    for reigon in reigons:
        reigon_x= int(reigon[1])
        reigon_y= int(reigon[2])
        reigon_width= int(reigon[3])
        reigon_height= int(reigon[4])
        population= int(reigon[5])
        reigon_top_left=[reigon_x,reigon_y]
        reigon_top_right=[reigon_x+reigon_width,reigon_y]
        reigon_bottom_left=[reigon_x,reigon_y+reigon_height]
        reigon_bottom_right=[reigon_x+reigon_width,reigon_y+reigon_height]
        distraction_percentage= check(rocket_top_left,rocket_top_right,rocket_bottom_left,rocket_bottom_right,reigon_top_left,reigon_top_right,reigon_bottom_left,reigon_bottom_right)
    return
path = "impact.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        lines.append(line_values)

reigons_num=0
reigons=[]
for i in range(len(lines)):
    line=lines[i]

    if len(line)==1:
        print("hello")
        #new testcase
        reigons_num=int(line[0])
        continue
    else:
            
        if i+1==len(lines):
            #end of testcase and file

            rocket_x=int(line[0])
            rocket_y=int(line[1])
            distraction=int(line[2])
            answer= calculate(reigons,rocket_x,rocket_y,distraction)
            break
        elif len(lines[i+1])==1:
            #end of a testcase
            rocket_x=int(line[0])
            rocket_y=int(line[1])
            distraction=int(line[2])
            answer= calculate(reigons,rocket_x,rocket_y,distraction)
              
        else:

            reigons.append(line)