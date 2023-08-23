def add_binary(a, b):
    carry = 0
    result = []   
    i = len(a) - 1
    j = len(b) - 1    
    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0        
        carry, sum = divmod(digit_a + digit_b + carry, 2)        
        result.append(str(sum))        
        i -= 1
        j -= 1 
    return "".join(result[::-1])

a = input("Enter the first binary string: ")
b = input("Enter the second binary string: ")
result = add_binary(a, b)
print("Sum as a binary string:", result)
