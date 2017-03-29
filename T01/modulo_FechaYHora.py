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
        if FechaYHora.comparar_fecha(fecha2,fecha1):
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
        else:
            contador = 0
        return contador
