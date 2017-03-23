import math


# lluvia se considera el total que cayo

class Usuario:
    def __init__(self, id="", nombre="", contrasena="", recurso_id=""):
        self.id = id
        self.nombre = nombre
        self.contrasena = contrasena
        self.recurso_id = recurso_id


class Recurso:
    def __init__(self, id="", tipo="", velocidad="", lat="", lon="", autonomia="", delay="", tasa_extincion="",
                 costo=""):
        self.id = id
        self.tipo = tipo
        self.velocidad = velocidad
        self.lat = float(lat)
        self.lon = float(lon)
        self.autonomia = float(autonomia)
        self.delay = delay
        self.tasa_extincion = tasa_extincion
        self.costo = costo
        self.lat_actual = self.lat
        self.lon_actual = self.lon
        self.total_horas_trabajadas = float(0)
        self.horas_trabajadas = float(0)
        self.estado = "standby"
        self.fecha_inicio = ""
        self.fecha_llegada = "2017-02-28 00:00:00"
        self.fecha_salida_incendio = ""
        self.id_incendio_asignado = ""
        self.distancia_objetivo = 0
        self.distancia_recorrida = 0
        self.puntos_apagados = 0
        self.autonomia_restante = autonomia
        self.fecha_ultima_ejecucion = self.fecha_inicio

    def __str__(self):
        cadena = "id={}, tipo={}, velocidad={}, lat={}, lon={}, autonomia={}, delay={}, tasa_extincion={}, costo={}".format(
            self.id, self.tipo, self.velocidad, self.lat, self.lon, self.autonomia, self.delay, self.tasa_extincion,
            self.costo)
        return cadena


class Incendio:
    def __init__(self, id="", lat="", lon="", potencia="", fecha_inicio=""):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.radio = float(0)
        self.potencia = int(potencia)
        self.puntos_poder_extintos = 0
        self.fecha_inicio = fecha_inicio
        self.recursos_usados = []
        self.ultima_condicion = ""
        self.fecha_apagado = ""
        self.fecha_ultimo_recurso = self.fecha_inicio
        self.horas_ya_simuladas = []
        self.fecha_ultima_simulacion = ""

    @property
    def activo(self):
        if self.puntos_poder > self.puntos_poder_extintos:
            return "activo"
        else:
            return "apagado"

    @property
    def porcentaje_de_extincion(self):
        if self.puntos_poder != 0:
            return float(self.puntos_poder_extintos) / float(self.puntos_poder)

        else:
            return "100%"

    @property
    def puntos_poder(self):
        return (math.pi * (self.radio ** 2)) * self.potencia

    def __str__(self):
        cadena = "id: {}, lat: {}, lon : {}, potencia : {}, fecha inicio: {}".format(self.id, self.lat, self.lon,
                                                                                     self.potencia, self.fecha_inicio)
        return cadena


class Meteorologia:
    def __init__(self, id="", lat="", lon="", radio="", fecha_inicio="", fecha_termino="", tipo="", valor=""):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.valor = valor
        self.radio = radio
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.tipo = tipo


