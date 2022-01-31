def factorial(num):
    if num == 0 or type(num) != int:
        return f'{num} has no factorial'
    x = 1
    for i in range(2,num+1):
        x *= i 
    return f'The factorial of {num} is {x}' 

