from itertools import permutations

def generate_combinations(digits):
    digit_list = list(digits)
    combinations = list(permutations(digit_list, len(digit_list)))
    return combinations

digits = input("Enter 3 digits: ")
combinations = generate_combinations(digits)
print("All possible combinations:", combinations)
