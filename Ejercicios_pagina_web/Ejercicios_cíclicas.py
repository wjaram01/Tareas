class EstructuraCiclicas:     
    def __init__(self):
        pass
    
    # ESTRUCTURAS FOR
    def Ciclo_For(self):
        acumulador = 0
        for i in range(0, 100):
            acumulador += i
            i += 1
        print("La suma de los 100 primeros números es: {}".format(acumulador))

    #CICLOS ANIDADOS
    def Ciclos_For2(self):
        num = int(input("Ingrese un número: "))
        fact = 1
        for i in range(1, num+1):
            fact *= i
        print("El factorial del número {} es: {}" .format(num, fact))
    
    #ESTRUCTURAS WHILE CONTROLADO POR CONTADOR
    def Bucle_while(self):
        i = 1
        while i <= 100:
            print("Presentación de los números:")
            print(i)
            i += 1

         #BUCLE WHILE CONTROLADO POR CONDICION
    def Bucle_while2(self):
        suma = 0
        prod = 1
        res = "S"
        while res == "S":
            n = int(input("Ingrese un número: "))
            suma = suma + n
            pro = prod * n
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(prod))
            print("Desea continuar [S/N]:  ")
            res = input().capitalize()

    #BUCLE CONTROLADO POR CONDICION #2
    def Bucle_while3(self):
        suma = 0
        prod = 1
        n = 0
        while n != -1:
            n = int(input("Ingrese un número: "))
            suma = suma + n
            prod = prod*n
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(prod))
            print("")

    # BUCLE CONTROLADO POR BANDERAS O INTERRUPTORES
    def Bucle_while4(self):
        primo = True
        divisor =2
        num= int(input("Ingrese un número: "))
        while divisor < num and primo == True:
            res = num % divisor
            if res == 0:
                primo = False
            divisor += 1
        if primo == True:
            print("El número {} es primo" .format(num))
        else:
            print("El número {} no es primo" .format(num))
    
    #ESTRUCTURAS REPEAT
    def Bucle_while5(self):
        I = 1
        serie = 0
        num = int(input("Ingrese un número: "))
        band =True
        while band:
            if band == True:
                serie = serie+(1/I)
                band = False
            else:
                serie = serie-(1/I)
                band = True
            I += 1
            if I > num:
                break
            print("El resultado de la serie es: {}" .format(serie))


ciclo = EstructuraCiclicas()
ciclo.Ciclo_For()
ciclo.Ciclos_For2()
ciclo.Bucle_while()
ciclo.Bucle_while2()
ciclo.Bucle_while3()
ciclo.Bucle_while4()
ciclo.Bucle_while5()
