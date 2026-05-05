
li=list(map(int,input("enter array: ").split()))
li2 = []
for current in li:
    count=0
    for compare in li:
        if current < compare:
            count = count + 1
    rank = count+ 1
    li2 = li2+[rank]
print(li2)