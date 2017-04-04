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
        self.propuestas = Lista()
        self.dato_infecciones = 0
        self.dato_muertes = 0
        self.resumen = Lista()
        self.datos_dia = Lista()
        self.datos_dia.append("dia: 0, infectados: 1, muertos: 0")

    def buscar_cura(self, visibilidad):
        probabilidad_detectar = visibilidad * self.poblacion_mundial_infectada * (self.poblacion_mundial_muerta ** 2)
        probabilidad_detectar = probabilidad_detectar / (self.poblacion_mundial ** 3)
        return probabilidad(probabilidad_detectar)

    def trabajar_cura(self):
        progreso = self.poblacion_mundial - (self.poblacion_mundial_infectada + self.poblacion_mundial_muerta)
        progreso = progreso / (self.poblacion_mundial * 2)
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
        return (contador / self.poblacion_mundial) * 100
    @property
    def poblacion_mundial_muerta_porcen(self):
        contador = 0
        for pais in self.lista_paises:
            contador += pais.poblacion_muerta
        return (contador / self.poblacion_mundial) * 100

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

    @property
    def porcentaje_infectados(self):
        return (self.poblacion_infectada / self.poblacion) * 100

    def entregar_mascarillas(self):
        if not self.mascarillas:
            if self.poblacion_infectada >= (self.poblacion / 3):
                return True
            else:
                return False

    def cerrar_aeropuerto(self):
        if self.aeropuerto:
            if self.aeropuerto.estado:
                if self.poblacion_infectada >= self.poblacion * 0.8 or self.poblacion_muerta >= self.poblacion * 0.2:
                    return True
        return False

    def cerrar_frontera(self):
        if self.frontera:
            if self.poblacion_infectada >= self.poblacion * 0.5 or self.poblacion_muerta >= self.poblacion * 0.25:
                return True
        return False

    def abrir_aeropuerto(self):
        if self.aeropuerto:
            if not self.aeropuerto.estado:
                if self.cura:
                    return True
                if self.poblacion_infectada < (self.poblacion * 0.8) and self.poblacion_muerta < (self.poblacion * 0.2):
                    return True
        return False

    def abrir_frontera(self):
        if not self.frontera:
            if self.poblacion_infectada < (self.poblacion * 0.5) and self.poblacion_muerta < (self.poblacion * 0.25):
                return True
            else:
                return False
        return False


