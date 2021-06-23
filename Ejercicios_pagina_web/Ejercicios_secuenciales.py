# ESTRUCTURAS CICLICAS
class EstructuraSecuenciales:
    def __init__(self):
        pass
    
    def Secuencial_1(self):
        subtotal = float(input("Ingrese el total de la compra: "))
        Descuento = subtotal * 0.15
        total = subtotal-Descuento
        print("El total de la compra es {}, su valor a pagar es {}" .format(subtotal, total))
    
    def Secuencial_2(self):
        Sueldo_Base = float(input("Ingrese su sueldo base: "))
        v1 = float(input("Ingrese el valor de su primera venta: "))
        v2 = float(input("Ingrese el valor de su segunda venta: "))
        v3 = float(input("Ingrese el valor de su tercera venta: "))
        V = v1+v2+v3
        Comision = V*0.1
        Total_pagar = Sueldo_Base+Comision
        print("Su sueldo base es {}, mas las ventas realizadas {}, usted recibirá un total {}" .format(Sueldo_Base, V, Total_pagar))

Secuencia = EstructuraSecuenciales()
Secuencia.Secuencial_1()
Secuencia.Secuencial_2()
