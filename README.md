Password Generator is a program that will generate strong random passwords of the specified length with the help of the alphabet, numbers, and symbols . 
We will mainly use the random module - A built-in Python module to generate random objects. We will utilize various methods of the random module in order to randomly select the letters of the password from the list of alphabets, numbers, and symbols .
STEPS :
1 : We need set of characters from which we want to create the password. We can do this by concatenating the constants from the string module:
    character = string.ascii_letters + string.digits + string.punctuation
    This will create a string that contains all the ASCII letters, digits, and punctuation marks.
2 : Then we need to set the lenght of the random password to be generated .
3 : After taking the length of the password, we can generate a password of the desired length using the function of the choice from the random module:
    password = ''.join(random.choices(all_characters, k=length))

The choices function takes two arguments: a sequence of items to choose from and the number of items. We pass the all_characters string and the password length as       arguments in this case. The function returns a list of randomly selected characters, which we combine into a single string using the join method.

4 : In the next step your random password will be generated and you can display is using print funtion . 
    print(password)
