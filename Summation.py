# Created by MARUF ROBN
# github address: https://github.com/marufrobin/

A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

B = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

result = [[0 for x in range(len(A))] for y in range(len(A))]


"""
    Summation of two Matrix
"""
for i in range(len(A)):
    for j in range(len(A)):
        result[i][j] = A[i][j] + B[i][j]


print(result)



