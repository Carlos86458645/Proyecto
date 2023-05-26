print("\tUna ecuacion cuadratica es de la forma ax^2+bx+c=0,\n\tpara esto necesitamos los coeficientes a, b y c")
numeros=input("Escriba 3 numeros a b c:")
numerosl=numeros.split()
while len(numerosl) != 3:
    print("verifique el numero de variables")
    numeros=input("Escriba 3 numeros a b c:")
    numerosl=numeros.split()
a,b,c=numerosl
a,b,c=int(a),int(b),int(c)
x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
print(x1,x2)