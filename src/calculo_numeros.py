from exceptions import ingrese_numero, NumeroDebeSerPositivo

def main():
    """
    Programa principal que solicita números al usuario y muestra los resultados.
    """
    while True:
        
            numero = ingrese_numero()
            print(f"Número válido: {numero}")

            break

if __name__ == "__main__":
    main() 