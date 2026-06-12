def registrar_mascota():
    """Solicita los datos de la mascota mediante el teclado."""
    print("--- Registro de Mascota ---")
    
    # Captura de datos individuales mediante variables locales
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    edad = input("Ingrese la edad de la mascota en años: ")
    
    # Se devuelven los datos para que puedan ser utilizados en otras partes del programa
    return nombre, especie, edad

def mostrar_informacion(nombre, especie, edad):
    """Muestra la información de la mascota de forma organizada."""
    print("\n--- Información Registrada ---")
    
    # Uso de f-strings para estructurar la salida de texto de forma ordenada
    print(f"Nombre:  {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad:    {edad} año/s")
    
def main():
    
    # Flujo principal del programa
    # 1. Llamada a la función de registro y asignación de los valores retornados
    
    nombre, especie, edad = registrar_mascota()
    
    # 2. Transmisión de las variables a la función encargada de mostrar el reporte
    
    mostrar_informacion(nombre, especie, edad)

# Punto de entrada estándar en Python para asegurar que el script
# Solo se ejecute si es el archivo principal y no al ser importado.

if __name__ == "__main__":
    main()