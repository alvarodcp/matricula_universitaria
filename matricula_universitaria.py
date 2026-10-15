# Declaración de las variables.
edad = int(input("Digite la edadd del interesado: "))
esta_graduado = input("Digite si el interesado ya se graduó (s/n): ")

# Determinar el tipo de programa que puede matricular.
if edad >= 17:
    if esta_graduado == "s":
        matricula_graduado = "Bachillerato"
    else:
        matricula_graduado = "Técnico"
else:
    matricula_graduado = "Técnico"   

# impresión de la información
print(f"El programa que el interesado puede matricular es {matricula_graduado}")

