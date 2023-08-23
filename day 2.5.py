def calculate(s):
    stack = []
    num = 0
    operator = "+"
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])

        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
            if operator == "+":
                stack.append(num)
            elif operator == "-":
                stack.append(-num)
            elif operator == "*":
                stack[-1] *= num
            elif operator == "/":
                stack[-1] = int(stack[-1] / num)
            num = 0
            operator = s[i]
    return sum(stack)

expression = input("Enter the expression: ")
result = calculate(expression)
print("Result:", result)
