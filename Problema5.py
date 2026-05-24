# -----------------------------------------
# Programa: Control de horas trabajadas
# Autor: Sheyla Vanessa Torrealba Banquet
# Curso: Fundamentos de Programación
# -----------------------------------------

# Matriz con nombre y horas trabajadas
recursos = [
    ["Carlos", 8, 8, 9, 8, 10],
    ["Ana", 7, 8, 7, 8, 7],
    ["Luis", 9, 9, 8, 9, 9],
    ["María", 8, 8, 8, 8, 8]
]

# Función para calcular horas y clasificación
def calcular_horas(horas):
    
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Mostrar resultados
print("CONTROL DE HORAS SEMANALES")
print("----------------------------------")

for recurso in recursos:

    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_horas(horas)

    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("----------------------------------")