# Programa 1: Esfera
PI = 3.1416
r = float(input("Radio de la esfera: "))
a_esfera = 4 * PI * r**2
v_esfera = (4/3) * PI * r**3
print(f"\nÁrea esfera: {a_esfera:.2f}")
print(f"Volumen esfera: {v_esfera:.2f}\n")

# --------------------------------------------

# Programa 2: Cilindro
r = float(input("Radio del cilindro: "))
h = float(input("Altura del cilindro: "))
a_cilindro = 2 * PI * r * (r + h)
v_cilindro = PI * r**2 * h
print(f"\nÁrea cilindro: {a_cilindro:.2f}")
print(f"Volumen cilindro: {v_cilindro:.2f}\n")

# --------------------------------------------

# Programa 3: Cono truncado
r1 = float(input("Radio menor del cono truncado: "))
r2 = float(input("Radio mayor del cono truncado: "))
h = float(input("Altura del cono truncado: "))
g = ((r2 - r1)**2 + h**2)**0.5  # Generatriz
a_cono = PI * (r1 + r2) * g + PI * (r1**2 + r2**2)
v_cono = (1/3) * PI * h * (r1**2 + r1 * r2 + r2**2)
print(f"\nÁrea cono truncado: {a_cono:.2f}")
print(f"Volumen cono truncado: {v_cono:.2f}\n")
