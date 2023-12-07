nombre = int(input ("Cuntos partdios ganó tu equipo ? :"))
nombre_2 = int(input ("Cuntos partdios perdió tu equipo ? :"))
nombre_3 = int(input ("Cuntos partdios empató tu equipo ? :"))

suma = nombre + nombre_2 + nombre_3

a = 3
b = 0
c = 1

resultado_gana = (nombre * a)
resultado_empate = (nombre_3 * c)

promedio = resultado_gana + resultado_empate
resultado = promedio / suma

print(f"Partido jugados =  {suma}")

print(f"Puntos totales = {promedio}")

print(f"Promedio del equipo = {resultado}")