from modulo_estructuras import Lista
from connections_generator import generate_connections
import random

def probabilidad(ingrese_probabilidad):
    proba = int(ingrese_probabilidad)+1
    numero = random.randint(1,100)
    for i in range(1,proba):
        if i == numero:
            return True
    else:
        return False

class Pais:
    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = poblacion
        self.poblacion_infectada = 0
        self.poblacion_muerta = 0
        self.conexiones_tierra = Lista()
        self.conexiones_aire = Lista()
        self.aeropuerto = None
        self.mascarillas = False
        self.frontera = True
        self.cura = False


    def __str__(self):
        return str(self.nombre)

    @property
    def estatus(self):
        if self.poblacion_infectada == 0 and self.poblacion_muerta == 0:
            return "limpio"
        elif self.poblacion_infectada > 0 and self.poblacion_muerta < self.poblacion:
            return "infectado"
        elif self.poblacion_muerta >= self.poblacion:
            return "muerto"

    def propuestas(self):
        pass

    def entregar_mascarillas(self):
        if self.poblacion_infectada >= (self.poblacion/3):
            return True
        else:
            return False

    def cerrar_aeropuerto(self):
        if self.poblacion_infectada >= self.poblacion*0.8 or self.poblacion_muerta >= self.poblacion*0.2:
            return True
        else:
            return False


    def cerrar_frontera(self):
        if self.poblacion_infectada >= self.poblacion*0.5 or self.poblacion_muerta >= self.poblacion*0.25:
            return True
        else:
            return False



class Mundo:
    def __init__(self):
        pass


class Infeccion:
    def __init__(self, tipo, contagiosidad, mortalidad, resistencia_medicina, visibilidad):
        self.tipo = tipo
        self.contagiosidad = contagiosidad
        self.mortalidad = mortalidad
        self.resistencia_medicina = resistencia_medicina
        self.visibilidad = visibilidad


class Archivos:
    def __init__(self):
        pass


class Aeropuerto():
    def __init__(self, nombre, conexion):
        self.nombre = nombre
        self.estado = "abierto"
        self.conexiones = Lista()
        self.agregar_conexion(conexion)

    def agregar_conexion(self, pais):
        self.conexiones.append(pais)

    def __str__(self):
        return self.nombre + ":" + str(self.conexiones)


class Pandemic:
    def __init__(self):
        self.lista_paises = Lista()
        self.infeccion = None
        print("Menu:\n1 : Nueva Partida\n2 : Cargar Partida")
        iniciar = False
        while not iniciar:
            opcion = input("Ingrese alguna opcion: ")
            try:
                val = int(opcion)
                opcion = int(opcion)
                if opcion == 1:
                    iniciar = True
                    self.nueva_partida()
                elif opcion == 2:
                    iniciar = True
                    self.cargar_partida()
                else:
                    print("opcion no valida")
            except ValueError:
                print("opcion no valida")
        self.menu()

    def cargar_partida(self):
        pass

    def nueva_partida(self):
        self.cargar_archivos_basicos()
        entrar = False
        while not entrar:
            tipo = input("Ingrese el tipo de infeccion(virus,bacteria,parasito): ")
            if tipo == "virus":
                self.infeccion = Infeccion(tipo, 1.5, 1.2, 1.5, 0.5)
                entrar = True
            elif tipo == "bacteria":
                self.infeccion = Infeccion(tipo, 1.0, 1.0, 0.5, 0.7)
                entrar = True
            elif tipo == "parasito":
                self.infeccion = Infeccion(tipo, 0.5, 1.5, 1.0, 0.45)
                entrar = True
            else:
                print("Opcion no valida")
        entrar1 = False
        while not entrar1:
            print("Ingrese el pais donde desea partir la infeccion")
            pais_elegido = input("ingrese 0 para ver lista de paises: ")
            if str(pais_elegido) == "0":
                for pais in self.lista_paises:
                    print(pais)
            else:
                for paises in self.lista_paises:
                    if pais_elegido == paises.nombre:
                        paises.poblacion_infectada += 1
                        entrar1 = True
                        break

    def cargar_archivos_basicos(self):
        generate_connections()
        with open("population.csv") as archivo:
            for linea in archivo:
                separar = linea.strip("\n").split(",")
                lista_buena = Lista(*separar)
                if lista_buena[0] == "Pais":
                    None
                else:
                    pais = Pais(lista_buena[0], lista_buena[1])
                    self.lista_paises.append(pais)
        with open("borders.csv") as archivo:
            for linea in archivo:
                separar = linea.strip("\n").split(";")
                lista_buena = Lista(*separar)
                nombre = lista_buena[0]
                if nombre == "Pais 1":
                    None
                else:
                    borde = lista_buena[1]
                for pais in self.lista_paises:
                    if nombre == pais.nombre:
                        pais.conexiones_tierra.append(borde)
        with open("random_airports.csv") as archivo:
            for linea in archivo:
                separar = linea.strip("\n").split(",")
                lista_buena = Lista(*separar)
                nombre = lista_buena[0]
                conexion = lista_buena[1]
                for elemento in self.lista_paises:
                    if nombre == elemento.nombre:
                        if elemento.aeropuerto == None:
                            elemento.aeropuerto = Aeropuerto(nombre, conexion)
                        else:
                            elemento.aeropuerto.agregar_conexion(conexion)
    def menu(self):
        self.pasar_dia()
        for i in self.lista_paises:
            print(i.poblacion_infectada)

    def pasar_dia(self):
        for pais in self.lista_paises:
            if pais.mascarillas:
                mod = 0.3
            else:
                mod = 1
            pais.poblacion_infectada += pais.poblacion_infectada*random.randint(0,6)*mod


juego = Pandemic()