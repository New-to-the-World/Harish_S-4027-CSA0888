def calculate_bonus(salary, grade):
    if salary < 10000:
        bonus = 0.02 * salary
    elif grade == 'A':
        bonus = 0.05 * salary
    elif grade == 'B':
        bonus = 0.10 * salary
    else:
        bonus = 0
    return salary + bonus

salary = float(input("Enter the salary: "))
grade = input("Enter the grade (A or B): ")
new_salary = calculate_bonus(salary, grade)
print("New salary after bonus:", new_salary)
