numbers = []
for i in range(int(input("Enter the number of elements in the list: "))):
    numbers.append(int(input(f"Enter element at position {i + 1}: ")))
print("Entered list:", numbers)

top_three = []
for num in numbers:
    if len(top_three) < 3:
        top_three.append(num)
        top_three.sort()
    else:
        if num > top_three[0]:
            top_three[0] = num
        elif num > top_three[1]:
            top_three[1] = num
        elif num > top_three[2]:
            top_three[2] = num
print(f"The third largest element is {top_three[0]}.")
