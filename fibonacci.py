n = int(input('Dijite el numero de elementos: '))

x = 0
y = 1
z = 1
print(end='1 ')
for i in range(n-1):
    z = x+y
    print(z, end=' ')
    x=y
    y=z

print('')
