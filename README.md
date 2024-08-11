Ejemplos de POO con Python

Nombre: Luis Angel López Roman
Carnet: 201906107

Solución de los siguientes problemas:
1. Solicitar 3 textos y realizar lo siguiente:
• Mostrar el promedio de las longitudes de los textos.
• Concatenar los textos e indicar si el largo es mayor, menor o igual a 15.
• Indicar cuál de los textos posee más caracteres.
• Concatenar los textos e indicar la cantidad de caracteres numéricos existentes.

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

from actividad1a import OperacionesTextos

ope = OperacionesTextos()
print("Actividad 1")
ope.texto1 = input("Ingrese el primer texto: ")
ope.texto2 = input("Ingrese el segundo texto: ")
ope.texto3 = input("Ingrese el tercer texto: ")
ope.longitudes()
ope.concatenaciones()
ope.caracteres()
ope.cantidades()


2. Realizar los siguientes cálculos para un empleado del departamento de ventas:
• Comisión por ventas (10% del total vendido)
• Monto para pagar de IGSS (4.83% del sueldo base)
• Ahorro (7% del total ganado)
• Total ganado = sueldo base + comisión por ventas + bonificación.
• Total descuentos = ahorro + IGSS.
• Sueldo liquido = Total ganado – total descuentos.

class OperacionesVentas:
    sueldo = 0.0
    vendido = 0.0
    bonificacion = 0.0
            
    def comisiones(self):
        comision = self.vendido * 0.10
        print("La comisión por ventas es de = Q",comision)

    def igss(self):
        monto = (self.sueldo * 4.83) / 100
        print("El monto a pagar de IGSS es de = Q",monto)

    def totales(self):
        total = self.sueldo + self.vendido + self.bonificacion
        print("Total ganado = Q",total)

    def ahorros(self):
        ahorro = (self.sueldo + self.vendido + self.bonificacion) * 0.07
        print("Total ahorrado = Q",ahorro)

    def descuentos(self):
        igss = (self.sueldo * 4.83) / 100
        total = self.sueldo + self.vendido + self.bonificacion
        ahorro = (self.sueldo + self.vendido + self.bonificacion) * 0.07
        descuento = igss + ahorro
        print("Total descuento = Q",descuento)

    def sueldos(self):
        igss = (self.sueldo * 4.83) / 100
        total = self.sueldo + self.vendido + self.bonificacion
        ahorro = (self.sueldo + self.vendido + self.bonificacion) * 0.07
        descuento = igss - ahorro
        sueldo_liquido = total - descuento
        print("Total Sueldo Líquido = Q",sueldo_liquido)

from actividad2a import OperacionesVentas

ope = OperacionesVentas()
print("Actividad 2")
ope.sueldo = float(input("Ingrese el sueldo base: "))
ope.vendido = float(input("Ingrese el total vendido: "))
ope.bonificacion = float(input("Ingrese la bonificación: "))
ope.comisiones()
ope.igss()
ope.totales()
ope.ahorros()
ope.descuentos()
ope.sueldos()


3. Solicitar 1 valor numérico de base 10 y realizar lo siguiente: • Calcular y mostrar factorial del valor
ingresado
• Indicar si el número es primo.
• Indicar si el número es perfecto.
• Convertir el número a binario
• Mostrar la serie de Fibonacci hasta el valor ingresado.

class OperacionesNumeros:
    valor = 0
    factorial = 0

    def factoriales(self):
        if self.valor < 0:
            print()
        factorial = 1
        for i in range(2, self.valor + 1):
            factorial *= i
        print("El factorial es =",factorial)

    def primos(self):
        if self.valor <= 1:
            print("El número no es primo")
        if self.valor == 2:
            print("El número es primo")
        if self.valor % 2 == 0:
            print("El número no es primo")
        for i in range(3, int(self.valor**0.5) + 1, 2):
            if self.valor % i == 0:
                print("El número no es primo")
            else:
                print("El número es primo")

    def perfectos(self):
        if self.valor < 2:
            print("El número no es perfecto")
        suma = 1
        for i in range(2, int(self.valor*00.5) + 1):
            if self.valor % i == 0:
                suma += i
                if i != self.valor // i:
                    suma += self.valor // i
        suma == self.valor
        print("El número es perfecto")

    def binarios(self):
        binario = bin(self.valor)[2:]
        print(self.valor,"en binario es =",binario)

from actividad3a import OperacionesNumeros

ope = OperacionesNumeros()
print("Actividad 3")
ope.valor = int(input("Ingrese un valor numérico de base 10: "))
ope.factoriales()
ope.primos()
ope.perfectos()
ope.binarios()


4. Ejemplo de Herencia

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

from actividad4a import OperacionesAnimales
from actividad4a import OperacionesPerro

ope = OperacionesPerro()
ope.nombre=input("Nombre: ")
ope.edad=int(input("Edad: "))
ope.raza=input("Raza: ")
ope.sonidos()
ope.pelotas()
