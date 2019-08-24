import os


def clear(): return os.system("cls")


def main():
    mensaje = ""
    try:
        numero = input(f"Ingrese un número: ")
        resultado = 0
        for i in range(1, int(numero)+1):
            resultado += i
        mensaje = f"La suma de números desde 1 hasta {numero} es: {str(resultado)}."
    except Exception as e:
        mensaje = f"Error detectado: {e}"
    return mensaje


if __name__ == "__main__":
    reiniciar = 's'
    while reiniciar != 'n':
        clear()
        print(f"{main()}")
        reiniciar = input(f"\n¿Desea reiniciar (s/n)? ")
