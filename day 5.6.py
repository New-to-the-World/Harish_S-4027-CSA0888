def generate_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]  
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j] 
    return triangle

def sum_of_nth_row(triangle, n):
    return sum(triangle[n - 1])

n = int(input("Enter the value of n: "))
pascals_triangle = generate_pascals_triangle(n)
sum_of_row = sum_of_nth_row(pascals_triangle, n)
print("Pascal's Triangle:")
for row in pascals_triangle:
    print(row)
print("Sum of elements in the nth row:", sum_of_row)