class Archivos:
    def __init__(self):
        self.primera_linea_usuarios = ""
        self.primera_linea_incendios = ""
        self.primera_linea_recursos = ""
        self.primera_linea_metereologia = ""

    def cargar_usuarios(self):
        self.lista_usuarios = []
        primera_linea = []
        llaves_columnas = []
        with open("usuarios.csv")as archivo_usuarios:
            contador = 0
            for linea in archivo_usuarios:
                if contador < 1:
                    self.primera_linea_usuarios = linea
                    primera_linea = (linea.strip("\n").split(","))
                    contador += 1
                    for columna in primera_linea:
                        llaves_columnas.append(columna.split(":")[0])
                else:
                    id_usuario = linea.strip("\n").split(",")[llaves_columnas.index("id")]
                    contrasena_usuario = linea.strip("\n").split(",")[llaves_columnas.index("contraseña")]
                    nombre_usuario = linea.strip("\n").split(",")[llaves_columnas.index("nombre")]
                    recurso_usuario = linea.strip("\n").split(",")[llaves_columnas.index("recurso_id")]
                    usuario1 = Usuario(id=id_usuario, nombre=nombre_usuario, contrasena=contrasena_usuario,
                                       recurso_id=recurso_usuario)
                    self.lista_usuarios.append(usuario1)
        return self.lista_usuarios

    def cargar_recursos(self):
        self.lista_recursos = []
        primera_linea = []
        llaves_columnas = []
        with open("recursos.csv")as archivo_recursos:
            contador = 0
            for linea in archivo_recursos:
                if contador < 1:
                    self.primera_linea_recursos = linea
                    primera_linea = (linea.strip("\n").split(","))
                    contador += 1
                    for columna in primera_linea:
                        llaves_columnas.append(columna.split(":")[0])
                else:
                    id_recurso = linea.strip("\n").split(",")[llaves_columnas.index("id")]
                    tipo = linea.strip("\n").split(",")[llaves_columnas.index("tipo")]
                    velocidad = linea.strip("\n").split(",")[llaves_columnas.index("velocidad")]
                    lat = linea.strip("\n").split(",")[llaves_columnas.index("lat")]
                    lon = linea.strip("\n").split(",")[llaves_columnas.index("lon")]
                    autonomia = linea.strip("\n").split(",")[llaves_columnas.index("autonomia")]
                    delay = linea.strip("\n").split(",")[llaves_columnas.index("delay")]
                    tasa_extincion = linea.strip("\n").split(",")[llaves_columnas.index("tasa_extincion")]
                    costo = linea.strip("\n").split(",")[llaves_columnas.index("costo")]
                    recurso1 = Recurso(id=id_recurso, tipo=tipo, lat=lat, lon=lon, autonomia=autonomia, delay=delay,
                                       tasa_extincion=tasa_extincion, costo=costo, velocidad=velocidad)
                    self.lista_recursos.append(recurso1)
        return self.lista_recursos

    def cargar_incendios(self):
        self.lista_incendios = []
        primera_linea = []
        llaves_columnas = []
        with open("incendios.csv")as archivo_incendios:
            contador = 0
            for linea in archivo_incendios:
                if contador < 1:
                    self.primera_linea_incendios = linea
                    primera_linea = (linea.strip("\n").split(","))
                    contador += 1
                    for columna in primera_linea:
                        llaves_columnas.append(columna.split(":")[0])
                else:
                    id = linea.strip("\n").split(",")[llaves_columnas.index("id")]
                    lat = linea.strip("\n").split(",")[llaves_columnas.index("lat")]
                    lon = linea.strip("\n").split(",")[llaves_columnas.index("lon")]
                    potencia = linea.strip("\n").split(",")[llaves_columnas.index("potencia")]
                    fecha_inicio = linea.strip("\n").split(",")[llaves_columnas.index("fecha_inicio")]
                    incendio1 = Incendio(id=id, lat=lat, lon=lon, potencia=potencia, fecha_inicio=fecha_inicio)
                    self.lista_incendios.append(incendio1)
        return self.lista_incendios

    def cargar_meteorologia(self):
        self.lista_meteorologia = []
        primera_linea = []
        llaves_columnas = []
        with open("meteorologia.csv")as archivo_meteorologias:
            contador = 0
            for linea in archivo_meteorologias:
                if contador < 1:
                    self.primera_linea_metereologia = linea
                    primera_linea = (linea.strip("\n").split(","))
                    contador += 1
                    for columna in primera_linea:
                        llaves_columnas.append(columna.split(":")[0])
                else:
                    id = linea.strip("\n").split(",")[llaves_columnas.index("id")]
                    tipo = linea.strip("\n").split(",")[llaves_columnas.index("tipo")]
                    lat = linea.strip("\n").split(",")[llaves_columnas.index("lat")]
                    lon = linea.strip("\n").split(",")[llaves_columnas.index("lon")]
                    radio = linea.strip("\n").split(",")[llaves_columnas.index("radio")]
                    valor = linea.strip("\n").split(",")[llaves_columnas.index("valor")]
                    fecha_inicio = linea.strip("\n").split(",")[llaves_columnas.index("fecha_inicio")]
                    fecha_termino = linea.strip("\n").split(",")[llaves_columnas.index("fecha_termino")]
                    meteorologia1 = Meteorologia(id=id, lat=lat, lon=lon, radio=radio, fecha_inicio=fecha_inicio,
                                                 fecha_termino=fecha_termino, tipo=tipo, valor=valor)
                    self.lista_meteorologia.append(meteorologia1)
        return self.lista_meteorologia

    def cargar_simulacion(self, fecha_actual, lista_recursos, lista_incendios):
        try:
            with open("datos_simulacion.txt")as archivo_simulacion:
                for linea in archivo_simulacion:
                    fecha = linea.strip("\n").split(",")[0]
                    if FechaYHora.comparar_fecha(fecha_actual, fecha):
                        for recurso in lista_recursos:
                            if "recuros" == linea.strip("\n").split(",")[1] and recurso.id == \
                                    linea.strip("\n").split(",")[1]:
                                recurso.horas_trabajadas = linea.strip("\n").split(",")[2]
                                recurso.lat_actual = linea.strip("\n").split(",")[3]
                                recurso.lon_actual = linea.strip("\n").split(",")[4]
                                recurso.id_incendio_asignado = linea.strip("\n").split(",")[5]
                        for incendio in lista_incendios:
                            if "incendio" == linea.strip("\n").split(",")[1] and incendio.id == \
                                    linea.strip("\n").split(",")[1]:
                                incendio.puntos_poder_extintos = linea.strip("\n").split(",")[2]
                                incendio.recursos_usados = linea.strip("\n").split(",")[3]
                                incendio.fecha_apagado = linea.strip("\n").split(",")[4]

        except FileNotFoundError:
            return None

    def sobreescribir_simulacion(self, lista_incendios, lista_recursos):
        archivo = open("datos_simulacion.txt", "w")
        for incendio in lista_incendios:
            fila = ""
            if len(incendio.recursos_usados) > 0:
                fila += str(incendio.id) + ";"
                fila += str(incendio.fecha_ultima_simulacion) + ";"
                fila += str(incendio.radio) + ";"
                fila += str(incendio.horas_ya_simuladas) + ";"
                fila += str(incendio.recursos_usados) + ";"
                fila += str(incendio.puntos_poder_extintos) + ";"
                fila += str(incendio.ultima_condicion) + ";"
                fila += str(incendio.fecha_apagado) + ";"
                fila += str(incendio.fecha_ultimo_recurso) + "\n"
                archivo.write(fila)
        for recursos in lista_recursos:
            fila = ""
            if recursos.total_horas_trabajadas > 0:
                fila += recursos.fecha_ultima_ejecucion + "\n"
                fila += recursos.id + ";"
                fila += recursos.lat_actual + ";"
                fila += recursos.lon_actual + ";"
                fila += recursos.total_horas_trabajadas + ";"
                fila += recursos.horas_trabajadas + ";"
                fila += recursos.estado + ";"
                fila += recursos.fecha_inicio + ";"
                fila += recursos.fecha_llegada + ";"
                fila += recursos.fecha_salida_incendio + ";"
                fila += recursos.id_incendio_asignado + ";"
                fila += recursos.distancia_objetivo + ";"
                fila += recursos.distancia_recorrida + ";"
                fila += recursos.puntos_apagados + ";"
                fila += recursos.autonomia_restante + ";"
                archivo.write(fila)
        archivo.close()

    def sobreescribir_usuarios(self, lista):
        archivo = open("usuarios.csv", "w")
        orden = self.primera_linea_usuarios.strip("\n").split(",")
        texto = ""
        for elemento in orden:
            if (elemento.split(":")[0]) == "id":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "nombre":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "contraseña":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "recurso_id":
                texto += str(elemento) + "\n"
        archivo.write(texto)
        fila = ""
        for elemento in lista:
            fila += str(elemento.id) + ","
            fila += str(elemento.nombre) + ","
            fila += str(elemento.contrasena) + ","
            fila += str(elemento.recurso_id) + "\n"
            archivo.write(fila)
            fila = ""
        archivo.close()

    def sobreescribir_incendios(self, lista):
        archivo = open("incendios.csv", "w")
        orden = self.primera_linea_incendios.strip("\n").split(",")
        texto = ""
        for elemento in orden:
            if (elemento.split(":")[0]) == "id":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "lat":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "lon":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "potencia":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "fecha_inicio":
                texto += str(elemento) + "\n"
        archivo.write(texto)
        fila = ""
        for elemento in lista:
            fila += str(elemento.id) + ","
            fila += str(elemento.lat) + ","
            fila += str(elemento.lon) + ","
            fila += str(elemento.potencia) + ","
            fila += str(elemento.fecha_inicio) + "\n"
            archivo.write(fila)
            fila = ""
        archivo.close()

    def sobreescribir_recursos(self, lista):
        archivo = open("recursos.csv", "w")
        orden = self.primera_linea_recursos.strip("\n").split(",")
        texto = ""
        for elemento in orden:
            if (elemento.split(":")[0]) == "id":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "tipo":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "velocidad":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "lat":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "lon":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "autonomia":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "delay":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "tasa_extincion":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "costo":
                texto += str(elemento) + "\n"
        archivo.write(texto)
        fila = ""
        for elemento in lista:
            fila += str(elemento.id) + ","
            fila += str(elemento.tipo) + ","
            fila += str(elemento.velocidad) + ","
            fila += str(elemento.lat) + ","
            fila += str(elemento.lon) + ","
            fila += str(elemento.autonomia) + ","
            fila += str(elemento.delay) + ","
            fila += str(elemento.tasa_extincion) + ","
            fila += str(elemento.costo) + "\n"
            archivo.write(fila)
            fila = ""
        archivo.close()

    def sobreescribir_meteorologia(self, lista):
        archivo = open("meteorologia.csv", "w")
        orden = self.primera_linea_metereologia.strip("\n").split(",")
        texto = ""
        for elemento in orden:
            if (elemento.split(":")[0]) == "id":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "fecha_inicio":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "fecha_termino":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "tipo":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "valor":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "lat":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "lon":
                texto += str(elemento) + ","
        for elemento in orden:
            if (elemento.split(":")[0]) == "radio":
                texto += str(elemento) + "\n"
        archivo.write(texto)
        fila = ""
        for elemento in lista:
            fila += str(elemento.id) + ","
            fila += str(elemento.fecha_inicio) + ","
            fila += str(elemento.fecha_termino) + ","
            fila += str(elemento.tipo) + ","
            fila += str(elemento.valor) + ","
            fila += str(elemento.lat) + ","
            fila += str(elemento.lon) + ","
            fila += str(elemento.radio) + "\n"
            archivo.write(fila)
            fila = ""
        archivo.close()


