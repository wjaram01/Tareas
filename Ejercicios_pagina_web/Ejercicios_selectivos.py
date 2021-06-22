# ESTRUCTURAS SELECTIVAS
class estructura_selectivas:
    def __init__(self):
        pass
    
    # ESTRUCTURAS SELECTIVAS SIMPLES
    def Selectivas1(self):
        nota = float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if nota >= 7:
            print("La nota es {}, APROBADO" .format(nota))

    # ESTRUCTURAS SELECTIVAS DOBLES
    def Selectivas2(self):
        nota = float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if nota >= 7:
            print("La nota es {}, APROBADO" .format(nota))
        else:
            print("La nota es {}, REPROBADO" .format(nota))

    def Selectivas3(self):
        Sueldo = float(input("Ingrese el sueldo: "))
        if Sueldo <= 600:
            Nuevo_Sueldo = Sueldo+(Sueldo*0.1)
            print("Su nuevo sueldo es {}" .format(Nuevo_Sueldo))
        else:
            print("Su sueldo sigue siendo {}" .format(Sueldo))

    #
    def Selectivas4(self):
        horas_trabajadas = int(input("Ingrese las horas que trabajó: "))
        pago_hora = float(input("Ingrese el pago de la hora normal: "))
        if horas_trabajadas > 40:
            horas_extra = horas_trabajadas - 40
            if horas_extra > 8:
                hora_extra_trabajada = horas_extra - 8
                pago_hora_extra = (pago_hora * 2 * 8) + (pago_hora * 3 * hora_extra_trabajada)
            else:
                pago_hora_extra = pago_hora * 2 * horas_extra
            pago_total = pago_hora * 40 + pago_hora_extra
        else:
            pago_total = pago_hora * horas_trabajadas
        print("El pago total por las horas trabajadas es {}" .format(pago_total))

    def Selectivas5(self):
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        n3 = int(input("Ingrese el tercer número: "))
        if n1 > n2 and n1 > n3:
            print("El número mayor es {}" .format(n1))
        elif n2 > n1 and n2 > n3:
            print("El número mayor es {}" .format(n2))
        else:
            print("El número mayor es {}" .format(n3))
    
    # ESTRUCTURAS SELECTIVAS MULTIPLES
    def Selectivas6(self):
        val1 = int(input("Ingrese un número: "))
        val2 = int(input("Ingrese un valor: "))
        if val1 == 1:
            res = 100 * val2
        elif val1 == 2:
            res = 100 ** val2
        elif val1 == 3:
            res = 100/val2
        else:
            res = 0
        print("El resultado del número {} y el valor {} es de: {} ".format(val1, val2, res))
    
    # EXPRESIONES LOICAS  USE DE AND
    def Selectivas7(self):
        nota1 = int(input("Ingrese la primera calificación: "))
        nota2 = int(input("Ingrese la segunda calificación: "))
        if nota1 >= 80 and nota2 >= 80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(nota1, nota2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(nota1, nota2))
    
        
Selectiva = estructura_selectivas()
Selectiva.Selectivas1()
Selectiva.Selectivas2()
Selectiva.Selectivas3()
Selectiva.Selectivas4()
Selectiva.Selectivas5()
Selectiva.Selectivas6()
Selectiva.Selectivas7()
