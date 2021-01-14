def multiplication(matrix,vector,m,n,a,b):
    ans=[]
    for i in range(m):
        row=[]
        for j in range(b):
            element=0
            for k in range(n):
                element+=matrix[i][k]*vector[k][j]
            row.append(element)
        ans.append(row)
    return ans
    

vector=[[3],[2],[1]]
matrix=[[2,3,4],[1,3,8],[6,2,8]]
ans=multiplication(matrix,vector,len(matrix),len(matrix[0]),len(vector),len(vector[0]))
print("VECTOR-MATRIX MULTIPLICATION:",ans)

