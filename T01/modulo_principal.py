import math
import shutil
from modulo_FechaYHora import FechaYHora
from objetos_personas import Usuario
from objetos_personas import Incendio
from objetos_personas import Recurso
from objetos_personas import Meteorologia
from funciones_archivos import Archivos
import os

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
        lis = os.listdir(os.getcwdb())
        try:
            os.mkdir("Reportes Estrategias de Extincion")
        except:
            FileExistsError
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
        self.cambiar_fecha_hora()
        print(self.fecha_y_hora_actual)
        self.cargar_archivos()
        for recursos in self.lista_recursos:
            if self.usuario_activo.recurso_id == recursos.id:
                mensaje1 = "miembro de {0}--".format(recursos.tipo)
                self.recurso_activo = recursos
                break
            else:
                mensaje1 = "miembro de la ANAF--"
        print(mensaje + mensaje1)
        print("calculando simulacion a la fecha ingresada, favor esperar")
        for recursos in self.lista_recursos:
            self.simulacion_recurso(recursos)
        self.menu()

    def cargar_archivos(self):
        self.lista_metereologia = self.archivos.cargar_meteorologia()
        self.lista_incendios = self.archivos.cargar_incendios()
        self.lista_incendios_ocurridos = self.archivos.cargar_incendios()
        self.archivos.cargar_simulacion(self.fecha_y_hora_actual, self.lista_recursos, self.lista_incendios_ocurridos)

    def sobreescribir_archivos(self):
        self.archivos.sobreescribir_simulacion(self.lista_incendios_ocurridos, self.lista_recursos)

    def menu(self):
        if self.recurso_activo == []:
            contador = True
            while contador:
                print("Opciones:\n0 : Cerrar sesion\n1 : Ver datos incendios\n2 : Ver datos recursos\n"
                      "3 : Ver datos usuarios\n4 : Agregar usuario\n"
                      "5 : Agregar pronostico meteorologico\n6 : Agregar nuevo incendio\n7 : Consultas avanzadas\n8 :Cambiar Fecha y Hora\n9 :Asignar recuros\n10: Estrategias extincion\n11: Salir ")
                opcion = input("Ingrese alguna opcion: ")
                try:
                    val = int(opcion)
                    opcion = int(opcion)
                    if int(opcion) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                        if opcion == 0:
                            self.sobreescribir_archivos()
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
                            self.sobreescribir_archivos()
                            self.cambiar_fecha_hora()
                        elif opcion == 9:
                            self.asignar_recurso()
                        elif opcion == 10:
                            self.estrategia_extincion()
                        elif opcion == 11:
                            self.sobreescribir_archivos()
                            print("Programa cerrado correctamente")
                            contador = False
                    else:
                        print("Opcion no valida")
                except ValueError:
                    print("Opcion no valida")
        else:
            recurso = self.recurso_activo
            self.simulacion_recurso(recurso)
            print("------ Barra Estado Recurso ---------")
            print(recurso)
            print("estado: {}, ubicacion actual: lat={} lon={}".format(recurso.estado, recurso.lat_actual,
                                                                       recurso.lon_actual))
            if recurso.estado != "standby":
                horas_restantes = float(recurso.autonomia) - float(recurso.horas_trabajadas)
                print("Horas trabajadas: {},horas restantes:{}".format(recurso.horas_trabajadas, horas_restantes))
            elif recurso.estado != "standby" and recurso.estado != "trabajando en incendio":
                print("distancia a objetivo{}".format(recurso.distancia_objetivo))
            contador1 = True
            print("---------------------------------")
            while contador1:
                print("Opciones:\n0 : Cerrar sesion\n1 : Ver datos incendio\n2 :Cambiar Fecha y Hora\n3: Salir ")
                opcion = input("Ingrese alguna opcion: ")
                try:
                    val = int(opcion)
                    opcion = int(opcion)
                    if int(opcion) in [0, 1, 2, 3]:
                        if opcion == 0:
                            self.sobreescribir_archivos()
                            self.cerrar_sesion()
                            contador = False
                        elif opcion == 1:
                            self.ver_incendio(recurso)
                        elif opcion == 2:
                            self.sobreescribir_archivos()
                            self.cambiar_fecha_hora()
                        elif opcion == 3:
                            self.sobreescribir_archivos()
                            print("Programa cerrado correctamente")
                            contador = False
                    else:
                        print("Opcion no valida")
                except ValueError:
                    print("Opcion no valida")

    def cerrar_sesion(self):
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
        if recurso.estado == "en ruta a incendio":
            for incendio in self.lista_incendios_ocurridos:
                if int(incendio.id) == int(recurso.id_incendio_asignado):
                    break
            if len(incendio.recursos_usados) >= 1:
                recurso.horas_trabajadas = float(recurso.horas_trabajadas)
                recurso.total_horas_trabajadas = float(recurso.total_horas_trabajadas)
                incendio.radio = float(incendio.radio)
                self.simulacion_incendio_solo(incendio, incendio.fecha_ultimo_recurso, recurso.fecha_inicio)
                fecha1 = recurso.fecha_ultima_ejecucion
                fecha2 = FechaYHora.siguiente_minuto(recurso.fecha_ultima_ejecucion)
                minutos = FechaYHora.contar_minutos(recurso.fecha_inicio, self.fecha_y_hora_actual)
                recurso.autonomia_restante = float(recurso.autonomia) - float(recurso.horas_trabajadas)
                x = (float(recurso.lat_actual) - float(incendio.lat)) ** 2
                y = (float(recurso.lon_actual) - float(incendio.lon)) ** 2
                distancia_grado = math.sqrt(x + y)
                distancia_km = distancia_grado * 110
                cos_o = ((float(recurso.lat) - float(incendio.lat)) * 110) / distancia_km
                sen_o = ((float(recurso.lon) - float(incendio.lon)) * 110) / distancia_km
                velocidad_km_min = (((float(recurso.velocidad)) / 1000) * 60)
                recurso.distancia_recorrida = velocidad_km_min * ((float(recurso.horas_trabajadas)) * 60)
                contador = True
                while minutos > 0 and contador:
                    if distancia_km > (float(incendio.radio) + recurso.distancia_recorrida):
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
                    if ((recurso.autonomia_restante * 60) * velocidad_km_min) <= recurso.distancia_recorrida:
                        recurso.estado = "en ruta a base"
                        recurso.fecha_ultima_ejecucion = fecha2
                        recurso.fecha_salida_incendio = fecha2
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
            tiempo_llegada = (recurso.distancia_objetivo - recurso.distancia_recorrida) / (
                (float(recurso.velocidad) / 1000) * 60)
            fecha = recurso.fecha_ultima_ejecucion
            if minutos_disponibles >= tiempo_llegada:
                recurso.estado = "standby"
                recurso.total_horas_trabajadas += (tiempo_llegada / 60)
                while tiempo_llegada > 0:
                    fecha = FechaYHora.siguiente_minuto(fecha)
                    tiempo_llegada -= 1
                recurso.horas_trabajadas = 0
                recurso.autonomia_restante = recurso.autonomia
                recurso.fecha_llegada = fecha
                recurso.fecha_llegada_base = fecha
                recurso.lat_actual = recurso.lat
                recurso.lon_actual = recurso.lon
                recurso.id_incendio_asignado = ""
                if FechaYHora.contar_minutos(recurso.fecha_llegada, self.fecha_y_hora_actual) > int(recurso.delay):
                    print("Recurso listo para ser usado de nuevo")
                else:
                    print("Recurso en delay")
            elif minutos_disponibles < tiempo_llegada:
                recurso.distancia_recorrida = ((float(recurso.velocidad) / 1000) * 60) * minutos_disponibles
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

    def ver_incendio(self,recurso):
        if recurso.estado == "en ruta a incendio" or recurso.estado == "trabajando en incendio":
            for incendio in self.lista_incendios_ocurridos:
                if str(recurso.id_incendio_asignado) == str(incendio.id):
                    print("Datos incendio:")
                    print("ID: {},lat: {},lon: {},potencia; {},fecha_inicio: {},radio: {}".format(incendio.id,
                                                                                                  incendio.lat,
                                                                                                  incendio.lat,
                                                                                                  incendio.potencia,
                                                                                                  incendio.fecha_inicio,
                                                                                                  incendio.radio))
        else:
            print("No tiene incendio asignado o se encuentra rumbo a base")

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
                  "3 : Recurso más efectivo\n4 : Ver incendios activos")
            opcion = input("Ingrese alguna opcion: ")
            try:
                val = int(opcion)
                opcion = int(opcion)
                if int(opcion) in [0, 1, 2, 3, 4]:
                    if opcion == 0:
                        contador = False
                    elif opcion == 1:
                        self.ver_incendios_apagados()
                    elif opcion == 2:
                        self.ver_recurso_mas_usado()
                    elif opcion == 3:
                        self.recurso_mas_efectivo()
                    elif opcion == 4:
                        self.ver_incendios_activos()
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

    def ver_incendios_activos(self):
        for incendio in self.lista_incendios_ocurridos:
            if incendio.activo == "activo":
                print(
                    "id: {},fecha inicio: {}, recursos: {}".format(incendio.id, incendio.fecha_inicio,
                                                                   incendio.recursos_usados))

    def ver_recurso_mas_usado(self):
        # al no tener hora, se asume que todos los recursos parten al mismo tiempo
        lista = []
        for recurso in self.lista_recursos:
            texto = ""
            texto += str(recurso.total_horas_trabajadas)
            texto += ":" + str(recurso.id)
            lista.append(texto)
        lista.sort(reverse=True)
        for elemento in lista:
            print("Id: {}".format(elemento.split(":")[1]))

    def recurso_mas_efectivo(self):
        lista = []
        for recurso in self.lista_recursos:
            normalizar = float(recurso.puntos_apagados) / float(recurso.tasa_extincion)
            efectividad = normalizar / float(recurso.total_horas_trabajadas)
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
                    recurso.fecha_llegada_base = self.fecha_y_hora_actual
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

    def estrategia_extincion(self):
        contador = True
        while contador:
            print("Opciones:\n0 : volver \n1 : Cantidad de recursos\n2 : Tiempo de extincion\n"
                  "3 : Costo economico")
            opcion = input("Ingrese alguna opcion: ")
            try:
                val = int(opcion)
                opcion = int(opcion)
                if int(opcion) in [0, 1, 2, 3]:
                    if opcion == 0:
                        contador = False
                    elif opcion == 1:
                        self.est_cantidad_recursos()
                    elif opcion == 2:
                        self.est_tiempo()
                    elif opcion == 3:
                        self.est_costo()
                else:
                    print("Opcion no valida")
            except ValueError:
                print("Opcion no valida")

    def est_cantidad_recursos(self):
        pass
    def est_tiempo(self):
        pass
    def est_costo(self):
        lista1 = []
        lista_para_imprimir = []
        validador = True
        while validador:
            id_incendio = input("Ingrese id del incendio: ")
            for incendio in self.lista_incendios_ocurridos:
                if id_incendio == incendio.id:
                    validador = False
                    break
        for recurso in self.lista_recursos:
            x = (float(recurso.lat) - float(incendio.lat)) ** 2
            y = (float(recurso.lon) - float(incendio.lon)) ** 2
            distancia_grado = math.sqrt(x + y)
            distancia_km = distancia_grado * 110
            tiempo_trabajo = float(recurso.autonomia)*60 - ((distancia_km*2)*(((float(recurso.velocidad))*60)/1000))
            real_extincion = float(recurso.tasa_extincion)*(tiempo_trabajo/60)
            costo_segun_extincion = real_extincion/(float(recurso.costo))
            tiempo_ciclo = (float(recurso.autonomia) + float(recurso.delay))*60
            print(tiempo_ciclo)
            txt = ""
            txt += str(costo_segun_extincion)+":"
            txt += str(recurso.id)+":"
            txt += str(tiempo_ciclo)+":"
            txt += str(real_extincion)
            lista1.append(txt)
            print(lista1)
        puntos_poder = incendio.puntos_poder
        minutos_disponibles = FechaYHora.contar_minutos(incendio.fecha_inicio,self.fecha_y_hora_actual)
        lista1.sort(reverse=True)
        print(lista1)
        for elemento in lista1:
            print("2")
            if puntos_poder <= 0:
                break
            contador = minutos_disponibles
            elemento = elemento.split(":")
            while contador >0:
                puntos_poder -= elemento[3]
                contador -= elemento[2]
                texto = str(elemento[1])+":"+str(elemento[3])
                lista_para_imprimir.append(texto)
        nombre ="{}_costo_economico.txt".format(incendio.id)
        archivo = open(nombre,"w")
        lista_ya_guardado = []
        for i in lista_para_imprimir:
            if not i in lista_ya_guardado:
                veces = 0
                fecha = incendio.fecha_inicio
                for j in lista_para_imprimir:
                    if i.strip[":"][0] == j.strip[":"][0]:
                        veces +=1
                lista_ya_guardado.append(i)
                for recurso in self.lista_recursos:
                    if str(recurso.id) == i.strip[":"][0]:
                        while veces >= 0:
                            txt = ""
                            veces -=1
                            x = (float(recurso.lat) - float(incendio.lat)) ** 2
                            y = (float(recurso.lon) - float(incendio.lon)) ** 2
                            distancia_grado = math.sqrt(x + y)
                            distancia_km = distancia_grado * 110
                            minutos_para_i = ((distancia_km ) * (((float(recurso.velocidad)) * 60) / 1000))
                            txt += "hora salida base: {}".format(fecha)
                            while minutos_para_i>=0:
                                fecha = FechaYHora.siguiente_minuto(fecha)
                                minutos_para_i -=1
                            tiempo_trabajo = float(recurso.autonomia) - (
                            (distancia_km * 2) * (((float(recurso.velocidad)) * 60) / 1000))
                            txt += "hora llegada incendio: {}".format(fecha)
                            while tiempo_trabajo>=0:
                                fecha = FechaYHora.siguiente_minuto(fecha)
                                tiempo_trabajo -= 1
                            minutos_para_b = ((distancia_km) * (((float(recurso.velocidad)) * 60) / 1000))
                            txt += "hora salida incendio: {}".format(fecha)
                            while minutos_para_b>=0:
                                fecha = FechaYHora.siguiente_minuto(fecha)
                                minutos_para_b -=1
                            txt += "hora llegada a base {}".format(fecha)
                            minutos_delay = float(recurso.delay)*60
                            while minutos_delay >= 0:
                                fecha = FechaYHora.siguiente_minuto(fecha)
                                minutos_delay -= 1
                            txt += "puntos apagados {}".format(i[1])
                            archivo.write(txt)
        archivo.close()
        #shutil.move(nombre,os.getcwdb()+os.fsdecode("/Reportes Estrategias de Extincion"))



ejecutar = SuperLuchin()