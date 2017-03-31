from modulo_estructuras import Lista
from connections_generator import generate_connections
import random


def probabilidad(ingrese_probabilidad):
    boolean = (random.random() < float(ingrese_probabilidad))
    return boolean


class Mundo:
    def __init__(self):
        self.dia = 1
        self.lista_paises = Lista()
        self.detectar = False
        self.progreso = 0
        self.cura = False
    def buscar_cura(self,visibilidad):
        probabilidad_detectar = visibilidad*self.poblacion_mundial_infectada*(self.poblacion_mundial_muerta**2)
        probabilidad_detectar = probabilidad_detectar/(self.poblacion_mundial**3)
        return probabilidad(probabilidad_detectar)

    def trabajar_cura(self):
        progreso =self.poblacion_mundial-(self.poblacion_mundial_infectada+self.poblacion_mundial_muerta)
        progreso = progreso/(self.poblacion_mundial*2)
        self.progreso += progreso



    @property
    def poblacion_mundial(self):
        contador = 0
        for pais in self.lista_paises:
            contador += pais.poblacion
        return contador

    @property
    def poblacion_mundial_actual(self):
        return self.poblacion_mundial - self.poblacion_mundial_muerta

    @property
    def poblacion_mundial_infectada(self):
        contador = 0
        for pais in self.lista_paises:
            contador += pais.poblacion_infectada
        return contador

    @property
    def poblacion_mundial_infectada_porcen(self):
        contador = 0
        for pais in self.lista_paises:
            contador += pais.poblacion_infectada
        return (contador/self.poblacion_mundial)*100
    @property
    def poblacion_mundial_muerta(self):
        contador = 0
        for pais in self.lista_paises:
            contador += pais.poblacion_muerta
        return contador


class Pais:
    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = int(poblacion)
        self.poblacion_infectada = 0
        self.poblacion_muerta = 0
        self.conexiones_tierra = Lista()
        self.aeropuerto = None
        self.mascarillas = False
        self.frontera = True
        self.cura = False
        self.dias_infectado = 0

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
        if self.poblacion_infectada >= (self.poblacion / 3):
            return True
        else:
            return False

    def cerrar_aeropuerto(self):
        if self.poblacion_infectada >= self.poblacion * 0.8 or self.poblacion_muerta >= self.poblacion * 0.2:
            return True
        else:
            return False

    def cerrar_frontera(self):
        if self.poblacion_infectada >= self.poblacion * 0.5 or self.poblacion_muerta >= self.poblacion * 0.25:
            return True
        else:
            return False


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


class Aeropuerto:
    def __init__(self, nombre, conexion):
        self.nombre = nombre
        self.estado = True
        self.conexiones = Lista()
        self.agregar_conexion(conexion)

    def agregar_conexion(self, pais):
        self.conexiones.append(pais)

    def __str__(self):
        return self.nombre + ":" + str(self.conexiones)