class FechaYHora:
    def __init__(self):
        self.bisiesto = False
        self.anio = 0
        self.mes = 0
        self.dia = 0
        self.hora = 0
        self.minuto = 0
        self.contador = True

    def ver_anio(self):
        self.contador = True
        while self.contador:
            anio = (input("ingrese año: "))
            try:
                val = int(anio)
                anio = int(anio)
                if self.es_biciesto(anio):
                    self.anio = anio
                    self.bisiesto = True
                    self.contador = False
                    return self.anio
                else:
                    self.bisiesto = False
                    self.anio = anio
                    self.contador = False
                    return self.anio
            except ValueError:
                print("Año no valido")

    def ver_mes(self):
        self.contador = True
        while self.contador:
            mes = (input("ingrese mes en formato numero (ej: marzo = 3): "))
            try:
                val = int(mes)
                mes = int(mes)
                meses = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
                self.mes = mes
                if int(mes) in meses:
                    self.contador = False
                    return mes
                else:
                    print("mes no valido")
            except ValueError:
                print("mes no valido")

    def ver_dia(self):
        self.contador = True
        while self.contador:
            dia = input("Ingrese dia: ")
            try:
                val = int(dia)
                dia = int(dia)
                if self.mes in [1, 3, 5, 7, 8, 10, 12]:
                    if dia in range(1, 32):
                        self.dia = dia
                        self.contador = False
                        return self.dia
                    else:
                        print("Dia no valido, debe estar entre 1:31")
                elif self.mes in [4, 6, 9, 11]:
                    if dia in range(1, 31):
                        self.dia = dia
                        self.contador = False
                        return self.dia
                    else:
                        print("Dia no valido, debe estar entre 1:30")
                elif self.mes in [2]:
                    if self.bisiesto:
                        if dia in range(1, 30):
                            self.dia = dia
                            self.contador = False
                            return self.dia
                        else:
                            print("Dia no valido, debe estar entre 1:29")
                    else:
                        if dia in range(1, 29):
                            self.dia = dia
                            self.contador = False
                            return self.dia
                        else:
                            print("Dia no valido, debe estar entre 1:28")
            except ValueError:
                print("Dia no valido")

    def ver_hora(self):
        self.contador = True
        while self.contador:
            hora = input("Ingrese hora (0:23): ")
            try:
                val = int(hora)
                hora = int(hora)
                if hora in range(0, 24):
                    if hora // 10 == 0:
                        hora = "0" + str(hora)
                    minuto = input("Ingrese minuto (0:59) ")
                    try:
                        val = int(minuto)
                        minuto = int(minuto)
                        if minuto in range(0, 59):
                            if minuto // 10 == 0:
                                minuto = "0" + str(minuto)
                            self.hora = "{0}:{1}:00".format(hora, minuto)
                            self.contador = False
                            return self.hora
                        else:
                            print("Minutos no validos")
                    except ValueError:
                        print("Minutos no validos")
                else:
                    print("hora no valida")
            except ValueError:
                print("Hora no valida")

    # Funcion para ver si fecha1 es despues de fecha2
    def comparar_fecha(fecha1, fecha2):
        fecha_1 = fecha1.split(" ")[0]
        hora_1 = fecha1.split(" ")[1]
        anio_1 = int(fecha_1.split("-")[0])
        mes_1 = int(fecha_1.split("-")[1])
        dia_1 = int(fecha_1.split("-")[2])
        minuto_1 = int(hora_1.split(":")[1])
        horaa_1 = int(hora_1.split(":")[0])
        fecha_2 = fecha2.split(" ")[0]
        hora_2 = fecha2.split(" ")[1]
        anio_2 = int(fecha_2.split("-")[0])
        mes_2 = int(fecha_2.split("-")[1])
        dia_2 = int(fecha_2.split("-")[2])
        minuto_2 = int(hora_2.split(":")[1])
        horaa_2 = int(hora_2.split(":")[0])
        if anio_1 > anio_2:
            return True
        elif anio_1 == anio_2:
            if mes_1 > mes_2:
                return True
            elif mes_1 == mes_2:
                if dia_1 > dia_2:
                    return True
                elif dia_1 == dia_2:
                    if horaa_1 > horaa_2:
                        return True
                    elif horaa_1 == horaa_2:
                        if minuto_1 >= minuto_2:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def es_biciesto(self, anio=0, **kwargs):
        if anio % 4 == 0:
            if str(anio)[-1] == "0" and str(anio)[-2] == "0":
                if anio % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def siguiente_minuto(fecha_ingresada):
        hora = fecha_ingresada.split(" ")[1]
        hora = hora.split(":")
        minuto = int(hora[1])
        hora = int(hora[0])
        fecha = fecha_ingresada.split(" ")[0]
        fecha = fecha.split("-")
        dia = int(fecha[2])
        mes = int(fecha[1])
        anio = int(fecha[0])
        if minuto < 59:
            minuto += 1
        else:
            minuto = 0
            if hora < 23:
                hora += 1
            else:
                hora = 0
                if mes in [1, 3, 5, 7, 8, 10, 12]:
                    if dia < 31:
                        dia += 1
                    else:
                        dia = 0
                        if mes < 12:
                            mes += 1
                        else:
                            anio += 1
                elif mes in [4, 6, 9, 11]:
                    if dia < 30:
                        dia += 1
                    else:
                        dia = 0
                        mes += 1
                elif mes in [2]:
                    if FechaYHora.es_biciesto(self="", anio=anio):
                        if dia < 29:
                            dia += 1
                        else:
                            dia = 0
                            mes += 1
                    else:
                        if dia < 28:
                            dia += 1
                        else:
                            dia = 0
                            mes += 1
        siguiente_fecha = "{0}-{1}-{2} {3}:{4}:00".format(anio, mes, dia, hora, minuto)
        return siguiente_fecha

    # cuenta los minutos entre fecha2(mayor) y fecha1(menor)
    def contar_minutos(fecha1, fecha2):
        fecha_2 = fecha2.split(" ")[0]
        hora_2 = fecha2.split(" ")[1]
        anio_2 = int(fecha_2.split("-")[0])
        mes_2 = int(fecha_2.split("-")[1])
        dia_2 = int(fecha_2.split("-")[2])
        minuto_2 = int(hora_2.split(":")[1])
        horaa_2 = int(hora_2.split(":")[0])
        fecha2 = "{0}-{1}-{2} {3}:{4}:00".format(anio_2, mes_2, dia_2, horaa_2, minuto_2)
        contador = 0
        while fecha1 != fecha2:
            contador += 1
            y = str(FechaYHora.siguiente_minuto(fecha1))
            fecha1 = y
        return contador


