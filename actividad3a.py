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