class Infeccion:
    def __init__(self, tipo, contagiosidad, mortalidad, resistencia_medicina, visibilidad):
        self.tipo = tipo
        self.contagiosidad = contagiosidad
        self.mortalidad = mortalidad
        self.resistencia_medicina = resistencia_medicina
        self.visibilidad = visibilidad



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
        self.dia = 0
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
                    for pais in self.lista_paises:
                        self.mundo.lista_paises.append(pais)
                    self.lista_paises.clear()
                    self.pasar_dia()
                    self.menu()
                elif opcion == 2:
                    try:
                        self.cargar_partida()
                        iniciar = True
                        self.menu()
                    except FileNotFoundError:
                        print("\nNo hay partida guardada\n")
                else:
                    print("opcion no valida")
            except ValueError:
                print("opcion no valida")

    def cargar_partida(self):
        with open("partida_guardada.txt") as archivo:
            contador = 1
            for linea in archivo:
                if contador == 1:
                    self.dia = int(linea.strip("\n"))
                    contador += 1
                elif contador == 2:
                    separar = linea.strip("\n").split(";")
                    lista = Lista(*separar)
                    self.infeccion = Infeccion(lista[0],float(lista[1]),float(lista[2]),float(lista[3]),float(lista[4]))
                    contador +=1
                elif contador ==3:
                    separar = linea.strip("\n").split(";")
                    lista = Lista(*separar)
                    self.mundo = Mundo()
                    self.mundo.dia = int(lista[0])
                    self.mundo.detectar = bool(lista[1])
                    self.mundo.progreso= float(lista[2])
                    self.mundo.cura = bool(lista[3])
                    lista1 = Lista(*lista[4].strip("[").strip("]").split(","))
                    for i in lista1:
                        if i == "":
                            pass
                        else:
                            self.mundo.propuestas.append(i)
                    self.mundo.dato_infecciones= int(lista[5])
                    self.mundo.dato_muertes= int(lista[6])
                    lista2 = Lista(*lista[7].strip("[").strip("]").split(","))
                    for i in lista2:
                        self.mundo.resumen.append(i)
                    lista3 = Lista(*lista[8].strip("[").strip("]").split(","))
                    for i in lista3:
                        self.mundo.datos_dia.append(i)
                    contador += 1
                else:
                    separar = linea.strip("\n").split(";")
                    lista = Lista(*separar)
                    pais = Pais(lista[0],lista[1])
                    self.mundo.lista_paises.append(pais)
                    for paises in self.mundo.lista_paises:
                        if paises.nombre == lista[0]:
                            paises.poblacion_infectada =int(lista[2])
                            paises.poblacion_muerta =int(lista[3])
                            lista1 = Lista(*lista[4].strip("[").strip("]").split(";"))
                            for i in lista1:
                                paises.conexiones_tierra.append(i)
                            if lista[5] == None:
                                paises.aeropuerto = None
                            elif lista[5] != None:
                                lista2 = Lista(*lista[5].split(":"))
                                for i in lista2:
                                    lista3 = Lista(*lista2[2].strip("[").strip("]").split(","))
                                    paises.aeropuerto = Aeropuerto(lista2[0],lista3[0])
                                    for j in lista3:
                                        if j not in paises.aeropuerto.conexiones:
                                            paises.aeropuerto.conexiones.append(j)
                            paises.mascarillas = bool(lista[6])
                            paises.frontera = bool(lista[7])
                            paises.cura = bool(lista[8])
                            paises.dias_infectado = int(bool(lista[9]))


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
                                    pais.aeropuerto = Aeropuerto(conexion, nombre)
                                elif nombre not in pais.aeropuerto.conexiones:
                                    pais.aeropuerto.conexiones.append(nombre)

    def menu(self):
        self.salir = False
        while not self.salir:
            print("Menu\nDia: "+str(self.dia))
            print("1 : Pasar dia\n2 : Estadisticas\n3 : Guardar estado\n4 : Salir")
            x = input("Ingrese opcion: ")
            try:
                var = int(x)
                if var in [1,2,3,4]:
                    if var == 1:
                        self.pasar_dia()
                    elif var == 2:
                        self.estadisticas()
                    elif var == 3:
                        self.guardar_estado()
                        print("Partida guardada correctamente")
                    else:
                        self.salir = True
                        print("juego cerrado")
                else:
                    ("Numero fuera de las opciones validas")
            except ValueError:
                print("Opcion no valida, ingrese un numero")

    def pasar_dia(self):
        self.mundo.resumen.clear()
        self.mundo.dato_muertes = self.mundo.poblacion_mundial_muerta
        self.mundo.dato_infecciones = self.mundo.poblacion_mundial_infectada
        self.dia += 1
        self.mundo.dia += 1
        self.contagios_personas()
        self.arreglador()
        self.muertes()
        self.contagio_frontera_aeropuerto()
        self.buscar_cura()
        self.trabajar_en_cura()
        self.evaluar_propuestas()
        self.generar_propuestas()
        self.actuar_cura()
        self.propagar_cura()
        self.mundo.dato_muertes = self.mundo.poblacion_mundial_muerta - self.mundo.dato_muertes
        self.mundo.dato_infecciones = self.mundo.poblacion_mundial_infectada - self.mundo.dato_infecciones
        dato = "dia: {}, nuevos infectados: {}, nuevos muertos: {}".format(int(self.dia),self.mundo.dato_infecciones,self.mundo.dato_muertes)
        self.mundo.datos_dia.append(dato)

    def contagios_personas(self):
        for pais in self.mundo.lista_paises:
            if pais.poblacion > (pais.poblacion_infectada + pais.poblacion_muerta):
                if pais.mascarillas:
                    mod = 0.3
                elif not pais.mascarillas:
                    mod = 1
                if pais.poblacion_infectada > 0:
                    pais.dias_infectado += 1
                    if pais.poblacion_infectada < 100000:
                        for i in range(1, pais.poblacion_infectada + 1):
                            pais.poblacion_infectada += int(random.randint(0, 6) * mod * self.infeccion.contagiosidad)
                    else:
                        contador = pais.poblacion_infectada
                        while contador > 0:
                            if contador > 1000:
                                contador -= 1000
                                pais.poblacion_infectada += int(
                                    1000 * random.randint(0, 6) * mod * self.infeccion.contagiosidad)
                            else:
                                for persona in range(1, contador + 1):
                                    pais.poblacion_infectada += int(
                                        random.randint(0, 6) * mod * self.infeccion.contagiosidad)
                                contador = 0

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
                probabilidad_contagio = 0.9
                for vecinos in pais.conexiones_tierra:
                    if probabilidad(probabilidad_contagio):
                        for paises in self.mundo.lista_paises:
                            if vecinos == paises.nombre and paises.frontera:
                                paises.poblacion_infectada += 1
                                paises.dias_infectado += 1
            if pais.aeropuerto:
                if (
                            self.mundo.poblacion_mundial_infectada / self.mundo.poblacion_mundial) > 0.04 and pais.aeropuerto.estado:
                    probabilidad_contagio = min(1, (0.07 * pais.poblacion_infectada) / (
                        (pais.poblacion - pais.poblacion_muerta) * conexiones))
                    for vecinos in pais.aeropuerto.conexiones:
                        if probabilidad(probabilidad_contagio * 100):
                            for paises in self.mundo.lista_paises:
                                if vecinos == paises.nombre and paises.aeropuerto.estado:
                                    paises.poblacion_infectada += 1
                                    paises.dias_infectado += 1

    def arreglador(self):
        for pais in self.mundo.lista_paises:
            if pais.poblacion_infectada > pais.poblacion:
                pais.poblacion_infectada = pais.poblacion - pais.poblacion_muerta

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

    def generar_propuestas(self):
        for pais in self.mundo.lista_paises:
            try:
                prioridad = pais.poblacion_infectada / pais.poblacion
            except ZeroDivisionError:
                pass
            if pais.cerrar_aeropuerto():
                prioridad *= 0.8
                txt = "{};{};cerrar aeropuerto".format(prioridad, pais.nombre)
                self.mundo.propuestas.append(txt)
                prioridad = pais.poblacion_infectada / pais.poblacion_infectada
            if pais.cerrar_frontera():
                contador = 0
                total_infec_porcen = 0
                for conexiones in pais.conexiones_tierra:
                    for paises in self.mundo.lista_paises:
                        if paises.nombre == conexiones:
                            contador += 1
                            total_infec_porcen += paises.porcentaje_infectados
                mod = (total_infec_porcen / contador) / 100
                prioridad *= mod
                txt = "{};{};cerrar frontera".format(prioridad, pais.nombre)
                self.mundo.propuestas.append(txt)
                prioridad = pais.poblacion_infectada / pais.poblacion_infectada
            if pais.entregar_mascarillas():
                prioridad *= 0.5
                txt = "{};{};entregar mascarillas".format(prioridad, pais.nombre)
                self.mundo.propuestas.append(txt)
                prioridad = pais.poblacion_infectada / pais.poblacion_infectada
            if pais.abrir_aeropuerto():
                if pais.cura:
                    mod = 1
                else:
                    mod = 0.7
                txt = "{};{};abrir aeropuerto".format(prioridad, pais.nombre)
                self.mundo.propuestas.append(txt)
                prioridad = (pais.poblacion_infectada / pais.poblacion_infectada) * mod
            if pais.abrir_frontera():
                mod = 0.7
                prioridad = (pais.poblacion_infectada / pais.poblacion_infectada) * mod
                txt = "{};{};abrir frontera".format(prioridad, pais.nombre)
                self.mundo.propuestas.append(txt)
        self.mundo.propuestas.sort()

    def evaluar_propuestas(self):
        rango = len(self.mundo.propuestas) + 1
        for i in range(1, min(4, rango)):
            prop = self.mundo.propuestas.pop()
            separar = prop.split(";")
            lista = Lista(*separar)
            self.mundo.resumen.append(lista)
            nombre = lista[1]
            iniciativa = lista[2]
            for pais in self.mundo.lista_paises:
                if pais.nombre == nombre:
                    if iniciativa == "cerrar frontera":
                        pais.frontera = False
                    elif iniciativa == "cerrar aeropuerto":
                        pais.aeropuerto.estado = False
                    elif iniciativa == "entregar mascarillas":
                        pais.mascarillas = True
                    elif iniciativa == "abrir frontera":
                        pais.frontera = True
                    elif iniciativa == "abrir aeropuerto":
                        pais.aeropuerto.estado = True
        self.mundo.propuestas.clear()

    def actuar_cura(self):
        probabilidad_cura = (probabilidad(0.25 * self.infeccion.resistencia_medicina))
        for pais in self.mundo.lista_paises:
            if pais.cura:
                if pais.estatus != "muerto":
                    if pais.poblacion_infectada < 500000:
                        for persona in range(1, pais.poblacion_infectada + 1):
                            if probabilidad(probabilidad_cura):
                                pais.poblacion_infectada -= 1
                    elif pais.poblacion_infectada < 5000000000:
                        contador = pais.poblacion_infectada
                        while contador > 0:
                            if contador > 1000:
                                contador -= 1000
                                if probabilidad(probabilidad_cura):
                                    pais.poblacion_infectada -= 1000
                            else:
                                for persona in range(1, contador + 1):
                                    if probabilidad(probabilidad_cura):
                                        pais.poblacion_infectada -= 1
                                contador = 0

    def propagar_cura(self):
        lista = Lista()
        for pais in self.mundo.lista_paises:
            if pais.cura:
                if pais.aeropuerto:
                    for elemento in pais.aeropuerto.conexiones:
                        lista.append(elemento)
        for nombre in lista:
            for pais1 in self.mundo.lista_paises:
                if pais1.nombre == nombre:
                    if not pais1.cura:
                        pais1.cura = True

    def estadisticas(self):
        estar = True
        while estar:
            print("\nEstadisticas:\n1 : Por pais\n2 : Situacion Mundo\n3 : Promedio muertes e infecciones\n4 : Resumen sucesos dia\n5 : Muertes e infeciones por dia\n6 : volver")
            x = input("Ingrese opcion: ")
            try:
                var = int(x)
                if var in [1,2,3,4,5,6]:
                    if var == 1:
                        pais = input("ingrese pais: ")
                        for elemento in self.mundo.lista_paises:
                            if pais == elemento.nombre:
                                print("Estado: {}".format(elemento.estatus))
                                print("Poblacion inicial pais: {}".format(elemento.poblacion))
                                print("Poblacion actual: {}".format(elemento.poblacion-elemento.poblacion_muerta))
                                print("Poblacion infectada: {}".format(elemento.poblacion_infectada))
                                print("Poblacion muerta: {}".format(elemento.poblacion_muerta))
                                if elemento.frontera:
                                    print("Frontera abierta")
                                elif not elemento.frontera:
                                    print("Frontera cerrada")
                                if elemento.cura:
                                    print("Pais posee la cura")
                                if elemento.aeropuerto:
                                    if elemento.aeropuerto.estado:
                                        print("Aeropuerto abierto")
                                    else:
                                        print("Aeropuerto cerrado")
                                if elemento.mascarillas:
                                    print("Gobierno entrego mascarillas")
                                print("Propuestas: ")
                                for propuesta in self.mundo.propuestas:
                                    if len(self.mundo.propuestas)>0:
                                        if propuesta[1]==elemento.nombre:
                                            print(propuesta[2])
                    elif var == 2:
                        validar = False
                        while not validar:
                            x = input("desea ver paises limpios(1), infectados(2) o muertos(3): ")
                            try:
                                var = int(x)
                                if var in [1,2,3]:
                                    if var ==1:
                                        buscar = "limpio"
                                    elif var == 2:
                                        buscar = "infectado"
                                    elif var == 3:
                                        buscar = "muerto"
                                    for pais in self.mundo.lista_paises:
                                        if pais.estatus == buscar:
                                            print(pais)
                                    validar = True
                                else:
                                    print("opcion no valida, ingrese un numero del 1 al 3")
                            except ValueError:
                                print("opcion no valida, ingrese un numero del 1 al 3")
                        print("Poblacion mundial inicial: {}".format(self.mundo.poblacion_mundial))
                        print("Poblacion mundial actual: {}".format(self.mundo.poblacion_mundial_actual))
                        print("Poblacion mundial infectada: {}".format(self.mundo.poblacion_mundial_infectada))
                        print("Porcentaje de infectados: {}%".format(self.mundo.poblacion_mundial_infectada_porcen))
                        print("Poblacion muerta: {}".format(self.mundo.poblacion_mundial_muerta))
                        print("Porcentaje de muertos: {}%".format(self.mundo.poblacion_mundial_muerta_porcen))
                        if self.mundo.detectar:
                            print("Infeccion detectada")
                            print("Porcentaje de desarollo cura: {}".format(self.mundo.progreso))
                    elif var == 3:
                        contador = True
                        while contador:
                            x = input("Tasas:\n1 : dia\n2 : acumuladas")
                            try:
                                var = int(x)
                                if var in [1,2]:
                                    if var == 1:
                                        print("Sanos hoy: {}".format(int(self.mundo.poblacion_mundial_actual)-int(self.mundo.poblacion_mundial_infectada)))
                                        print("Infectados hoy: {}".format(self.mundo.dato_infecciones))
                                        print("Muertos hoy: {}".format(self.mundo.dato_muertes))
                                    elif var == 2:
                                        print("Poblacion muerta hasta la fecha: {}".format(self.mundo.poblacion_mundial_muerta))
                                        print("Poblacion infectada hasta la fecha: {}".format(
                                            self.mundo.poblacion_mundial_infectada))
                                    contador = False


                            except ValueError:
                                print("Opcion incorrecta, ingrese 1 o 2")

                    elif var == 4:
                        print("Infectados hoy: {}".format(self.mundo.dato_infecciones))
                        print("Muertos hoy: {}".format(self.mundo.dato_muertes))
                        for pais in self.mundo.lista_paises:
                            if pais.poblacion_infectada == 1:
                                print("{} fue infectado".format(pais.nombre))
                        for lista in self.mundo.resumen:
                            pais = lista[1]
                            accion = lista[2]
                            print("{} hizo la accion de: {}".format(pais,accion))
                    elif var == 5:
                        for dato in self.mundo.datos_dia:
                            print(dato)
                    else:
                        estar = False


                else:
                    print("Error, ingrese un numero dentro de las opciones")
            except ValueError:
                print("Error, ingrese un numero")

    def guardar_estado(self):
        with open("partida_guardada.txt","w") as archivo:
            txt = str(self.dia)+"\n"
            archivo.write(txt)
            txt = str(self.infeccion.tipo)+";"
            txt += str(self.infeccion.contagiosidad)+";"
            txt += str(self.infeccion.mortalidad)+";"
            txt += str(self.infeccion.resistencia_medicina)+";"
            txt += str(self.infeccion.visibilidad)+"\n"
            archivo.write(txt)
            txt = str(self.mundo.dia)+";"
            txt += str(self.mundo.detectar)+";"
            txt +=str(self.mundo.progreso)+";"
            txt += str(self.mundo.cura)+";"
            txt += str(self.mundo.propuestas)+";"
            txt += str(self.mundo.dato_infecciones)+";"
            txt += str(self.mundo.dato_muertes)+";"
            txt += str(self.mundo.resumen)+";"
            txt +=str(self.mundo.datos_dia)+"\n"
            archivo.write(txt)
            for pais in self.mundo.lista_paises:
                txt = pais.nombre+";"
                txt +=str(pais.poblacion)+";"
                txt +=str(pais.poblacion_infectada)+";"
                txt +=str(pais.poblacion_muerta)+";"
                txt +=str(pais.conexiones_tierra)+";"
                if pais.aeropuerto == None:
                    txt +=None+";"
                else:
                    txt += pais.aeropuerto.nombre+":"
                    txt += str(pais.aeropuerto.estado)+":"
                    txt += str(pais.aeropuerto.conexiones) + ";"
                txt +=str(pais.mascarillas)+";"
                txt +=str(pais.frontera)+";"
                txt +=str(pais.cura)+";"
                txt +=str(pais.dias_infectado)+"\n"
                archivo.write(txt)







juego = Pandemic()
