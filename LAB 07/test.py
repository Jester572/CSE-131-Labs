def sumTheDigits(number):
    total = 0
    length = len(str(number))
    for i in range(length):
        total += number % 10
        number = number // 10
    return total



def sum_the_digits_iteratively(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number = number // 10
    return sum

print(sumTheDigits(15152))
print(sum_the_digits_iteratively(15152))
def fibonacci(number):
    ''' Find the number-th Fibonacci number '''
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
print(fibonacci(6))



F(6)= F(5)  +                                                          F(4)                  
    = F(4)  +                                  F(3) +                  F(3) +                F(2)
    = F(3)  +                  F(2) +          F(2) +         F(1) +   F(2) +        F(1) +  F(1) + F(0)
    = F(2)  +         F(1) +   F(1) +  F(0) +  F(1) + F(0) +    1  +   F(1) + F(0) +   1  +    1  +   0
    = F(1)  + F(0)  +   1  +     1  +    0  +    1  +   0  +    1  +     1  +   0  +   1  +    1  +   0
    =   1   +   0   +   1  +     1  +    0  +    1  +   0  +    1  +     1  +   0  +   1  +    1  +   0
    = 8