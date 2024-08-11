class OperacionesTextos:
    def ingreso(self, texto1, texto2, texto3):
        self.texto1 = texto1
        self.texto2 = texto2
        self.texto3 = texto3
        
    def longitudes(self):
        longitud = len(self.texto1) + len(self.texto2) + len(self.texto3)
        print("El promedio de las longitudes es = ",longitud / 3)
    
    def concatenaciones(self):
        concatenacion = self.texto1 + self.texto2 + self.texto3
        length = len(concatenacion)
        if length > 15:
            print("El largo es mayor a 15")
        elif length < 15:
            print("El largo es menor a 15")
        else:
            print("El largo es igual a 15")
        
    def caracteres(self):
        largo = {self.texto1: len(self.texto1), self.texto2: len(self.texto2), self.texto3: len(self.texto3)}
        print("El texto con más caracteres es = ",max(largo, key=largo.get))
    
    def cantidades(self):
        cantidad = len(self.texto1) + len(self.texto2) + len(self.texto3)
        print("La cantidad de caracteres existentes entre los textos es = ",cantidad)
