from modulo_FechaYHora import FechaYHora
from objetos_personas import Usuario
from objetos_personas import Incendio
from objetos_personas import Recurso
from objetos_personas import Meteorologia

class Archivos:
    def __init__(self):
        self.primera_linea_usuarios = ""
        self.primera_linea_incendios = ""
        self.primera_linea_recursos = ""
        self.primera_linea_metereologia = ""
        # esta lista es para almacenar datos de incendios en caso de que se entre en pasado
        self.datos_incendios = []

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
                    lista_linea = linea.strip("\n").split(";")
                    if lista_linea[0] == "recurso":
                        for recurso in lista_recursos:
                            if str(recurso.id) == str(lista_linea[2]) and lista_linea[1] != "":
                                fecha_guardado = lista_linea[1]
                                if FechaYHora.comparar_fecha(fecha_actual, fecha_guardado):
                                    recurso.lat_actual = float(lista_linea[3])
                                    recurso.lon_actual = float(lista_linea[4])
                                    recurso.total_horas_trabajadas = lista_linea[5]
                                    recurso.horas_trabajadas = float(lista_linea[6])
                                    recurso.estado = lista_linea[7]
                                    recurso.fecha_inicio = lista_linea[8]
                                    recurso.fecha_llegada = lista_linea[9]
                                    recurso.fecha_salida_incendio = lista_linea[10]
                                    recurso.id_incendio_asignado = lista_linea[11]
                                    recurso.distancia_objetivo = float(lista_linea[12])
                                    recurso.distancia_recorrida = float(lista_linea[13])
                                    recurso.puntos_apagados = float(lista_linea[14])
                                    recurso.fecha_ultima_ejecucion = lista_linea[15]
                                    recurso.autonomia_restante = float(lista_linea[16])
                    elif lista_linea[0] == "incendio":
                        for incendio in lista_incendios:
                            if str(incendio.id) == str(lista_linea[2]) and lista_linea[1] != "":
                                fecha_guardado = lista_linea[1]
                                if FechaYHora.comparar_fecha(fecha_actual, fecha_guardado):
                                    incendio.fecha_ultimo_recurso = lista_linea[1]
                                    incendio.id = lista_linea[2]
                                    incendio.radio = float(lista_linea[3])
                                    incendio.horas_ya_simuladas = []
                                    horas = lista_linea[4].split(",")
                                    for hora in horas:
                                        incendio.horas_ya_simuladas.append(hora)
                                    incendio.recursos_usados = []
                                    recursos_usados = lista_linea[5].split(",")
                                    for recurso in recursos_usados:
                                        incendio.recursos_usados.append(recurso)
                                    incendio.puntos_poder_extintos = float(lista_linea[6])
                                    incendio.ultima_condicion = lista_linea[7]
                                    incendio.fecha_apagado = lista_linea[8]
                                    incendio.fecha_ultima_simulacion = lista_linea[9]
                                    self.datos_incendios.append(incendio)
        except FileNotFoundError:
            return None

    def sobreescribir_simulacion(self, lista_incendios, lista_recursos):
        archivo = open("datos_simulacion.txt", "w")
        # este for es para recuperar datos incendios pasados
        for incendio in self.datos_incendios:
            fila = ""
            fila += "incendio" + ";"
            fila += str(incendio.fecha_ultimo_recurso) + ";"
            fila += str(incendio.id) + ";"
            fila += str(incendio.radio) + ";"
            fila += str(incendio.horas_ya_simuladas) + ";"
            fila += str(incendio.recursos_usados) + ";"
            fila += str(incendio.puntos_poder_extintos) + ";"
            fila += str(incendio.ultima_condicion) + ";"
            fila += str(incendio.fecha_apagado) + ";"
            fila += str(incendio.fecha_ultima_simulacion) + "\n"
            archivo.write(fila)
        for incendio in lista_incendios:
            fila = ""
            if len(incendio.recursos_usados) > 0:
                fila += "incendio" + ";"
                fila += str(incendio.fecha_ultimo_recurso) + ";"
                fila += str(incendio.id) + ";"
                fila += str(incendio.radio) + ";"
                fila += str(incendio.horas_ya_simuladas) + ";"
                fila += str(incendio.recursos_usados) + ";"
                fila += str(incendio.puntos_poder_extintos) + ";"
                fila += str(incendio.ultima_condicion) + ";"
                fila += str(incendio.fecha_apagado) + ";"
                fila += str(incendio.fecha_ultima_simulacion) + "\n"
                archivo.write(fila)
        for recursos in lista_recursos:
            fila = ""
            if recursos.total_horas_trabajadas > 0 or recursos.estado != "stanby":
                fila += "recurso" + ";"
                fila += recursos.fecha_llegada_base + ";"
                fila += recursos.id + ";"
                fila += str(recursos.lat_actual) + ";"
                fila += str(recursos.lon_actual) + ";"
                fila += str(recursos.total_horas_trabajadas) + ";"
                fila += str(recursos.horas_trabajadas) + ";"
                fila += str(recursos.estado) + ";"
                fila += recursos.fecha_inicio + ";"
                fila += recursos.fecha_llegada + ";"
                fila += recursos.fecha_salida_incendio + ";"
                fila += str(recursos.id_incendio_asignado) + ";"
                fila += str(recursos.distancia_objetivo) + ";"
                fila += str(recursos.distancia_recorrida) + ";"
                fila += str(recursos.puntos_apagados) + ";"
                fila += str(recursos.fecha_ultima_ejecucion) + ";"
                fila += str(recursos.autonomia_restante) + "\n"
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

