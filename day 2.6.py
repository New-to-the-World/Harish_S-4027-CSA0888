def letter_combinations(digits):
    if not digits:
        return []
    mapping = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }
    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            result.append(combination)
        else:
            for letter in mapping[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
    result = []
    backtrack("", digits)
    return result

digits = input("Enter the digits (2-9): ")
result = letter_combinations(digits)
print("Letter combinations:", result)
