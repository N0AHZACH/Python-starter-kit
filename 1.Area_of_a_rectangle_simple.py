l,b = map(int,input("separated by space: ").split())
#since there are 2 inputs being taken here - we need to use split
#so as to understand that it is 2 different values and not 1 value.
#since there is 2 values we use map to "map" the string to integer so that
#so that we can actually do math operations with it. map here is needed.
print(l*b)