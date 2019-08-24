import os


def clear(): return os.system("cls")


def main():
    mensaje = ""
    try:
        texto = input(f"Ingrese el texto: ")
        resultado = ""
        for c in texto:
            transformado = f"{c}"
            if c.lower() == 'a' or c.lower() == 'á':
                transformado += "fa"
            elif c.lower() == 'e' or c.lower() == 'é':
                transformado += "fe"
            elif c.lower() == 'i' or c.lower() == 'í':
                transformado += "fi"
            elif c.lower() == 'o' or c.lower() == 'ó':
                transformado += "fo"
            elif c.lower() == 'u' or c.lower() == 'ú' or c.lower() == 'ü':
                transformado += "fu"
            resultado += transformado
        mensaje = f"La traducción es: {resultado}"
    except Exception as e:
        mensaje = f"Error detectado: {e}"
    return mensaje


if __name__ == "__main__":
    reiniciar = 's'
    while reiniciar != 'n':
        clear()
        print(f"{main()}")
        reiniciar = input(f"\n¿Desea reiniciar (s/n)? ")
