lst = []
num_elements = int(input("Enter number of list elements:\t"))
for i in range(num_elements):
    lst.append(int(input("Enter element at position {i + 1}:\t")))
print("List:\t", lst)


for x in lst:
    if x%2==0:
      even_list = [x];  

print("Even numbers are " + str(even_list))
