
def mostrar_cuadrado():
    numero = int(input("Ingresa un número entero por favor: "))
    print(f"El cuadrado de {numero} es {numero ** 2}")

def mostrar_producto():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    print(f"El producto de {num1} y {num2} es {num1 * num2}")


if __name__ == "__main__":
    mostrar_cuadrado()
    mostrar_producto()


