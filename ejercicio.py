class Mamifero:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def moverse(self):
        print(f"{self.nombre} se está moviendo.")

class Perro(Mamifero):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

    def traer(self, objeto):
        print(f"{self.nombre} trae el {objeto}.")

# Crear un objeto de la clase Perro
mi_perro = Perro("Rex", 5, "Pastor Alemán")

# Usar métodos de la clase Perro
mi_perro.comer()
mi_perro.dormir()
mi_perro.moverse()
mi_perro.ladrar()
mi_perro.traer("palo")

# Mostrar información del perro
print(f"Nombre: {mi_perro.nombre}")
print(f"Edad: {mi_perro.edad} años")
print(f"Raza: {mi_perro.raza}")
print(f"Tipo: {mi_perro.tipo}")