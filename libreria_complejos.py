def suma_complejos(numero1, numero2):
    """ funcion para sumar numeros complejos """

    a = numero1[0] + numero2[0]
    b = numero1[1] + numero2[1]

    c = [a, b]
    
    return c

def multiplicacion_complejos(numero1, numero2):
    """ funcion para multiplicar numeros complejos """

    a = (numero1[0] * numero2[0]) - (numero1[1] * numero2[1])
    b = (numero1[0] * numero2[1]) - (numero1[1] * numero2[0])

    c = [a, b]
    
    return c

def divicion_complejos(numero1, numero2):
    """ funcion para dividir  numeros complejos """

    a = ((numero1[0] * numero2[0]) - (numero1[1] * numero1[1]))/numero2[0]**2 - (numero2[1]**2*-1)
    b = ((numero1[0] * numero2[1]) + (numero1[1] * numero2[1]))/numero2[0]**2 - (numero2[1]**2*-1)

    c = [a, b]
    
    return c

def resta_complejos(numero1, numero2):
    """ funcion para sumar numeros complejos """

    a = numero1[0] - numero2[0]
    b = numero1[1] - numero2[1]

    c = [a, b]
    
    return c

def modulo_complejos(numero1):
    """ funcion para obtener el modulo de ub numero complejo """

    a = (numero1[0]**2 + numero1[1]**2)**(1/2)

    c = a
    
    return c

def conjugado_complejos(numero1):
    """ funcion para sumar numeros complejos """

    a = numero1[0]
    b = numero1[1]

    c = [a, -b]
    
    return c


def main():

    print("este programa puede realiar operaciones basicas con numeros complejos")
    print("para usarlo debe indicar el numero de la operacion que desea realizar")
    print("Suma = 1")
    print("Producto = 2")
    print("Resta = 3")
    print("División = 4")
    print("Módulo = 5")
    print("Conjugado = 6") 
    print("luego debe introducir el numero comlejo primero la parte real y luego l aimaginaria")

    num = int(input("ingrese el numero de la operacion que desea realizar"))

    numero1 = []
    numero2 = []

    if num == 1:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)

        c = suma_complejos(numero1, numero2)
    elif num == 2:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)
        
        c = multiplicacion_complejos(numero1, numero2)
    elif num == 3:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)
        
        c = resta_complejos(numero1, numero2)
    elif num == 4:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)

        c = divicion_complejos(numero1, numero2)
    elif num == 5:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)
        c = modulo_complejos(numero1)
    elif num == 6:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)
        c = conjugado_complejos(numero1)
        
    print(numero1)
    print(numero2)
    
    print (c)
    
