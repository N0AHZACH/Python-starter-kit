li = [[1, 2, 3, 4], [1, 2, 3, 4]]
r = 4
c = 2
temp = []

# Flatten the list
for i in range(len(li)):
    for j in range(len(li[0])):
        temp.append(li[i][j])

# Initialize ans with r rows and c columns
ans = [[0] * c for _ in range(r)]

# Fill ans with elements from temp
k = 0
for i in range(r):
    for j in range(c):
        ans[i][j] = temp[k]
        k += 1

# Print the final matrix
for row in ans:
    print(row)
