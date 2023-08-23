def sumsquare(l):
    odd_sum = 0
    even_sum = 0
    
    for num in l:
        if num % 2 == 0: 
            even_sum += num ** 2
        else:
            odd_sum += num ** 2
    
    return [odd_sum, even_sum]

input_str = input("Enter a list of integers separated by commas: ")
input_list = [int(x) for x in input_str.split(",")]
result = sumsquare(input_list)
print(result)  
