def coFactor(mat,row,col):
    minor=[]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if not (i==row or j==col):
                minor.append(mat[i][j])
    return (minor[0]*minor[3])-(minor[1]*minor[2])
                
def determinant(m,order):
    if order==2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    if order==3:
        return (m[0][0]*coFactor(m,0,0))-(m[0][1]*coFactor(m,0,1))+(m[0][2]*coFactor(m,0,2))

def adjointMatrix(m,order):
    if order==2:
        n=[[0,0,],[0,0]]
        n[0][0],n[0][1],n[1][0],n[1][1]=m[1][1],-m[1][0],-m[0][1],m[0][0] 
        return transpose(n)
    if order==3:
        n=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(m)):
            for j in range(len(m[0])):
                n[i][j]= ((-1)**(i+j))*coFactor(m,i,j)   
        return transpose(n)

def transpose(m):
    tra=[]
    for i in range(len(m)):
        row=[]
        for j in range(len(m[0])):
            element=m[j][i]
            row.append(element)
        tra.append(row)
    return tra

def inverseMatrix(det,adj):
    det=1/det
    for i in range(len(adj)):
        for j in range(len(adj[0])):
            adj[i][j]=adj[i][j]*det
    return adj    
    



matrix = [[1,0],[0,1]]
d=determinant(matrix,len(matrix))
a=adjointMatrix(matrix,len(matrix))
print("determinant and adjoint:",d,a)
print("INVERSE MATRIX:",inverseMatrix(d,a))
