def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0    
    while left < right:
        h = min(height[left], height[right])  
        width = right - left
        area = h * width
        max_area = max(max_area, area)  
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1    
    return max_area

height_str = input("Enter a list of heights separated by spaces: ")
height = [int(x) for x in height_str.split()]
print("Maximum Area:", max_area(height))
