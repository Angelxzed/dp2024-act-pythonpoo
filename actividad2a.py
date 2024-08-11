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
