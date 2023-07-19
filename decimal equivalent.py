def binToDec(binNum):
    decNum = 0
    power = 0
    while binNum>0:
        decNum += 2 **power* (binNum%10)
        binNum //=10
        power += 1
    return decNum
binary_num = input("Enter number in Binary Format: ");
 
decimal_num = int(binary_num, 2);
 
print(binary_num,"in Decimal =",decimal_num);
