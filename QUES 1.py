n=int(input("Enter the number to check whether it is perfect or not:"))
def perfect_number(n):
    sum = 0
    
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(n))
