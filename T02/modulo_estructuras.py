class Nodo:
    def __init__(self, valor=None):
        self.siguiente = None
        self.valor = valor


class Lista:
    def __init__(self, *args):
        self.cola = None
        self.cabeza = None
        for arg in args:
            self.append(arg)

    def __repr__(self):
        nodo = self.cabeza
        s = "["
        if nodo:
            s += str(nodo.valor) + ", "
        else:
            return "[]"
        while nodo.siguiente:
            nodo = nodo.siguiente
            s += str(nodo.valor) + ", "
        return s.strip(", ") + "]"

    def __getitem__(self, index):
        nodo = self.cabeza
        for i in range(index):
            if nodo:
                nodo = nodo.siguiente
            else:
                raise IndexError
        if not nodo:
            raise IndexError
        else:
            return nodo.valor

    def __in__(self, valor):
        for elemento in self:
            if elemento == valor:
                return True
        return False

    def append(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            self.cola.siguiente = Nodo(valor)
            self.cola = self.cola.siguiente

    def clear(self):
        self.cabeza = None
        self.cola = None

    def __len__(self):
        contador = 0
        for elemento in self:
            contador += 1
        return contador


    def sort(self, reverse=False):
        lista_aux = self
        lista_aux1 = Lista()
        for i in range(len(self)):
            if reverse:
                elemento = max(lista_aux)
            else:
                elemento = min(lista_aux)
            lista_aux1.append(elemento)
            lista_aux.borrar(elemento)
        self.clear()
        for cosa in lista_aux1:
            self.append(cosa)


    def borrar(self, value):
        contador = True
        contador2 = False
        elemento = self.cabeza
        elemento1 = None
        if len(self)>1:
            while contador:
                if elemento.valor == value and contador2 == False:
                    if elemento.siguiente and elemento != self.cabeza:
                        elemento.valor = elemento.siguiente.valor
                        elemento1 = elemento
                        elemento = elemento.siguiente
                        contador2 = True
                    elif elemento.siguiente and elemento == self.cabeza:
                        self.cabeza = elemento.siguiente
                        contador = False
                    else:
                        elemento1.siguiente = None
                        self.cola = elemento1
                        contador = False
                elif contador2 and elemento.siguiente != None:
                    elemento.valor = elemento.siguiente.valor
                    elemento1 = elemento
                    elemento = elemento.siguiente
                elif contador2 and elemento.siguiente == None:
                    elemento1.siguiente = None
                    self.cola = elemento1
                    contador = False
                else:
                    elemento1 = elemento
                    elemento = elemento.siguiente
        else:
            self.clear()
    def pop(self):
        if len(self)>1:
            contador = 0
            elemento = self.cabeza
            for i in range(len(self)):
                if contador == len(self)-2:
                    sacado = elemento.siguiente
                    elemento.siguiente = None
                    self.cola = elemento
                    return sacado.valor
                else:
                    elemento = elemento.siguiente
                    contador += 1
        else:
            valor = self.cabeza.valor
            self.clear()
            return valor

    def contar(self, valor):
        contador = 0
        for elemento in self:
            if elemento == valor:
                contador += 1
        return contador

    def __setitem__(self, key, value):
        if key > (len(self)-1):
            raise IndexError
        contador = 0
        elemento = self.cabeza
        for i in range(len(self)):
            if contador == key:
                elemento.valor = value
            else:
                contador +=1
                elemento = elemento.siguiente
