## input value used as string value, make it an integer value
n = int(input('Enter the numeber:'))
result = 1
## establish a for loop for values in the range (beginning at n, end at 0, step down by -1)
for i in range(n , 0, -1):
## result is set to 1 previously and now multiplied by i
    result = result * i
print('factorial of', n, 'is', result)