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
