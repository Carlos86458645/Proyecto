def numeromayor(x,y,z):
    """
    Una funcion que dados 3 numeros devuelva el max de los 3.
    """
    if x > y and x > z:
        return(x)
    elif y > x and y > z:
        return(y)
    else:
        return(z)

n1=float(input("Ingresa el primer numero"))
n2=float(input("Ingresa el segundo numero"))
n3=float(input("Ingresa el tercer numero"))
mayor=numeromayor(n1,n2,n3)
print("El numero mayor es: ", mayor)