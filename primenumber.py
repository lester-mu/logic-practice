num = int(input('Enter a number: '))

is_prime = True

for i in range(2,num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"The number ({num}) is prime")
else:
    print(f"The number ({num}) is not prime")
