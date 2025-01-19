choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
result = ""
for char in text:
    if char.isalpha():  
        new_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
        if char.isupper():
            new_char = new_char.upper()
        result += new_char
    else:
        result += char  
print(result)
