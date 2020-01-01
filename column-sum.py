A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
# creating a empty matrix
result = [0 for x in range(len(A))]

for row in A:
    for index in range(len(A)):
        result[index] += row[index]
        
print(result)