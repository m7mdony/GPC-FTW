# class tree:
#     def __inti__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None
def make(m,n,tree):
    tree_copy=tree.copy()
    for i in range(len(tree)-1):
        m1,n1=tree[i].split(" ")
        m1=int(m1)
        n1=int(n1)
        m2,n2=tree[i+1].split(" ")
        m2=int(m2)
        n2=int(n2)
        final_m=m1+m2
        final_n=n1+n2
        final_m=str(final_m)
        final_n=str(final_n)
        index= tree_copy.index(tree[i])
        tree_copy.insert(index+1,final_m+" "+final_n)

    if str(m)+" "+str(n) not in tree_copy:
        tree_copy =make(m,n,tree_copy)    
    return tree_copy
def calculate(m,n,tree):
    position = len(tree)//2
    string=""
    
    if m ==1 and n==1:
        return ""
    if m==0 and n==1:
        return ""
    if m==1 and n==0:
        return ""
    if tree[position].split(" ")[0]==str(m) and tree[position].split(" ")[1]==str(n):
        return 1
    elif len(tree)==1:
        return 0
    
    tree_copy=tree.copy()
    try:
        tree_copy.remove("1 0")
        tree_copy.remove("0 1")
        
    except:
        a=1
    
    position = len(tree_copy)//2
    tree1= tree_copy[:position:]
    tree2= tree_copy[position+1::]
    answer1 = calculate(m,n,tree1)
    answer2=calculate(m,n,tree2)
    if answer1:
        if type(answer1)==str:
            string+=answer1
        string+="L"

        return string
    if answer2:
        if type(answer2)==str:
            string+=answer2
        string+="R"

        return string
        
    return ""

m=878 
n=323
tree=["0 1","1 1","1 0"]
if str(m)+" "+str(n) not in tree:
    tree =make(m,n,tree)
print(tree)
answer= calculate(m,n,tree)
print(answer[::-1])