class SuperLuchin:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_activo = []
        self.lista_recursos = []
        self.recurso_activo = []
        self.lista_incendios = []
        self.lista_incendios_ocurridos = []
        self.lista_metereologia = []
        self.fecha_actual = ""
        self.hora_actual = ""
        self.archivos = Archivos()
        self.fecha = FechaYHora()
        self.anio = 0
        self.mes = 0
        self.dia = 0
        self.fecha_y_hora_actual = ""
        print("---- Bienvenido al Software SuperLuchin -----")
        self.iniciar_sesion()

    def iniciar_sesion(self):
        self.lista_usuarios = self.archivos.cargar_usuarios()
        self.lista_recursos = self.archivos.cargar_recursos()
        identificador = False
        while identificador == False:
            usuario_ingresado = input("ingrese usuario: ")
            clave_ingresada = input("ingrese contraseña: ")
            for usuarios_existentes in self.lista_usuarios:
                if usuario_ingresado == usuarios_existentes.nombre and clave_ingresada == usuarios_existentes.contrasena:
                    identificador = True
                    self.usuario_activo = usuarios_existentes
                    break
                else:
                    identificador = False
            if identificador is False:
                print("clave o usuario incorrecto")
        mensaje = "-- Bienvenido {0} ".format(self.usuario_activo.nombre)
        for recursos in self.lista_recursos:
            if self.usuario_activo.recurso_id == recursos.id:
                mensaje1 = "miembro de {0}--".format(recursos.tipo)
                self.recurso_activo = recursos
                break
            else:
                mensaje1 = "miembro de la ANAF--"
        print(mensaje + mensaje1)
        self.cambiar_fecha_hora()
        print(self.fecha_y_hora_actual)
        self.lista_metereologia = self.archivos.cargar_meteorologia()
        self.lista_incendios = self.archivos.cargar_incendios()
        self.lista_incendios_ocurridos = self.archivos.cargar_incendios()
        self.menu()

    def menu(self):
        if self.recurso_activo == []:
            contador = True
            while contador:
                print("Opciones:\n0 : Cerrar sesion\n1 : Ver datos incendios\n2 : Ver datos recursos\n"
                      "3 : Ver datos usuarios\n4 : Agregar usuario\n"
                      "5 : Agregar pronostico meteorologico\n6 : Agregar nuevo incendio\n7 : Consultas avanzadas\n8 :Cambiar Fecha y Hora\n9 :Asignar recuros\n10: Salir ")
                opcion = input("Ingrese alguna opcion: ")
                try:
                    val = int(opcion)
                    opcion = int(opcion)
                    if int(opcion) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                        if opcion == 0:
                            self.cerrar_sesion()
                            contador = False
                        elif opcion == 1:
                            self.ver_incendios()
                        elif opcion == 2:
                            self.ver_recursos()
                        elif opcion == 3:
                            self.ver_usuarios()
                        elif opcion == 4:
                            self.agregar_usuario()
                        elif opcion == 5:
                            self.agregar_pronostico_meteorologico()
                        elif opcion == 6:
                            self.agregar_incendio()
                        elif opcion == 7:
                            self.consultas_avanzadas()
                        elif opcion == 8:
                            self.cambiar_fecha_hora()
                        elif opcion == 9:
                            self.asignar_recurso()
                        elif opcion == 10:
                            self.ver_recurso()
                    else:
                        print("Opcion no valida")
                except ValueError:
                    print("Opcion no valida")
        else:
            print("no Anaf")

    def cerrar_sesion(self):
        self.lista_recursos = []
        self.lista_usuarios = []
        self.usuario_activo = []
        self.recurso_activo = []
        self.fecha_actual = ""
        self.hora_actual = ""
        self.archivos = Archivos()
        self.fecha = FechaYHora()
        self.anio = 0
        self.mes = 0
        self.dia = 0
        print("---- Bienvenido al Software SuperLuchin -----")
        self.iniciar_sesion()

    def cambiar_fecha_hora(self):
        self.anio = self.fecha.ver_anio()
        self.mes = self.fecha.ver_mes()
        self.dia = self.fecha.ver_dia()
        self.fecha_actual = ("{2}-{1}-{0}".format(self.dia, self.mes, self.anio))
        self.hora_actual = self.fecha.ver_hora()
        self.fecha_y_hora_actual = self.fecha_actual + " " + self.hora_actual

    def simulacion_incendio_solo(self, incendio, fecha_inicio_simulacion, fecha_termino_s):
        fecha_simulacion = fecha_inicio_simulacion
        contador = FechaYHora.contar_minutos(fecha_inicio_simulacion, fecha_termino_s)
        while contador > 0:
            if fecha_simulacion in incendio.horas_ya_simuladas:
                pass
            else:
                incendio.radio += (0.5 / 60)
                for condiciones in self.lista_metereologia:
                    if FechaYHora.comparar_fecha(fecha_simulacion,
                                                 condiciones.fecha_inicio) and FechaYHora.comparar_fecha(
                        condiciones.fecha_termino, fecha_simulacion):
                        x = (float(condiciones.lat) - float(incendio.lat)) ** 2
                        y = (float(condiciones.lon) - float(incendio.lon)) ** 2
                        distancia_grado = math.sqrt(x + y)
                        distancia_km = distancia_grado * 110
                        if distancia_km <= (float(condiciones.radio) / 1000 + float(incendio.radio)):
                            tasa_por_minuto = 0
                            if condiciones.tipo == "VIENTO":
                                tasa_por_minuto = (((float(condiciones.valor)) / 1000) * 60) / 100
                            elif condiciones.tipo == "TEMPERATURA":
                                if float(condiciones.valor) > 30:
                                    tasa_por_minuto = ((float(condiciones.valor) - 30) * 25) / 60
                            elif condiciones.tipo == "LLUVIA":
                                tasa_por_minuto = (float(condiciones.valor) * -50) / 60
                            incendio.radio += tasa_por_minuto
                incendio.horas_ya_simuladas.append(fecha_simulacion)
            fecha_simulacion = (FechaYHora.siguiente_minuto(fecha_simulacion))
            contador -= 1
            incendio.fecha_ultima_simulacion = self.fecha_y_hora_actual

    def simulacion_recurso(self, recurso):
        if recurso.estado == "standby":
            if FechaYHora.contar_minutos(recurso.fecha_llegada, self.fecha_y_hora_actual) > int(recurso.delay):
                return True
            else:
                print("Recurso en delay")
        elif recurso.estado == "en ruta a incendio":
            for incendio in self.lista_incendios_ocurridos:
                if int(incendio.id) == int(recurso.id_incendio_asignado):
                    break
            if len(incendio.recursos_usados) >= 1:
                print("hola")
                self.simulacion_incendio_solo(incendio, incendio.fecha_ultimo_recurso, recurso.fecha_inicio)
                fecha1 = recurso.fecha_ultima_ejecucion
                fecha2 = FechaYHora.siguiente_minuto(recurso.fecha_ultima_ejecucion)
                minutos = FechaYHora.contar_minutos(recurso.fecha_inicio, self.fecha_y_hora_actual)
                recurso.autonomia_restante = recurso.autonomia - recurso.horas_trabajadas
                x = (float(recurso.lat_actual) - float(incendio.lat)) ** 2
                y = (float(recurso.lon_actual) - float(incendio.lon)) ** 2
                distancia_grado = math.sqrt(x + y)
                distancia_km = distancia_grado * 110
                cos_o = ((float(recurso.lat) - float(incendio.lat)) * 110) / distancia_km
                sen_o = ((float(recurso.lon) - float(incendio.lon)) * 110) / distancia_km
                velocidad_km_min = (((float(recurso.velocidad)) / 1000) * 60)
                recurso.distancia_recorrida = velocidad_km_min * (recurso.horas_trabajadas * 60)
                contador = True
                while minutos > 0 and (
                    (recurso.autonomia_restante * 60) * velocidad_km_min) > recurso.distancia_recorrida and contador:
                    if distancia_km > (incendio.radio + recurso.distancia_recorrida):
                        recurso.horas_trabajadas += float(1 / 60)
                        recurso.total_horas_trabajadas += float(1 / 60)
                        recurso.autonomia_restante = float(recurso.autonomia) - recurso.horas_trabajadas
                        recurso.distancia_recorrida = velocidad_km_min * (recurso.horas_trabajadas * 60)
                        self.simulacion_incendio_solo(incendio, fecha1, fecha2)
                        fecha1 = FechaYHora.siguiente_minuto(fecha1)
                        fecha2 = FechaYHora.siguiente_minuto(fecha2)
                        minutos -= 1
                        recurso.lon_actual = ((recurso.distancia_recorrida * cos_o) / 110) + int(recurso.lon_actual)
                        recurso.lat_actual = ((recurso.distancia_recorrida * sen_o) / 110) + int(recurso.lat_actual)
                        recurso.distancia_objetivo = distancia_km - recurso.distancia_recorrida
                        recurso.fecha_ultima_ejecucion = fecha2
                    elif distancia_km <= (incendio.radio + recurso.distancia_recorrida):
                        recurso.estado = "trabajando en incendio"
                        recurso.fecha_llegada = fecha2
                        contador = False
                    elif ((recurso.autonomia_restante * 60) * velocidad_km_min) <= recurso.distancia_recorrida:
                        recurso.estado = "en ruta a base"
                        contador = False
        if recurso.estado == "trabajando en incendio":
            for incendio in self.lista_incendios_ocurridos:
                if int(incendio.id) == int(recurso.id_incendio_asignado):
                    break
            velocidad_km_min = (((float(recurso.velocidad)) / 1000) * 60)
            minutos = float(FechaYHora.contar_minutos(recurso.fecha_ultima_ejecucion, self.fecha_y_hora_actual))
            minutos_disponibles = ((recurso.autonomia_restante) * 60) - (
            recurso.distancia_recorrida / float(velocidad_km_min))
            fecha = recurso.fecha_ultima_ejecucion
            if minutos_disponibles > 0:
                incendio.puntos_poder_extintos += (float(recurso.tasa_extincion) / 60) * min(minutos,
                                                                                             minutos_disponibles)
                recurso.puntos_apagados += (float(recurso.tasa_extincion) / 60) * min(minutos, minutos_disponibles)
                recurso.autonomia_restante -= (min(minutos, minutos_disponibles)) / 60
                recurso.horas_trabajadas += (min(minutos, minutos_disponibles)) / 60
                recurso.total_horas_trabajadas += (min(minutos, minutos_disponibles)) / 60
                if incendio.activo == "apagado":
                    incendio.fecha_apagado = fecha
                else:
                    self.simulacion_incendio_solo(incendio, recurso.fecha_ultima_ejecucion, self.fecha_y_hora_actual)
                while minutos_disponibles > 0:
                    fecha = FechaYHora.siguiente_minuto(fecha)
                    minutos_disponibles -= 1
                    recurso.fecha_ultima_ejecucion = fecha
            if recurso.autonomia_restante * 60 <= recurso.distancia_recorrida / float(velocidad_km_min):
                recurso.estado = "en ruta a base"
                recurso.fecha_salida_incendio = fecha
                incendio.fecha_ultimo_recurso = fecha
                recurso.fecha_ultima_ejecucion = fecha
        if recurso.estado == "en ruta a base":
            if recurso.fecha_ultima_ejecucion == recurso.fecha_salida_incendio:
                recurso.distancia_objetivo = recurso.distancia_recorrida
                recurso.distancia_recorrida = 0
            minutos_disponibles = FechaYHora.contar_minutos(recurso.fecha_ultima_ejecucion, self.fecha_y_hora_actual)
            tiempo_llegada = (recurso.distancia_objetivo-recurso.distancia_recorrida) / ((float(recurso.velocidad) / 1000) * 60)
            fecha = recurso.fecha_ultima_ejecucion
            if minutos_disponibles >= tiempo_llegada:
                recurso.estado = "standby"
                recurso.total_horas_trabajadas += (tiempo_llegada/60)
                while tiempo_llegada > 0:
                    fecha = FechaYHora.siguiente_minuto(fecha)
                    tiempo_llegada -= 1
                recurso.horas_trabajadas = 0
                recurso.autonomia_restante = recurso.autonomia
                recurso.fecha_llegada = fecha
                recurso.lat_actual = recurso.lat
                recurso.lon_actual = recurso.lon
                if FechaYHora.contar_minutos(recurso.fecha_llegada, self.fecha_y_hora_actual) > int(recurso.delay):
                    print("Recurso listo para ser usado de nuevo")
                else:
                    print("Recurso en delay")
            elif minutos_disponibles < tiempo_llegada:
                recurso.distancia_recorrida = ((float(recurso.velocidad)/1000)*60)*minutos_disponibles
                recurso.horas_trabajadas += minutos_disponibles / 60
                recurso.total_horas_trabajadas += minutos_disponibles / 60
                recurso.autonomia_restante -= minutos_disponibles / 60
                while minutos_disponibles > 0:
                    fecha = FechaYHora.siguiente_minuto(fecha)
                    minutos_disponibles -= 1
                recurso.fecha_ultima_ejecucion = fecha
                distancia_km = recurso.distancia_objetivo
                cos_o = ((float(recurso.lat) - float(incendio.lat)) * 110) / distancia_km
                sen_o = ((float(recurso.lon) - float(incendio.lon)) * 110) / distancia_km
                recurso.lon_actual = ((recurso.distancia_recorrida * cos_o) / 110) + int(recurso.lon_actual)
                recurso.lat_actual = ((recurso.distancia_recorrida * sen_o) / 110) + int(recurso.lat_actual)

    def incendios_activos(self):
        incendios_inactivos = []
        for incendio in self.lista_incendios_ocurridos:
            if FechaYHora.comparar_fecha(incendio.fecha_inicio, self.fecha_y_hora_actual):
                incendios_inactivos.append(incendio)
            if not incendio in incendios_inactivos:
                self.simulacion_incendio_solo(incendio, incendio.fecha_inicio, self.fecha_y_hora_actual)
        for incendio in incendios_inactivos:
            self.lista_incendios_ocurridos.remove(incendio)

    def ver_recurso(self):
        x = input("ingrese id recurso: ")
        for recurso in self.lista_recursos:
            if int(recurso.id) == int(x):
                if FechaYHora.comparar_fecha(recurso.fecha_ultima_ejecucion, self.fecha_y_hora_actual):
                    print("hola")
                    print(recurso.horas_trabajadas)
                    print(recurso.autonomia_restante)
                    print(recurso.estado)
                else:
                    self.simulacion_recurso(recurso)
                    print(recurso.horas_trabajadas)
                    print(recurso.autonomia_restante)
                    print(recurso.estado)

    def agregar_pronostico_meteorologico(self):
        verificador1 = True
        verificador2 = True
        verificador3 = True
        verificador4 = True
        verificador5 = True
        verificador6 = True
        verificador7 = True
        while verificador1:
            lat = input("Ingrese latitud: ")
            try:
                val = float(lat)
                verificador1 = False
            except ValueError:
                print("dato incorrecto")
        while verificador2:
            lon = input("Ingrese Longitud: ")
            try:
                val = float(lon)
                verificador2 = False
            except ValueError:
                print("dato incorrecto")
        while verificador3:
            valor = input("Ingrese valor: ")
            try:
                val = float(valor)
                verificador3 = False
            except ValueError:
                print("dato incorrecto")
        while verificador4:
            radio = input("Ingrese radio: ")
            try:
                val = int(radio)
                verificador4 = False
            except ValueError:
                print("dato incorrecto")
        while verificador5:
            tipo = input("Ingrese tipo: ")
            if tipo in ["VIENTO", "NUBES", "LLUVIA", "TEMPERATURA"]:
                verificador5 = False
            else:
                print("dato incorrecto")
        while verificador6:
            print("Fecha inicio:")
            anio = self.fecha.ver_anio()
            mes = self.fecha.ver_mes()
            dia = self.fecha.ver_dia()
            fecha_inicio = ("{2}-{1}-{0}".format(dia, mes, anio))
            hora_inicio = self.fecha.ver_hora()
            fecha_inicio = fecha_inicio + " " + hora_inicio
            print("Fecha termino:")
            anio = self.fecha.ver_anio()
            mes = self.fecha.ver_mes()
            dia = self.fecha.ver_dia()
            fecha_termino = ("{2}-{1}-{0}".format(dia, mes, anio))
            hora_termino = self.fecha.ver_hora()
            fecha_termino = fecha_termino + " " + hora_termino
            if FechaYHora.comparar_fecha(fecha_termino, fecha_inicio):
                verificador6 = False
            else:
                print("Fecha incorrecta, fecha termino debe ser posterior a la de inicio")
        id = len(self.lista_metereologia)
        meteorologia1 = Meteorologia(id=id, lat=lat, lon=lon, radio=radio, fecha_inicio=fecha_inicio,
                                     fecha_termino=fecha_termino, tipo=tipo, valor=valor)
        self.lista_metereologia.append(meteorologia1)
        print("Pronostico meteorologico agregado correctamente\n")
        self.archivos.sobreescribir_meteorologia(self.lista_metereologia)

    def consultas_avanzadas(self):
        contador = True
        while contador:
            print("Opciones:\n0 : volver \n1 : Ver incendios apagados\n2 : Ver recursos más usados\n"
                  "3 : Recurso más efectivo\n")
            opcion = input("Ingrese alguna opcion: ")
            try:
                val = int(opcion)
                opcion = int(opcion)
                if int(opcion) in [0, 1, 2, 3]:
                    if opcion == 0:
                        contador = False
                    elif opcion == 1:
                        self.ver_incendios_apagados()
                    elif opcion == 2:
                        self.ver_recurso_mas_usado()
                    elif opcion == 3:
                        self.recurso_mas_efectivo()
                else:
                    print("Opcion no valida")
            except ValueError:
                print("Opcion no valida")

    def ver_incendios_apagados(self):
        for incendio in self.lista_incendios_ocurridos:
            if incendio.activo == "apagado":
                print(
                    "id: {},fecha inicio: {},fecha apagado: {}, recursos: {}".format(incendio.id, incendio.fecha_inicio,
                                                                                     incendio.fecha_apagado,
                                                                                     incendio.recursos_usados))
    def ver_recurso_mas_usado(self):
