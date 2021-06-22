class algoritmo_1:
    def __init__(self, pi=3.1415):
        self.pi = pi

    def area_circ(self):
        radio = float(input("Ingrese el radio del circulo: "))
        superficie = self.pi * (radio**2)
        print("La superficie del circulo es {}" .format(superficie))


circulo = algoritmo_1()
circulo.area_circ()
