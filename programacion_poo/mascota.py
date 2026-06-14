# DEFINICIÓN DE LA CLASE (MOLDE DE ABSTRACCIÓN)

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre     # Atributo que almacena el nombre del objeto actual
        self.especie = especie   # Atributo que almacena la especie del objeto actual
        self.edad = edad         # Atributo que almacena la edad del objeto actual

    def mostrar_informacion(self):
        """Muestra los detalles del objeto Mascota."""
        print(f"Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        """Emite un sonido genérico o específico según la especie."""
        # Un pequeño detalle extra para el método hacer_sonido
        especie_lower = self.especie.lower()
        
        # Estructura de control para personalizar la respuesta según los datos del objeto
        if especie_lower == "perro":
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif especie_lower == "gato":
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido animal.")