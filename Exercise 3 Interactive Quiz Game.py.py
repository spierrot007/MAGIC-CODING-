# Defining the purpose, and the name of our Game using multiple comments
# Athor's name and the version of the Game
'''
The purpose of Super Heroes Game is to make it interactive and user-friendly.

Author: Pierrot 
Game: Heroes
Version: 1.0

© Pierrot Y. SIMONETTI (2021). All right reserved.

'''
# Print welcome message

message=('Welcome to the world of Heroes, Super Man') 
print(message)

# User name input function

name = input("Enter your name:")

# Assign values to the variables

score = 0;
q_count = 0;

# Q1 information:

question1 = "Q1. Waht is the hottest month in UK ?";
choices1  = "\na. January \nb. August \nc. December";

prompt_question1 = question1 + choices1;
answer1 = "b";

user_in = input(prompt_question1 + "\n\nEnter your answer: ")
print()

if user_in == answer1:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCorrect answer. You got {0} points!!".format(score))

else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. You got {0} points!!".format(score))

# Q2 information:

question2 = "Q2. Waht is the bigest country in the world ?";
choices2  = "\na. China \nb. Rusia \nc. Canada";

prompt_question2 = question2 + choices2;
answer2 = "b";

user_in = input(prompt_question2 + "\n\nEnter your answer: ")
print()

if user_in == answer2:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCorrect answer. You got {0} points!!".format(score))

else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. You got {0} points!!".format(score))

# Q3 information:

question3 = "Q3. In which continent from the richest person in History ?";
choices3  = "\na. America \nb. Europe \nc. Africa ";

prompt_question3 = question3 + choices3;
answer3 = "c";

user_in = input(prompt_question3 + "\n\nEnter your answer: ")
print()

if user_in == answer3:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCorrect answer. You got {0} points!!".format(score))

else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. You got {0} points!!".format(score))

# Q4 information:

question4 = "Q4. where is locate the city of Rome ?";
choices4 = "\na. North Italy \nb. South Italy \nc. Central Italy ";

prompt_question4 = question4 + choices4;
answer4 = "c";

user_in = input(prompt_question4 + "\n\nEnter your answer: ")
print()

if user_in == answer4:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCorrect answer. You got {0} points!!".format(score))

else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. You got {0} points!!".format(score))

# Q5 information:

question5 = "Q5. What is the capital city of Rwanda ?";
choices5 = "\na. Bujumbura \nb. Kigali \nc. Nairobi ";

prompt_question5 = question5 + choices5;
answer5 = "b";

user_in = input(prompt_question5 + "\n\nEnter your answer: ")
print()

if user_in == answer4:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCorrect answer. You got {0} points!!".format(score))

else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. You got {0} points!!".format(score))

if score >= 40:
    print("\n\nYou got {0} points in total. You won. Bravo, you're such a pro Super Man!".format(score))
else:
    print("\n\nYou got {0} points in total. You lost. Aww, so close, Super Man. Try harder next time!".format(score))

message=('\nWould you like to play again ?')
print(message)

input('Enter your response here: ')
