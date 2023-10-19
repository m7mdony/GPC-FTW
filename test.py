def make(i,j):
    points=[[i-1,j],[i,j-1],[i,j+1],[i+1,j]]
    return points
def search(island,i,j,visited):
    visited[str([i,j])]=True
    points=make(i,j)
    for point in points:
        if str(point) not in visited and point[0]<len(island)and point[1]<len(island[point[0]]) and island[point[0]][point[1]]==1:
            search(island,point[0],point[1],visited)
            
        
    

def count(island):
    
    visited={}
    counter=0
    for i in range(len(island)):
        for j in range(len(island[i])):

            if str([i,j])not in visited and island[i][j]==1:
                
                search(island,i,j,visited)
                counter+=1
                
    return counter


island=[[0,1,0,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,1,1,0],[1,0,0,1,1],[1,1,0,0,0]]

print(count(island))