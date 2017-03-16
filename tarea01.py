with open("recursos.csv") as f:
    x=[]
    dicc = dict()
    for linea in f:
        x.append(linea.strip("\n").split(","))
    for base in x[1::]:
        dicc[int(base[0])]=base[1::]
    #print(dicc[2])
    dicc[2][1]=4
    #print(dicc[2][1])
    #print(dicc[2])

class usuario:

    def __init__(self,id = "",nombre = "",contrasena = "",recurso_id="",**kwargs):
        self.id = id
        self.nombre = nombre
        self.contrasena = contrasena
        self.recurso_id= recurso_id

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

class SuperLuchin:

    def __init__(self):
        self.lista_usuarios = []
        self.usuario_activo = []
        self.fecha = ""
        self.hora = ""
        self.archivos = Archivos()
        print("---- Bienvenido al Software SuperLuchin -----")

    def iniciar_sesion(self):
        self.lista_usuarios = self.archivos.cargar_usuarios()
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
        print("Estas dentro")

    def cambiar_fecha_hora(self):
        pass


ejecutar = SuperLuchin()
ejecutar.iniciar_sesion()
