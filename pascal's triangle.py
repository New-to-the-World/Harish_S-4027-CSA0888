def generate_full_pascal_pyramid(height):
    pyramid = []
    for i in range(height):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = pyramid[i - 1][j - 1] + pyramid[i - 1][j]
        pyramid.append(row)
    max_width = len(" ".join(map(str, pyramid[-1])))
    for row in pyramid:
        spaces = " " * ((max_width - len(" ".join(map(str, row)))) // 2)
        print(spaces + " ".join(map(str, row)))

height = int(input("Enter the height of the full Pascal's pyramid: "))
generate_full_pascal_pyramid(height)
