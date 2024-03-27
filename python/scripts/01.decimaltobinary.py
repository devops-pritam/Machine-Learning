def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2)
        num = num//2
    for j in binaryArray:
        print(j, end="")


decimal_num = 9
convertBinary(decimal_num)

#one line code
# print(bin(9)[2:])
