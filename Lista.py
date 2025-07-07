integrantes = [
    {"nombre": "Diego Elias", "apellidos": "Leyton Orellana"},
    {"nombre": "Felipe Ignacio", "apellidos": "Becerra Moller"}
]

print("Integrantes del grupo:")
print("======================")
for i, integrante in enumerate(integrantes, 1):
    print(f"{i}. {integrante['nombre']} {integrante['apellidos']}")