# Ejercicio 19: Flowchart: Total with VAT

# === CÓDIGO PARA PEGAR EN PSEINT Y GENERAR EL DIAGRAMA ===
# Algoritmo TotalConIVA
#     Definir precio, iva, total Como Real
#     
#     Escribir "Ingresa el precio:"
#     Leer precio
#     
#     iva <- precio * 0.16
#     total <- precio + iva
#     
#     Escribir "El total con IVA es: ", total
# FinAlgoritmo
# =========================================================

# Código funcional 
precio = float(input("Ingresa el precio: "))
iva = precio * 0.16
total = precio + iva
print("El total con IVA es:", total)
