#li=[1,2,3,4,5]
li = list(map(int,input("enter arr: ").split()))
leng = len(li)
for i in range(leng-1,-1,-1):
    
    print(li[i])
#instead of iterating the through the entire list straight forward
#iterate from behind and just print.
#instead of the starting from 0, start from leng-1 because array
#starts from 0. start at leng-1 and end at -1, because you need
#the last (first element from the array to be printed to).
#increment step by step and rev without using function.s