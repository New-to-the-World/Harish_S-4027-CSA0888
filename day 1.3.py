def is_happy(n):
    visited = set()    
    while n != 1:
        if n in visited:
            return False
        visited.add(n)      
        n_str = str(n)
        n = sum(int(digit)**2 for digit in n_str)
    return True

num = int(input("Enter a positive integer: "))
if is_happy(num):
    print(f"{num} is a happy number!")
else:
    print(f"{num} is not a happy number.")
