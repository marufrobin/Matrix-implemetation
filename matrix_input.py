# import numpy as np 
  
# R= C = int(input("Enter the number of rows and colume:")) 

  
  
# print("Enter the entries in a single line (separated by space): ") 
  
# # User input of entries in a  
# # single line separated by space 
# entries = list(map(int, input().split())) 
  
# # For printing the matrix 
# matrix = np.array(entries).reshape(R, C) 

# print(matrix) 

# digonalsum = 0
# for i in range(R):
#     digonalsum += matrix[i][i]
# print(digonalsum)

# for x in range(R):
#     for y in range(C):
#         if x==0 and y==2:
#             r1=matrix[x][y]
#         if x==2 and y==0:
#             r2=matrix[x][y]
#         if x==1 and y==1:
#             r=matrix[x][y]
# anotherdigonalsum = r+r1+r2 
# print(anotherdigonalsum)
# n = int(input()) 
# a = []
# for i in range(n):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)
# m = int(input('number of rows, m = '))
# n = int(input('number of columns, n = '))
# matrix = []
# # initialize the number of rows
# for i in range(0,m):
#     matrix += [0]
# # initialize the matrix
# for i in range (0,m):
#     matrix[i] = [0]*n
# for i in range (0,m):
#     for j in range (0,n):
#         print ('entry in row: ',i+1,' column: ',j+1)
#         matrix[i][j] = int(input())
# print (matrix)
# m = int(input('number of rows, m : '))
# n = int(input('number of columns, n : '))
# a=[]
# for i in range(1,m+1):
#   b = []
#   print("{0} Row".format(i))
#   for j in range(1,n+1):
#     b.append(int(input("{0} Column: " .format(j))))
#   a.append(b)
# print(a)
rows, columns = list(map(int,input().split())) #input no. of row and column
b=[]
for i in range(rows):
    a=list(map(int,input().split()))
    b.append(a)
print(b)