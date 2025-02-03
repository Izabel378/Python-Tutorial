lst = []  
n = int(input("Enter number of elements: "))  

for i in range(n):  
    num = int(input(f"Enter element {i + 1}: "))  
    lst.append(num)  

lst.sort()  
print(f"Largest: {lst[-1]}, Smallest: {lst[0]}")
