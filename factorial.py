n = int(input('Enter a number: '))
fact = 1
for i in range(1, n+1):
    print(f"{i}!")
    fact *=i
print(f'the sume of factorial ({n}) is equal to {fact}')