class Pandemic:
    def __init__(self):
        self.dia = 1
        self.lista_paises = Lista()
        self.infeccion = None
        self.mundo = Mundo()
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
        for pais in self.lista_paises:
            self.mundo.lista_paises.append(pais)
        self.lista_paises.clear()
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
                        paises.dias_infectado += 1
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
                        if borde not in pais.conexiones_tierra:
                            pais.conexiones_tierra.append(borde)
                            for elemento in self.lista_paises:
                                if elemento.nombre == borde:
                                    elemento.conexiones_tierra.append(pais.nombre)

        with open("random_airports.csv") as archivo:
            for linea in archivo:
                separar = linea.strip("\n").split(",")
                lista_buena = Lista(*separar)
                nombre = lista_buena[0].title()
                conexion = lista_buena[1].title()
                for elemento in self.lista_paises:
                    if nombre == elemento.nombre:
                        if elemento.aeropuerto == None:
                            elemento.aeropuerto = Aeropuerto(nombre, conexion)
                        elif conexion not in elemento.aeropuerto.conexiones:
                            elemento.aeropuerto.agregar_conexion(conexion)
                        for pais in self.lista_paises:
                            if conexion == pais.nombre:
                                if pais.aeropuerto == None:
                                    pais.aeropuerto = Aeropuerto(conexion,nombre)
                                elif nombre not in pais.aeropuerto.conexiones:
                                    pais.aeropuerto.conexiones.append(nombre)

    def menu(self):
        self.salir = False
        while not self.salir:
            print(self.dia)
            for pais in self.mundo.lista_paises:
                if pais.estatus == "infectado":
                    print(pais)
                    print(pais.conexiones_tierra)
            self.pasar_dia()
            x = input("")

    def pasar_dia(self):
        self.dia += 1
        self.mundo.dia += 1
        self.contagios_personas()
        self.arreglador()
        self.muertes()
        self.contagio_frontera_aeropuerto()
        self.buscar_cura()
        self.trabajar_en_cura()

    def contagios_personas(self):
        for pais in self.mundo.lista_paises:
            if pais.poblacion > (pais.poblacion_infectada + pais.poblacion_muerta):
                if pais.mascarillas:
                    mod = 0.3
                else:
                    mod = 1
                pais.poblacion_infectada += int(pais.poblacion_infectada * random.randint(0,
                                                                                      6) * mod * self.infeccion.contagiosidad)
                if pais.poblacion_infectada > 0:
                    pais.dias_infectado += 1

    def muertes(self):
        probabilidad_muerte = (min((min(0.2, (self.dia ** 2) / 100000)) * self.infeccion.mortalidad, 1))
        for pais in self.mundo.lista_paises:
            if pais.estatus != "muerto":
                if pais.poblacion_infectada < 500000:
                    for persona in range(1, pais.poblacion_infectada + 1):
                        if probabilidad(probabilidad_muerte):
                            pais.poblacion_infectada -= 1
                            pais.poblacion_muerta += 1
                elif pais.poblacion_infectada < 5000000000:
                    contador = pais.poblacion_infectada
                    while contador > 0:
                        if contador > 1000:
                            contador -= 1000
                            if probabilidad(probabilidad_muerte):
                                pais.poblacion_infectada -= 1000
                                pais.poblacion_muerta += 1000
                        else:
                            for persona in range(1, contador + 1):
                                if probabilidad(probabilidad_muerte):
                                    pais.poblacion_infectada -= 1
                                    pais.poblacion_muerta += 1
                            contador = 0

    def contagio_frontera_aeropuerto(self):
        for pais in self.mundo.lista_paises:
            conexiones = len(pais.conexiones_tierra)
            if pais.aeropuerto:
                conexiones += len(pais.aeropuerto.conexiones)
            if (pais.poblacion_infectada / pais.poblacion) > 0.2 and pais.frontera:
                probabilidad_contagio = min(1, (0.07 * pais.poblacion_infectada) / (
                    (pais.poblacion - pais.poblacion_muerta) * conexiones))
                for vecinos in pais.conexiones_tierra:
                    if probabilidad(probabilidad_contagio):
                        for paises in self.mundo.lista_paises:
                            if vecinos == paises.nombre and paises.frontera:
                                paises.poblacion_infectada += 1
                                paises.dias_infectado += 1
            if pais.aeropuerto:
                if (self.mundo.poblacion_mundial_infectada / self.mundo.poblacion_mundial) > 0.04 and pais.aeropuerto.estado:
                    probabilidad_contagio = min(1, (0.07 * pais.poblacion_infectada) / (
                        (pais.poblacion - pais.poblacion_muerta) * conexiones))
                    for vecinos in pais.aeropuerto.conexiones:
                        if probabilidad(probabilidad_contagio*100):
                            for paises in self.mundo.lista_paises:
                                if vecinos == paises.nombre and paises.aeropuerto.estado:
                                    paises.poblacion_infectada += 1
                                    paises.dias_infectado += 1
    def arreglador(self):
        for pais in self.mundo.lista_paises:
            if pais.poblacion_infectada > pais.poblacion:
                pais.poblacion_infectada = pais.poblacion-pais.poblacion_muerta

    def buscar_cura(self):
        if not self.mundo.detectar:
            self.mundo.detectar = self.mundo.buscar_cura(self.infeccion.visibilidad)

    def trabajar_en_cura(self):
        if not self.mundo.cura:
            if self.mundo.detectar and self.mundo.progreso < 1:
                self.mundo.trabajar_cura()
                if self.mundo.progreso >= 1:
                    pais = random.choice(self.mundo.lista_paises)
                    pais.cura = True
                    self.mundo.cura = True



juego = Pandemic()
