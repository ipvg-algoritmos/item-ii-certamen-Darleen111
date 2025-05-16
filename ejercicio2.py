# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código


for i in range(cantidad_nota):
    nota = float(input(f"ingresa nota {i + 1}: "))
    notas.append(nota)

if cantidad_nota > 0:
    resultado = sum(notas) / cantidad_nota
    print(f"El promedio de las notas es: {resultado}")
else:
    print("No se ingresaron notas.")
