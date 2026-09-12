print(30*"-")
print(30*"-")
print("Calculadora de suma y resta")
print(30*"-")
print(30*"-")


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

int1 = int(input("Ingrese el primer número: "))
int2 = int(input("Ingrese el segundo número: "))    


print("La suma es:", suma(int1, int2))
print("La resta es:", resta(int1, int2))


def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

print("La multiplicación es:", multiplicacion(int1, int2))
print("La división es:", division(int1, int2))