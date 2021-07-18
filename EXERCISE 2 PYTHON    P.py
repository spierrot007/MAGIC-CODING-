#Python program to divide two numbers

try:
    numerator=int(input('Enter to number to devide:'))

#declare and initialize a numerator variable

    denominator=int(input('Enter a number to devide by:'))

#declare and initialize denominator variable

    Result=numerator/denominator;

#Calculate the division result 

    print(Result)
    
#print the result under condition by using Except Exception function
    
except Exception:
    
    print('Error – You cannot divide by 0. Please choose an appropriate denominator.')

#display the output on the screen
