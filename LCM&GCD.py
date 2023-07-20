a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
HCF = 1

for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        HCF = i

LCM=(a*b)/HCF

print("First Number is: ",a)
print("Second Number is: ",b)
print("HCF of the numbers is: ",HCF)
print("LCMof the numbers is: ",LCM)
