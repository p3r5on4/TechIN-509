# 5! = 5 x 4 x 3 x 2 x 1
## Establish the variables 
## user enters number to find factorial for as integer instead of string form
number = int(input('Enter the Number:'))
## intialized factorial to = 1 instead of auto zero variable
factorial = 1
## if conditional statement to check that number is not a negative number
if (number < 0):
    print('Cant compute negative numbers')
## additonal condition of integer number is less than two because the factorial of 1 is 1
elif(number < 2):
    ## {} place holder for number and factorial variable also will print the values of 0 and 1
    print('{}! = {}'.format(number, factorial))
## passed both conditions and is what will be performed on variable number
else:
    ## for loop run in a range from number to 1 and decrease by -1 num = new variable
    for num in range(number,1, -1):
        ##num starts at number then will decrease by 1 all the way down to 1
        ##this changes the factorial to change through the loop
        factorial = factorial * num
    ## exit loop
    print('{}! = {}'.format(number, factorial))

## if four was the input it would fail the first if and elif, then go into the else block.

## for the num = variable in the range (starting with input number, end at 1, and decrease by 1):
## then it will perform factorial (1) *num which is 4 for the first loop then 4 is stored as the factorial(4,1,-1)
## in the second loop iteration 4= factorial variable num value will be 3 
## factorial 