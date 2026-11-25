
v = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
a = []

for i in range(v):
    a.append(list(map(int, input().split())))
for k in range(v):
    for i in range(v):
        for j in range(v):
            a[i][j] = min(a[i][j], a[i][k] + a[k][j])

print("Shortest distance matrix:")
for i in range(v):
    print(*a[i])

