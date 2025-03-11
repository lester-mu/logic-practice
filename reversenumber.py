"""
def invertirCadena(cadena):
    reverse = ""
    for caracter in cadena:
        reverse = caracter + reverse
    return reverse

x = int(input('Enter a number: '))
y = str(x)
print(invertirCadena(y))

"""

y = int(input("enter a number: "))
x = str(y)
print(x[::-1])


