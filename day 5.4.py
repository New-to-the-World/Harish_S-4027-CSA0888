def isDivisible(prod, _sum):
    return prod % _sum == 0

test_cases = int(input("Enter the number of test cases: "))
for _ in range(test_cases):
    a, b = map(int, input("Enter two integers separated by space: ").split())
    prod = a * b
    _sum = a + b
    if isDivisible(prod, _sum):
        print("YEAH")
    else:
        print("NAH")
