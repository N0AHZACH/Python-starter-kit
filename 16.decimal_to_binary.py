decimal=int(input("enter n: "))
binary=""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal//2
print(binary)

#a decimal number is first decimal%2 which yields the first result.
#for eg: 2%2=0 which is the first number. Then the decimal gets halved
#this halving results in the process obtaining the 
# decimal equvalenet - highest 2^.
#thus filling from units digit to the highest digit.
