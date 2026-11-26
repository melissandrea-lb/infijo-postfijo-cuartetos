def infijo_a_postfijo(expresion):
    # Definición de precedencias
    precedencia = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    # Operadores asociativos a la derecha
    asociatividad_derecha = {'^'}

    pila = []
    salida = []

    # Eliminar espacios en blanco
    tokens = expresion.replace(" ", "")

    for token in tokens:

        # Caso 1: El token es un operando
        if token.isalnum():
            salida.append(token)

        # Caso 2: Paréntesis de apertura
        elif token == '(':
            pila.append(token)

        # Caso 3: Paréntesis de cierre
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())

            if pila and pila[-1] == '(':
                pila.pop()

        # Caso 4: El token es un operador
        elif token in precedencia:

            while (pila and pila[-1] != '(' and
                   (precedencia[pila[-1]] > precedencia[token] or
                   (precedencia[pila[-1]] == precedencia[token]
                    and token not in asociatividad_derecha))):

                salida.append(pila.pop())

            pila.append(token)

    # Vaciar los operadores restantes
    while pila:
        salida.append(pila.pop())

    return "".join(salida)

def generar_cuartetos(postfijo):
    pila = []
    cuartetos = []
    contador = 1
    operadores = ['+','-','*','/','^']

    for token in postfijo:
        if token not in operadores:
            pila.append(token)
        else:
            argumento2 = pila.pop()
            argumento1 = pila.pop()
            temporal = "T" + str(contador)
            contador += 1
            cuarteto = (token, argumento1,argumento2,temporal)
            cuartetos.append(cuarteto)
            pila.append(temporal)
    return cuartetos

# Pruebas de ejecución
if __name__ == "__main__":

    ejemplo = "A + B * C ^ D - E"

    resultado = infijo_a_postfijo(ejemplo)

    cuartetos = generar_cuartetos(resultado)

    print(f"Infijo: {ejemplo}")
    print(f"Postfijo: {resultado}")
    print("\nCuartetos")
    print("Nº | operador | Arg1 | Arg2 | Resultado")
    for i, c in enumerate(cuartetos, 1):
        print(f"{i:2} | {c[0]:8} |{c[1]:4}  |{c[2]:4}  |{c[3]}")
