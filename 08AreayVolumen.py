# Programa 1: Cálculo del área y volumen de una esfera
import math

def esfera_area_volumen(radio):
    area = 4 * math.pi * radio**2
    volumen = (4/3) * math.pi * radio**3
    return area, volumen

radio_esfera = float(input("Introduce el radio de la esfera: "))
area_esfera, volumen_esfera = esfera_area_volumen(radio_esfera)
print(f"Área de la esfera: {area_esfera:.2f}")
print(f"Volumen de la esfera: {volumen_esfera:.2f}")

# --------------------------------------------

# Programa 2: Cálculo del área y volumen de un cilindro
def cilindro_area_volumen(radio, altura):
    area = 2 * math.pi * radio * (radio + altura)
    volumen = math.pi * radio**2 * altura
    return area, volumen

radio_cilindro = float(input("\nIntroduce el radio del cilindro: "))
altura_cilindro = float(input("Introduce la altura del cilindro: "))
area_cilindro, volumen_cilindro = cilindro_area_volumen(radio_cilindro, altura_cilindro)
print(f"Área del cilindro: {area_cilindro:.2f}")
print(f"Volumen del cilindro: {volumen_cilindro:.2f}")

# --------------------------------------------

# Programa 3: Cálculo del área y volumen de un cono truncado
def cono_truncado_area_volumen(radio_menor, radio_mayor, altura):
    generatriz = math.sqrt((radio_mayor - radio_menor)**2 + altura**2)
    area = math.pi * (radio_menor + radio_mayor) * generatriz + math.pi * (radio_menor**2 + radio_mayor**2)
    volumen = (1/3) * math.pi * altura * (radio_menor**2 + radio_menor * radio_mayor + radio_mayor**2)
    return area, volumen

radio_menor_cono = float(input("\nIntroduce el radio menor del cono truncado: "))
radio_mayor_cono = float(input("Introduce el radio mayor del cono truncado: "))
altura_cono = float(input("Introduce la altura del cono truncado: "))
area_cono, volumen_cono = cono_truncado_area_volumen(radio_menor_cono, radio_mayor_cono, altura_cono)
print(f"Área del cono truncado: {area_cono:.2f}")
print(f"Volumen del cono truncado: {volumen_cono:.2f}")

