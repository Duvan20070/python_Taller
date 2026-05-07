from Logica.mascota import Perro, Gato

def registrar_mascota():
    print("Registrar una mascota: ")
    print("Selecciona el tipo de mascota: ")
    print("1. Perro")
    print("2. Gato")

    opcion = input("Elige el tipo de mascota: ")
    nombre = input("Ingrese el nombre de tu mascota: ")
    edad = int(input("Ingrese la edad cronologica de tu mascota: "))

    if opcion == '1':
        tamaño = input("Ingrese el tamaño (Pequeño: p), (Mediano: m), (Grande: g): ")
        mi_mascota = Perro (nombre, edad, tamaño)

    elif opcion == '2':
        mi_mascota = Gato (nombre, edad)
    
    else: 
        print("Opcion invalida")
        return
    
    print(f"Has registrado a {mi_mascota} con {mi_mascota.edad_cronologica} años cronollogicos. ")
    edad_humanda = mi_mascota.calcular_edad_humana()
    print(f"La edad humana de {mi_mascota.nombre} es: {edad_humanda} años.")

    