# FLUJO PRINCIPAL Y CREACIÓN DE OBJETOS

# Se importa la clase Mascota desde el módulo/archivo mascota.py
from mascota import Mascota

def main():
    print("--- Sistema de Gestión de Mascotas (POO) ---")
    
    # Crear al menos dos objetos de la clase Mascota
    # 1. INSTANCIACIÓN: Creación de objetos independientes usando la clase como molde.
    # Cada objeto posee su propio espacio en memoria con sus respectivos datos.
    
    mascota1 = Mascota("Brando", "Perro", "3")
    mascota2 = Mascota("JoJo", "Gato", "2")
    
    # 2. EJECUCIÓN DE MÉTODOS: Invocación del comportamiento definido en la clase.
    # Mostrar la información y ejecutar métodos para la mascota 1
    
    print("\n--- Mascota 1 ---")
    mascota1.mostrar_informacion()   # Muestra los datos específicos de mascota1
    mascota1.hacer_sonido()          # Evalúa y ejecuta el sonido de mascota1
    
    # Mostrar la información y ejecutar métodos para la mascota 2
    # Operaciones asociadas al segundo objeto
    
    print("\n--- Mascota 2 ---")
    mascota2.mostrar_informacion()   # Muestra los datos específicos de mascota2
    mascota2.hacer_sonido()          # Evalúa y ejecuta el sonido de mascota2

# Punto de entrada para la ejecución del programa

if __name__ == "__main__":
    main()