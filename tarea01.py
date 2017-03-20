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
        self.lat = lat
        self.lon = lon
        self.autonomia = autonomia
        self.delay = delay
        self.tasa_extincion = tasa_extincion
        self.costo = costo


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

    @property
    def activo(self):
        if self.potencia > 0:
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
        self.primera_linea_usuarios=""
        self.primera_linea_incendios=""
        self.primera_linea_recursos=""
        self.primera_linea_metereologia=""

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
                                       tasa_extincion=tasa_extincion, costo=costo)
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

    def sobreescribir_usuarios(self,lista):
        archivo = open("usuarios.csv", "w")
        orden = self.primera_linea_usuarios.strip("\n").split(",")
        texto = ""
        for elemento in orden:
            if (elemento.split(":")[0])=="id":
                texto +=str(elemento)+","
        for elemento in orden:
            if (elemento.split(":")[0])=="nombre":
                texto +=str(elemento)+","
        for elemento in orden:
            if (elemento.split(":")[0])=="contraseña":
                texto +=str(elemento)+","
        for elemento in orden:
            if (elemento.split(":")[0])=="recurso_id":
                texto +=str(elemento)+"\n"
        archivo.write(texto)
        fila=""
        for elemento in lista:
            fila += str(elemento.id) + ","
            fila += str(elemento.nombre) + ","
            fila += str(elemento.contrasena) + ","
            fila += str(elemento.recurso_id) + "\n"
            archivo.write(fila)
            fila = ""
        archivo.close()

    def sobreescribir_incendios(self,lista):
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
            if identificador == False:
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
        self.menu()

    def cambiar_fecha_hora(self):
        self.anio = self.fecha.ver_anio()
        self.mes = self.fecha.ver_mes()
        self.dia = self.fecha.ver_dia()
        self.fecha_actual = ("{2}-{1}-{0}".format(self.dia, self.mes, self.anio))
        self.hora_actual = self.fecha.ver_hora()
        self.fecha_y_hora_actual = self.fecha_actual + " " + self.hora_actual

    def incendios_activos(self):
        incendios_inactivos = []
        for incendio in self.lista_incendios:
            radio = 0
            self.anio = int(self.anio)
            self.mes = int(self.mes)
            self.dia = int(self.dia)
            hora = incendio.fecha_inicio.split(" ")[1]
            hora = hora.split(":")
            minuto = int(hora[1])
            hora = int(hora[0])
            fecha = incendio.fecha_inicio.split(" ")[0]
            fecha = fecha.split("-")
            dia = int(fecha[2])
            mes = int(fecha[1])
            anio = int(fecha[0])
            hora_actual_programa = self.hora_actual.strip(":")
            hora_actual = int(hora_actual_programa[0])
            minuto_actual = int(hora_actual_programa[1])
            if anio > self.anio:
                incendios_inactivos.append(incendio)
            elif anio == self.anio:
                if mes > self.mes:
                    incendios_inactivos.append(incendio)
                elif mes == self.mes:
                    if dia > self.dia:
                        incendios_inactivos.append(incendio)
                    elif dia == self.dia:
                        if hora > hora_actual:
                            incendios_inactivos.append(incendio)
                        elif hora == hora:
                            if minuto > minuto_actual:
                                incendios_inactivos.append(incendio)
            if not incendio in incendios_inactivos:
                fecha_simulacion = "{0}-{1}-{2} {3}:{4}:00".format(anio, mes, dia, hora, minuto)
                while FechaYHora.comparar_fecha(self.fecha_y_hora_actual, fecha_simulacion):
                    incendio.radio += (0.5 / 60)
                    for condiciones in self.lista_metereologia:
                        x = (float(condiciones.lat) - float(incendio.lat)) ** 2
                        y = (float(condiciones.lon) - float(incendio.lon)) ** 2
                        distancia_grado = math.sqrt(x + y)
                        distancia_km = distancia_grado * 110
                        if distancia_km <= (float(condiciones.radio) / 1000 + float(incendio.radio)):
                            if FechaYHora.comparar_fecha(fecha_simulacion,
                                                         condiciones.fecha_inicio) and FechaYHora.comparar_fecha(
                                condiciones.fecha_termino, fecha_simulacion):
                                tasa_por_minuto = 0
                                if condiciones.tipo == "VIENTO":
                                    tasa_por_minuto = (((float(condiciones.valor)) / 1000) * 60) / 100
                                elif condiciones.tipo == "TEMPERATURA":
                                    if float(condiciones.valor) > 30:
                                        tasa_por_minuto = ((float(condiciones.valor) - 30) * 25) / 60
                                elif condiciones.tipo == "LLUVIA":
                                    tasa_por_minuto = (float(condiciones.valor) * -50) / 60
                                incendio.radio += tasa_por_minuto
                    fecha_simulacion = (FechaYHora.siguiente_minuto(fecha_simulacion))
        for incendio in incendios_inactivos:
            self.lista_incendios_ocurridos.remove(incendio)

    def menu(self):
        self.lista_metereologia = self.archivos.cargar_meteorologia()
        self.lista_incendios = self.archivos.cargar_incendios()
        self.lista_incendios_ocurridos = self.archivos.cargar_incendios()
        if self.recurso_activo == []:
            contador = True
            while contador:
                print("Opciones:\n0 : Cerrar sesion\n1 : Ver datos incendios\n2 : Ver datos recursos\n"
                      "3 : Ver datos usuarios\n4 : Agregar usuario\n"
                      "5 : Agregar pronostico meteorologico\n6 : Agregar nuevo incendio\n7 : Consultas avanzadas\n8 :Cambiar Fecha y Hora\n9 :Salir ")
                opcion = input("Ingrese alguna opcion: ")
                try:
                    val = int(opcion)
                    opcion = int(opcion)
                    if int(opcion) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        if opcion == 0:
                            self.cerrar_sesion()
                            contador = False
                        elif opcion == 1:
                            self.ver_incendios()
                        elif opcion == 4:
                            self.agregar_usuario()
                        elif opcion == 6:
                            self.agregar_incendio()
                        elif opcion == 8:
                            self.cambiar_fecha_hora()
                            contador = False
                            self.menu()
                    else:
                        print("Opcion no valida")
                except ValueError:
                    print("Opcion no valida")
        else:
            print("no Anaf")

    def agregar_usuario(self):
        nombre = input("Ingrese nombre: ")
        contrasena = input("Ingrese contrasena: ")
        verificador = True
        while verificador:
            recurso_id = input("Ingrese ID del recurso(deje en blanco si es ANAF): ")
            for recurso in self.lista_recursos:
                if recurso_id == recurso.id:
                    verificador = False
                elif recurso_id == "":
                    verificador = False
            if verificador:
                print("Recurso no valido")
        id = len(self.lista_usuarios)
        usuario = Usuario(id=id, nombre=nombre, contrasena=contrasena, recurso_id=recurso_id)
        self.lista_usuarios.append(usuario)
        self.archivos.sobreescribir_usuarios(self.lista_usuarios)
        print("Usuario agregado correctamente\n")

    def agregar_incendio(self):
        verificador1 = True
        verificador2 = True
        verificador3 = True
        verificador4 = True
        while verificador1:
            lat = input("Ingrese latitud: ")
            try:
                val = int(lat)
                verificador1 = False
            except ValueError:
                print("dato incorrecto")
        while verificador2:
            lon = input("Ingrese Longitud: ")
            try:
                val = int(lon)
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

    def ver_incendios(self):
        self.incendios_activos()
        if len(self.lista_incendios_ocurridos) == 0:
            print("No hay incendios activos")
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


def escribir(x):
    archivo = open("hola.csv", "w")
    h = ""
    for i in x:
        h += i.id + ","
        h += i.nombre + ","
        h += i.contrasena + ","
        h += i.recurso_id + "\n"
        archivo.write(h)
        h = ""
    archivo.close()


ejecutar = SuperLuchin()
