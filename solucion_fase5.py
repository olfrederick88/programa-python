# =====================================================
# Fase 5 - Evaluacion Final POA
# Problema 1: Clasificacion de compromiso de sesiones
# Autor: [Milton Jiar Arevalo Alfonso]
# Grupo: [213022_2204]
# Fecha: 23 de noviembre de 2026
# =====================================================

# ----------------------
# Datos iniciales: Matriz con al menos 5 sesiones
# Formato por fila: [ID del Cliente, Duracion (segundos), Numero de clics]
# ----------------------
sesiones = [
    [101, 240, 12],
    [102, 50, 7],
    [103, 120, 5],
    [104, 200, 6],
    [105, 45, 2]
]

# ----------------------
# Funcion que calcula la clasificacion de compromiso
# Recibe: duracion en segundos y numero de clics
# Retorna: cadena con la clasificacion
# ----------------------
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# ----------------------
# Salida: Generacion del informe
# ----------------------
print("=" * 50)
print("       INFORME DE NIVEL DE COMPROMISO")
print("=" * 50)
print(f"{'ID Cliente':<15} | {'Clasificacion':<15}")
print("-" * 50)

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    nivel = clasificar_compromiso(duracion, clics)
    print(f"{id_cliente:<15} | {nivel:<15}")

print("=" * 50)
print("Fin del informe")
