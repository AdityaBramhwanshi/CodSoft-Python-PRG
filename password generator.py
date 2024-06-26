import string
import random
while True:
    character = string.ascii_letters + string.digits + string.punctuation
    length = int(input("Enter the length of the password: "))
    password = ''.join(random.choices(character, k=length))
    print("Your password is:", password)
    next = input("Generate Again ? (yes/no): ")
    if next == "no":
          break
    else:
         print()   