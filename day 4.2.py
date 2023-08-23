student_users = int(input("Enter the number of student users: "))
total_users = int(input("Enter the total number of users: "))
staff_users = int(input("Enter the number of staff users: "))
non_teaching_staff_users = staff_users // 3
total_users += non_teaching_staff_users
print("\nStudent Users:", student_users)
print("Total Users (including non-teaching staff):", total_users)
print("Staff Users:", staff_users)
print("Non-Teaching Staff Users:", non_teaching_staff_users)
