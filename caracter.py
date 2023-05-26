def tipo_string(x):
    if ord(x) >= 65 and ord(x) <= 90:
        print("El valor ingresado es una letra mayuscula")
    elif ord(x) >= 97 and ord(x) <= 122:
        print("El valor es una letra miniscula")
    elif ord(x) >= 49 and ord(x) <= 57:
        print("El valor es un numero")
    else:
        print("El valor es un caracter especial")