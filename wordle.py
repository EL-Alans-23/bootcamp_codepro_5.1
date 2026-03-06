def obtener_filas_verificadas(palabra_encontrar, palabra_ingresada):
    cantidad_de_letras_encontrar = 5

    letras_verificadas = []

    for posicion in range(cantidad_de_letras_encontrar):

        if palabra_ingresada[posicion] == palabra_encontrar[posicion]:
            letras_verificadas.append('[' + palabra_ingresada[posicion] + ']')

        elif palabra_ingresada[posicion] in palabra_encontrar:
            letras_verificadas.append('(' + palabra_ingresada[posicion] + ')')

        else:
            letras_verificadas.append(palabra_ingresada[posicion])

    return letras_verificadas
intentos = 0

while intentos < 4:
    respuesta = obtener_filas_verificadas('gatoo', (input('ingrese la palabra: ')))
    print(respuesta)
    intentos = intentos + 1

print('ya no quedan intentos')

#corregir el bug de letras repetidas en la palabra