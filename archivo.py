numero_entero = 5
numero_flotante = 3.1416
tipo_cadena = "Hola Mundo otra vez"
tipo_bool = "false"

print(numero_entero, numero_flotante, tipo_cadena, tipo_bool)


#Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
# Descubrimiento: Los enteros no tienen límite de tamaño
# Descubrimiento: Los números de punto flotante se representan en el hardware de computadoras como fracciones en base 2 (binarias)
# Descubrimiento: La mínima precisión de los float es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308



#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable

def suma_n_numeros_pares(n):
    suma = n * (n + 1)
    return suma

# Pedir al usuario que ingrese el valor de n
n = int(input("Ingresa un número entero para 'n': "))

# Llamar a la función para calcular la suma de los primeros n números pares
resultado = suma_n_numeros_pares(n)

# Mostrar el resultado
print(f"La suma de los primeros {n} números pares es: {resultado}")

