print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# solicita una opción al usuario
opcion = int(input("Ingresa el número de la operación que deseas realizar (1-4): "))

# pide dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# verifica la opción y realiza la operación
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

# muestra el resultado
if resultado is not None:
    print(f"El resultado de la {operacion} es: {resultado}")
else:
    print("No se pudo calcular el resultado.")
