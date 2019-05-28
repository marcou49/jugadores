import json

class Jugadores():
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo

class Basket(Jugadores):

    def __init__(self, nombre, edad, equipo, puntos, rebotes):
        super().__init__(nombre=nombre, edad=edad, equipo=equipo)
        self.puntos = puntos
        self.rebotes = rebotes

class Futbol(Jugadores):

    def __init__(self, nombre, edad, equipo, goles, asistencias):
        super().__init__(nombre=nombre, edad=edad, equipo=equipo)
        self.goles = goles
        self.asistencias = asistencias

LJ = input("Equipo de Lebron James ")
KL = input("Equipo de Kawhi leonard ")
ZZ = input("Equipo de Zinedine Zidane ")
DAM = input("Equipo de Maradona ")

Player_1 = Basket(nombre="Lebron James", edad=32, puntos=30, rebotes=8, equipo=LJ)
Player_2 = Basket(nombre="Kawhi Leonard", edad=30, puntos=22, rebotes=7, equipo=KL)
Player_3 = Futbol(nombre="Diego Armando Maradona", edad=57,  goles=30, asistencias=8, equipo=ZZ)
Player_4 = Futbol(nombre="Zinedine Zidane", edad=47, goles=22, asistencias=20, equipo=DAM)

uno = Player_1.__dict__

with open("jugadores.txt", "w") as listap:
    listap.write(json.dumps(uno))


