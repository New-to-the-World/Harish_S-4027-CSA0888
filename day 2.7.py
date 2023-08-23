def generate_parentheses(n):
    def backtrack(combination, open_count, close_count):
        if len(combination) == 2 * n:
            result.append(combination)
            return
        if open_count < n:
            backtrack(combination + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(combination + ")", open_count, close_count + 1)
    result = []
    backtrack("", 0, 0)
    return result

n = int(input("Enter the number of pairs of parentheses: "))
combinations = generate_parentheses(n)
print("Parentheses combinations:", combinations)
