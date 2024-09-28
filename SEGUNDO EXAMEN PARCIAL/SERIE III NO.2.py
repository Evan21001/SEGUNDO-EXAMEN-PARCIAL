#2. confeccionar una funcion de calcule la superficie de un ractangulo y laretorne, la funcion recibe
#como parametros los valores de dos de sus lados; en el bloque principal del programa cargar los lados 
#de dos rectangulos y luego mostrar cual de los dos tiene suna superficie mayor



def calcular_superficie(lado1, lado2):
    "Calcula la superficie de un rectángulo."
    return lado1 * lado2

def main():
    lado1_rectangulo1 = float(input("Ingrese el primer lado del primer rectángulo: "))
    lado2_rectangulo1 = float(input("Ingrese el segundo lado del primer rectángulo: "))

    lado1_rectangulo2 = float(input("Ingrese el primer lado del segundo rectángulo: "))
    lado2_rectangulo2 = float(input("Ingrese el segundo lado del segundo rectángulo: "))

    superficie_rectangulo1 = calcular_superficie(lado1_rectangulo1, lado2_rectangulo1)
    superficie_rectangulo2 = calcular_superficie(lado1_rectangulo2, lado2_rectangulo2)

    if superficie_rectangulo1 > superficie_rectangulo2:
        print("El primer rectángulo tiene una superficie mayor:", superficie_rectangulo1)
    elif superficie_rectangulo2 > superficie_rectangulo1:
        print("El segundo rectángulo tiene una superficie mayor:", superficie_rectangulo2)
    else:
        print("Ambos rectángulos tienen la misma superficie:", superficie_rectangulo1)

if __name__ == "__main__":
    main()
