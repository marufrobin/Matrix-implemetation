# Created by MARUF ROBN
# github address: https://github.com/marufrobin/


## Input
matrix = [ 
            [1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3], 
            [4, 4, 4, 4]
        ]

print(matrix)
print("---------------------")
# Result Array
transposed = [[0 for x in range(len(matrix))] for y in range(len(matrix))]


for i in range(len(matrix)):
    for j in range(len(matrix)):
        transposed[j][i] = matrix[i][j]


for n in transposed:
    print(n)