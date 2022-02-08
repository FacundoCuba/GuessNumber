import random

def numeroParaAdivinar():
    n = input("Ingrese la cantidad de digitos del numero a adivinar: ")
    if n.isdigit():

        digitos = 10**int(n)
        numero_secreto = random.randint(digitos/10, digitos)
        #print(numero_secreto)
        return numero_secreto
    else:
        print("Intente ingresar un numero")
        print("Pruebe de nuevo")
        numeroParaAdivinar()

def adivinando(numero):
    NumeroSecreto = str(numero)
    l = "0123456789"
    NumeroOculto = ""
    for i in NumeroSecreto:
        if i in l:
            NumeroOculto += "*"
    NumeroOculto = str(NumeroOculto)
    print("")
    print("Adivine el siguiente numero:", NumeroOculto)
    print("")
    if NumeroSecreto != NumeroOculto:
        busqueda(NumeroSecreto, NumeroOculto)
    else:
        print(NumeroOculto)

def busqueda(NumeroSecreto, NumeroOculto):
    if NumeroSecreto != NumeroOculto:
        n = str(input("Ingrese un numero para adivinar: "))
        if n in NumeroSecreto:
            reemplazo(NumeroSecreto, NumeroOculto, n)
        elif n not in NumeroSecreto:
            print(f"{n} No esta en el numero")
            print("Intente de nuevo!")
            print("")
            busqueda(NumeroSecreto, NumeroOculto)
    elif NumeroSecreto == NumeroOculto:
        print(f"El numero es {NumeroOculto}")

def reemplazo (str1, str2, n):
    lista2 = list(str2)
    while True:
        indice = str1.index(n)
        lista2.pop(indice)
        lista2.insert(indice, n)
        str2 = ListaAString(lista2)
        print(str2)
        if str1 == str2:
            print("Adivinado!")
            quit()
        elif str1 != str2:
            busqueda(str1, str2)

def ListaAString(l):
    str1 = ""
    for i in l:
       str1 += i
    return str1

if __name__ == "__main__":
    adivinando(numeroParaAdivinar())