#al no tener hora, se asume que todos los recursos parten al mismo tiempo
        lista = []
        for recurso in self.lista_recursos:
            texto = ""
            texto += str(recurso.total_horas_trabajadas)
            texto +=":"+str(recurso.id)
            lista.append(texto)
        lista.sort(reverse=True)
        for elemento in lista:
            print("Id: {}".format(elemento.split(":")[1]))

    def recurso_mas_efectivo(self):
        lista = []
        for recurso in self.lista_recursos:
            normalizar = recurso.puntos_apagados/recurso.tasa_extincion
            efectividad = normalizar/recurso.total_horas_trabajadas
            texto = ""
            texto += str(efectividad)
            texto += ":" + str(recurso.id)
            lista.append(texto)
        lista.sort(reverse=True)
        for elemento in lista:
            print("Id: {}".format(elemento.split(":")[1]))

    def agregar_usuario(self):
        nombre = input("Ingrese nombre: ")
        contrasena = input("Ingrese contrasena: ")
        verificador = True
        while verificador:
            tipo = input("Ingrese nombre del recurso en mayusculas(deje en blanco si es ANAF): ")
            if tipo in ["BOMBERO", "AVION", "HELICOPTERO", "BRIGADA", ""]:
                if tipo == "":
                    recurso_id = ""
                else:
                    verificador1 = True
                    verificador2 = True
                    verificador3 = True
                    verificador4 = True
                    verificador5 = True
                    verificador6 = True
                    verificador7 = True
                    while verificador1:
                        lat = input("Ingrese latitud: ")
                        try:
                            val = float(lat)
                            verificador1 = False
                        except ValueError:
                            print("dato incorrecto")
                    while verificador2:
                        lon = input("Ingrese Longitud: ")
                        try:
                            val = float(lon)
                            verificador2 = False
                        except ValueError:
                            print("dato incorrecto")
                    while verificador3:
                        velocidad = input("Ingrese velocidad: ")
                        try:
                            val = int(velocidad)
                            verificador3 = False
                        except ValueError:
                            print("dato incorrecto")
                    while verificador4:
                        autonomia = input("Ingrese autonomia: ")
                        try:
                            val = float(autonomia)
                            verificador4 = False
                        except ValueError:
                            print("dato incorrecto")
                    while verificador5:
                        tasa_extincion = input("Ingrese tasa_extincion: ")
                        try:
                            val = int(tasa_extincion)
                            verificador5 = False
                        except ValueError:
                            print("dato incorrecto")
                    while verificador6:
                        delay = input("Ingrese delay: ")
                        try:
                            val = int(delay)
                            verificador6 = False
                        except ValueError:
                            print("dato incorrecto")
                    while verificador7:
                        costo = input("Ingrese costo: ")
                        try:
                            val = int(costo)
                            verificador7 = False
                        except ValueError:
                            print("dato incorrecto")
                    id = len(self.lista_recursos)
                    recurso_id = id
                    recurso = Recurso(id=id, tipo=tipo, lat=lat, lon=lon, autonomia=autonomia, delay=delay,
                                      tasa_extincion=tasa_extincion, costo=costo, velocidad=velocidad)
                    self.lista_recursos.append(recurso)
                verificador = False
        id = len(self.lista_usuarios)
        usuario = Usuario(id=id, nombre=nombre, contrasena=contrasena, recurso_id=recurso_id)
        self.lista_usuarios.append(usuario)
        self.archivos.sobreescribir_usuarios(self.lista_usuarios)
        self.archivos.sobreescribir_recursos(self.lista_recursos)
        print("Usuario agregado correctamente\n")

    def agregar_incendio(self):
        verificador1 = True
        verificador2 = True
        verificador3 = True
        verificador4 = True
        while verificador1:
            lat = input("Ingrese latitud: ")
            try:
                val = float(lat)
                verificador1 = False
            except ValueError:
                print("dato incorrecto")
        while verificador2:
            lon = input("Ingrese Longitud: ")
            try:
                val = float(lon)
                verificador2 = False
            except ValueError:
                print("dato incorrecto")
        while verificador3:
            potencia = input("Ingrese potencia: ")
            try:
                val = int(potencia)
                verificador3 = False
            except ValueError:
                print("dato incorrecto")
        while verificador4:
            anio = self.fecha.ver_anio()
            mes = self.fecha.ver_mes()
            dia = self.fecha.ver_dia()
            fecha_inicio = ("{2}-{1}-{0}".format(dia, mes, anio))
            hora_inicio = self.fecha.ver_hora()
            fecha_inicio = fecha_inicio + " " + hora_inicio
            if not FechaYHora.comparar_fecha(fecha_inicio, self.fecha_y_hora_actual):
                verificador4 = False
            else:
                print("Fecha incorrecta, debe ser anterior a la fecha actual")
        id = len(self.lista_incendios)
        incendio = Incendio(id=id, lat=lat, lon=lon, potencia=potencia, fecha_inicio=fecha_inicio)
        self.lista_incendios.append(incendio)
        self.lista_incendios_ocurridos.append(incendio)
        print("Incendio agregado correctamente\n")
        self.archivos.sobreescribir_incendios(self.lista_incendios)

    def ver_usuarios(self):
        for usuario in self.lista_usuarios:
            print("id: {0},Nombre: {1},Clave: {2},Id del recurso: {3}".format(usuario.id, usuario.nombre,
                                                                              usuario.contrasena, usuario.recurso_id))

    def ver_incendios(self):
        self.incendios_activos()
        print("aqui")
        if len(self.lista_incendios_ocurridos) == 0:
            print("\nNo hay incendios activos\n")
        else:
            for incendios in self.lista_incendios_ocurridos:
                print(incendios)
                print(
                    "El Incendio {0} esta {1}, porcentaje de extincion: {3}, recursos asigandos: {2}, puntos de poder: {4}".format(
                        incendios.id,
                        incendios.activo,
                        incendios.recursos_usados,
                        incendios.porcentaje_de_extincion, incendios.puntos_poder))
                print("---------------------------------------------------------------")

    def ver_recursos(self):
        for recurso in self.lista_recursos:
            print("---------------")
            print(recurso)
            print("estado: {}, ubicacion actual: lat={} lon={}".format(recurso.estado, recurso.lat_actual,
                                                                       recurso.lon_actual))
            if recurso.estado != "standby":
                horas_restantes = float(recurso.autonomia) - float(recurso.horas_trabajadas)
                print("Horas trabajadas: {},horas restantes:{}".format(recurso.horas_trabajadas, horas_restantes))
            elif recurso.estado != "standby" and recurso.estado != "trabajando en incendio":
                print("distancia a objetivo{}".format(recurso.distancia_objetivo))

    def asignar_recurso(self):
        validador = True
        while validador:
            id_recurso = input("Ingrese id del recurso: ")
            for recurso in self.lista_recursos:
                if id_recurso == recurso.id and recurso.estado == "standby":
                    validador = False
                    recurso.estado = "en ruta a incendio"
                    recurso.fecha_inicio = self.fecha_y_hora_actual
                    recurso.fecha_ultima_ejecucion = self.fecha_y_hora_actual
                    break
            if validador:
                print("Error en id")
        validador = True
        while validador:
            id_incendio = input("Ingrese id del incendio: ")
            for incendio in self.lista_incendios_ocurridos:
                if id_incendio == incendio.id:
                    if FechaYHora.comparar_fecha(self.fecha_y_hora_actual, incendio.fecha_inicio):
                        incendio.recursos_usados.append(recurso.id)
                        recurso.id_incendio_asignado = incendio.id
                        self.simulacion_incendio_solo(incendio, incendio.fecha_inicio, self.fecha_y_hora_actual)
                        validador = False
                        break
            if validador:
                print("id erroneo o incendio posterior a fecha actual")
        print("\nRecurso asignado correctamente\n")


ejecutar = SuperLuchin()
