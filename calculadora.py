def mostrar_menu():
    """
    Función para mostrar el menú de opciones de la calculadora.
    """
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def realizar_operacion(opcion, num1, num2):
    """
    Función para realizar la operación seleccionada por el usuario.
    Maneja operaciones básicas y verifica errores como división por cero.
    """
    if opcion == 1:
        resultado = num1 + num2
        operacion = "suma"
    elif opcion == 2:
        resultado = num1 - num2
        operacion = "resta"
    elif opcion == 3:
        resultado = num1 * num2
        operacion = "multiplicación"
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            operacion = "división"
        else:
            resultado = None
            operacion = "división"
            print("Error: No se puede dividir entre cero.")
    else:
        resultado = None
        operacion = "ninguna"
        print("Error: Opción inválida.")
    return resultado, operacion

# Inicio del programa con una estructura repetitiva
while True:
    mostrar_menu()
    try:
        # Solicita una opción al usuario
        opcion = int(input("Ingresa el número de la operación que deseas realizar (1-5): "))

        if opcion == 5:
            # Salir del programa
            print("Saliendo del programa.")
            break
        
        # Solicita los números al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Realiza la operación seleccionada
        resultado, operacion = realizar_operacion(opcion, num1, num2)

        # Muestra el resultado
        if resultado is not None:
            print(f"El resultado de la {operacion} es: {resultado}")
        else:
            print("No se pudo calcular el resultado.")

    except ValueError:
        # Manejo de error en caso de que el usuario ingrese un valor no válido
        print("Error: Por favor, ingresa un número válido.")
