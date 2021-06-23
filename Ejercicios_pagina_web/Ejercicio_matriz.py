import numpy as np


class examenes:

    def __init__(self, prom_exam=0):
        self.exam = np.zeros((30, 6))
        self.prom_exam = prom_exam

    def Promedio_examen(self):
        for j in range(0, 6):
            for i in range(0, 30):
                nota = float(input("Ingrese la nota examen del alumno {}, de la materia {}:".format((i+1), (j+1))))
                self.exam[i, j] = nota

        # cálculo del promedio de calificaciones de cada uno de los exámenes
        self.prom_exam = []
        for j in range(0, 6):
            acum = 0
            for i in range(0, 30):
                num = self.exam[i, j]
                acum = acum + num
            prom = acum/30
            self.prom_exam.append(prom)
            print("Promedio de examenes de la materia: {}, es de {}".format(j+1, prom))
            return self.prom_exam

    def Promedio_alumno(self):
        for i in range(0, 30):
            acum = 0
            for j in range(0, 6):
                num = self.exam[i, j]
                acum = acum + num
            prom = acum/6
            print("Promedio del alumno {}, es {}".format(i, prom))

    def Puntaje_examen(self, examenes):
        Examen = 1
        mayor = examenes[0]
        for i in range(1, 6):
            if mayor < examenes[i]:
                mayor = examenes[i]
                Examen = i
        print("El examen {}, obtuvo el mayor promedio con : {}".format(Examen, mayor))


if __name__ == "__main__":
    Alumnos_masivos = examenes()
    Alumnos_masivos.Promedio_alumno()
    examenes = Alumnos_masivos.Promedio_examen()
    Alumnos_masivos.Puntaje_examen(examenes)
