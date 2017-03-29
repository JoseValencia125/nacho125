import math

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
        self.fecha_llegada_base = ""
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
            self.potencia = 0
            return "apagado"

    @property
    def porcentaje_de_extincion(self):
        if self.puntos_poder != 0:
            return float(self.puntos_poder_extintos) / float(self.puntos_poder_historios)

        else:
            return "100%"

    @property
    def puntos_poder(self):
        return ((math.pi * ((self.radio * 1000) ** 2)) * self.potencia) - self.puntos_poder_extintos

    @property
    def puntos_poder_historios(self):
        return ((math.pi * ((self.radio * 1000) ** 2)) * self.potencia)

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

