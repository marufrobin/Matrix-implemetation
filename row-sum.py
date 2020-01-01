
A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
print(A)
print("-----------------")
# creating a empty matrix 
result = [ 0 for x in range(len(A))]
print(result)

for rowIndex , row in enumerate(A):
    for n in row:
        result[rowIndex] += n

print(result)