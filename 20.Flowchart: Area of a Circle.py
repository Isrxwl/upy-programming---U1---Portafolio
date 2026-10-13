# Ejercicio 20: Flowchart: Area of a Circle

# === CÓDIGO PARA PEGAR EN PSEINT Y GENERAR EL DIAGRAMA ===
# Algoritmo AreaYCircunferencia
#     Definir radio, area, circunferencia Como Real
#     
#     Escribir "Ingresa el radio del circulo:"
#     Leer radio
#     
#     area <- PI * (radio ^ 2)
#     circunferencia <- 2 * PI * radio
#     
#     Escribir "El area es: ", area
#     Escribir "La circunferencia es: ", circunferencia
# FinAlgoritmo
# =========================================================

# Código funcional en Python para que el script sea válido en la revisión:
import math

radio = float(input("Ingresa el radio del circulo: "))
area = math.pi * (radio ** 2)
circunferencia = 2 * math.pi * radio

print("El area es:", area)
print("La circunferencia es:", circunferencia)
