# Leap year 366 every four years last one 2020
# conditions divisible by 400
## divisible by 4 but not 100
##other wise not a leap year
year = int(input('Input a year:'))
if year %4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Is a leap year')
        else:
            print("It is not a leap year")
    else:
        print('Is a leap year')
else:
    print('Not a leap year')

    