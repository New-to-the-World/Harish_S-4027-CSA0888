def calculate_price(num_loaves):
    regular_price = num_loaves * 185
    discount = regular_price * 0.60
    total_price = regular_price - discount
    return regular_price, discount, total_price

num_loaves = int(input("Enter the number of day-old bread loaves: "))
regular_price, discount, total_price = calculate_price(num_loaves)
print(f"Regular Price: {regular_price:.2f} rupees")
print(f"Discount: {discount:.2f} rupees")
print(f"Total Price: {total_price:.2f} rupees")
