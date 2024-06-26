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




Python calculator : The program is created in the following steps :-
1 : Define Functions: Addition, Subtraction, Multiplication, and Division
2 : Promoting Input from the user
3 : Choosing which operation to perform
4 : Return the output based on the operation being choosen .
5 : Display the output . 
6(optional) : Create a loop under which you can ask user whether operation to be continued or stop . 




Rock Paper Scissors Game : To build the Rock paper scissors python game, we will divide the problem statement into three simple steps to help us build the game.

The steps are as follows:

1 : Take the input from the user to know their choice (rock, paper or scissors).
2 : Randomly allow the computer to choose its choice.
3 : Based on the game rules, decide the winner .
4 : Display the winner on the screen.
5 : Ask the User to continue the game or stop the game . 
