# Ecuacion cinematica de caida libre
# vf = vo + gt
# y = yo + vot + 1/2gt^2
# vf^2 = vo^2 + 2gy

# Donde:
# v = velocidad final
# u = velocidad inicial
# a = aceleracion (gravedad = 9.8 m/s^2)
# t = tiempo
# s = desplazamiento

u = 0  # Velocidad inicial en m/s
a = 9.80  # Aceleracion debida a la gravedad en m/s^2
t = 5  # Tiempo en segundos

v = u + a * t
s = u * t + 0.5 * a * t**2

print("Velocidad final (v):", v, "m/s")
print("Desplazamiento (s):", s, "m")