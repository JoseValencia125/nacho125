class usuario:

    def __init__(self,id = "",nombre = "",contrasena = "",recurso_id="",**kwargs):
        self.id = id
        self.nombre = nombre
        self.contrasena = contrasena
        self.recurso_id= recurso_id

class Recurso:

    def __init__(self,id = "", tipo = "", velocidad = "", lat = "", lon = "", autonomia = "", delay = "", tasa_extincion = "", costo = "", **kwargs):
        self.id = id
        self.tipo = tipo
        self.velocidad = velocidad
        self.lat = lat
        self.lon = lon
        self.autonomia = autonomia
        self.delay = delay
        self.tasa_extincion = tasa_extincion
        self.costo = costo


class Archivos:

     def __init__(self):
         pass

     def cargar_usuarios(self):
         self.lista_usuarios = []
         primera_linea = []
         llaves_columnas = []
         with open("usuarios.csv")as archivo_usuarios:
             contador = 0
             for linea in archivo_usuarios:
                 if contador < 1:
                     primera_linea = (linea.strip("\n").split(","))
                     contador += 1
                     for columna in primera_linea:
                         llaves_columnas.append(columna.split(":")[0])
                 else:
                     id_usuario = linea.strip("\n").split(",")[llaves_columnas.index("id")]
                     contrasena_usuario = linea.strip("\n").split(",")[llaves_columnas.index("contraseña")]
                     nombre_usuario = linea.strip("\n").split(",")[llaves_columnas.index("nombre")]
                     recurso_usuario = linea.strip("\n").split(",")[llaves_columnas.index("recurso_id")]
                     usuario1 = usuario(id=id_usuario, nombre=nombre_usuario, contrasena=contrasena_usuario,
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
                     recurso1 = Recurso(id = id_recurso,tipo = tipo,lat = lat,lon = lon,autonomia = autonomia, delay =delay, tasa_extincion = tasa_extincion, costo = costo)
                     self.lista_recursos.append(recurso1)
         return self.lista_recursos

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
                if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 != 0):
                    self.anio = anio
                    self.bisiesto = True
                    print(self.anio)
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
            mes=(input("ingrese mes en formato numero (ej: marzo = 3): "))
            try:
                val = int(mes)
                mes = int(mes)
                meses = [1,2,3,4,5,6,7,9,10,11,12]
                self.mes= mes
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
                if self.mes in [1,3,5,7,8,10,12]:
                    if dia in range(1,32):
                        self.dia = dia
                        self.contador = False
                        return self.dia
                    else:
                        print("Dia no valido, debe estar entre 1:31")
                elif self.mes in [4,6,9,11]:
                    if dia in range(1,31):
                        self.dia = dia
                        self.contador = False
                        return self.dia
                    else:
                        print("Dia no valido, debe estar entre 1:30")
                elif self.mes in [2]:
                    if self.bisiesto:
                        if dia in range(1,30):
                            self.dia = dia
                            self.contador = False
                            return self.dia
                        else:
                            print("Dia no valido, debe estar entre 1:29")
                    else:
                        if dia in range(1,29):
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
                if hora in range(0,24):
                    if hora//10 == 0:
                        hora = "0"+str(hora)
                    minuto = input("Ingrese minuto (0:59) ")
                    try:
                        val = int(minuto)
                        minuto = int(minuto)
                        if minuto in range(0,59):
                            if minuto//10 == 0:
                                minuto = "0"+str(minuto)
                            self.hora = "{0}:{1}:00".format(hora,minuto)
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

class SuperLuchin:

    def __init__(self):
        self.lista_usuarios = []
        self.usuario_activo = []
        self.lista_recursos = []
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
        print (mensaje+mensaje1)
        self.cambiar_fecha_hora()
        self.menu()

    def cambiar_fecha_hora(self):
        self.anio=self.fecha.ver_anio()
        self.mes = self.fecha.ver_mes()
        self.dia = self.fecha.ver_dia()
        self.fecha_actual = ("{2}-{1}-{0}".format(self.dia,self.mes,self.anio))
        self.hora_actual = self.fecha.ver_hora()

    def menu(self):
        opcion = input("Ingrese alguna opcion: ")

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

ejecutar = SuperLuchin()