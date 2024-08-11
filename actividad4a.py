class OperacionesAnimales:
    nombre = ""
    edad = 0

    def sonidos(self):
        print("Sonido de animal")

class OperacionesPerro(OperacionesAnimales):
    nombre = ""
    edad = 0
    raza = ""

    def sonidos(self):
        print("Ladrido")

    def pelotas(self):
        print("Mi perro",self.nombre,"de",self.edad,"años y raza",self.raza,"está trayendo la pelota")
