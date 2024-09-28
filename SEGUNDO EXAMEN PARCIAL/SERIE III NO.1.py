#1.Elaborar una funcion que reciba tres enteros y nos retorne el valor promedio de los mismos

def calcular_promedio(num1, num2, num3):
    "Calcula el promedio de tres números enteros."
    return (num1 + num2 + num3) / 3

def main():
    entero1 = int(input("Ingrese el primer entero: "))
    entero2 = int(input("Ingrese el segundo entero: "))
    entero3 = int(input("Ingrese el tercer entero: "))

    promedio = calcular_promedio(entero1, entero2, entero3)


    print("El promedio de los tres enteros es:", promedio)

if __name__ == "__main__":
    main()
