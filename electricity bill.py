units = int(input("Enter the number of units consumed: "))

if units < 100:
    amount = 20
elif units <= 200:
    amount = 20 + (units - 100) * 3
elif units <= 400:
    amount = 20 + 300 + (units - 200) * 5
elif units <= 500:
    amount = 20 + 300 + 1000 + (units - 400) * 7
else:
    amount = 20 + 300 + 1000 + 700 + (units - 500) * 10

print("Your electricity bill is: Rs.", amount)
