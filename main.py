def numeroParaAdivinar():
    n = int(input("Ingrese el numero a adivinar: "))
    return n

def adivinando(numero):
    NumeroSecreto = str(numero)
    l = "0123456789"
    NumeroOculto = ""
    for i in NumeroSecreto:
        if i in l:
            NumeroOculto += "*"
    NumeroOculto = str(NumeroOculto)
    #print(NumeroSecreto)
    print("")
    print("Adivine el siguiente numero:", NumeroOculto)
    print("")
    busqueda(NumeroSecreto, NumeroOculto)

def busqueda(NumeroSecreto, NumeroOculto):
    n = str(input("Ingrese un numero para adivinar: "))
    if n in NumeroSecreto:
        print("entra al IF")
        NumeroOculto = reemplazo(NumeroSecreto, NumeroOculto, n)
        print(NumeroOculto)
    else:
        print(f"{n} No esta en el numero")
        print("Intente de nuevo!")
        print("")
        busqueda(NumeroSecreto, NumeroOculto)

def reemplazo (str1, str2, n):
    lista1 = list(str1)
    lista2 = list(str2)
    for i in lista1:
        try:
            indice = str1.index(n)
            print(lista2)
            lista2.pop(indice)
            lista2.insert(indice, n)
            print(lista1)
            print(lista2)
        except ValueError:
            print("Error")
            break
    #lista2[int(i)] = lista1[int(i)]


if __name__ == "__main__":
    adivinando(numeroParaAdivinar())

