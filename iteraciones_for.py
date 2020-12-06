estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puelto lico': 4,
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)

for numero_estudiantes in estudiantes.values():
    print(numero_estudiantes)

for pais, numero_estudiantes in estudiantes.items():
    print(pais, numero_estudiantes)
