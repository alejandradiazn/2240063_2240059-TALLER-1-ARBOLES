#Árbol realizado con listas junto a sus correspondientes características.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

#El orden máximo permitido corresponde al "orden" y orden grado máximo alcanzado corresponde al "grado".
class Arbol:
    def __init__(self, valorRaiz, ordenMaximo):
        self.raiz = Nodo(valorRaiz)
        self.ordenMaximo = ordenMaximo

    

    def agregarNodo(self, valor, padre):
        if padre is None:
            if self.raiz is None:
                nuevo_nodo = Nodo(valor)
                self.raiz = nuevo_nodo
            else:
                print("Debes tener una raíz para el árbol.")
        else:
            padre = self.buscarNodo(self.raiz, padre)
            if padre:
                if len(padre.hijos) < self.ordenMaximo:
                    padre.hijos.append(Arbol(valor, self.ordenMaximo))
                else:
                    print(f"El nodo {padre.valor} ya tiene el número máximo de hijos permitido ({self.ordenMaximo}).")
            else:
                print(f"No se encontró el nodo padre con valor {padre}.")
            
    def buscarNodo(self, nodo_actual, valor_buscado):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == valor_buscado:
            return nodo_actual
        for hijo_arbol in nodo_actual.hijos:  
            resultado = self.buscarNodo(hijo_arbol.raiz, valor_buscado)  
            if resultado:
                return resultado
        return None
                    


    def imprimirArbol(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        print(nodo.valor)
        for hijo_arbol in nodo.hijos:
            self.imprimirArbol(hijo_arbol.raiz)

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        
        if len(nodo.hijos) == 0:
            return 1
        else:
            altura_hijos = []
            for hijo in nodo.hijos:
                altura_hijos.append(self.altura(hijo.raiz))
            return 1 + max(altura_hijos)
        

    def peso(self, nodo = None):
        if nodo is None:
            nodo = self.raiz
        totalNodos = 1
        for hijo in nodo.hijos:
            totalNodos += self.peso(hijo.raiz)
        return totalNodos


    def orden(self, nodo= None):
        if nodo is None:
            nodo = self.raiz
        maxHijos = len(nodo.hijos)
        for hijo in nodo.hijos:
            maxHijos = max(maxHijos, self.orden(hijo.raiz))   
        return maxHijos


#Fragmento expuesto en consola.


print("CREACIÓN DE ÁRBOL")
valorRaiz = input("Ingrese el valor del nodo raiz: ")
orden_max = int(input("Ingrese el orden máximo permitido (número máximo de hijos por nodo): "))
arbol1 = Arbol(valorRaiz, orden_max)

while True:
    inpt = input("Ingrese el valor de un nodo y el valor de su padre separados por una coma o 'fin' para dejar de agregar nodos: ")
    if inpt == "fin":
        break
    else:
        if "," in inpt:
            partes = inpt.split(",")
            if len(partes) ==2:
                hijo = partes[0]
                padre = partes[1]
            arbol1.agregarNodo(hijo, padre)

print("\nÁRBOL EN RECORRIDO PREORDEN.")
arbol1.imprimirArbol()

print("\nCARACTERÍSTICAS DEL ÁRBOL.")
print(f"Peso del arbol: {arbol1.peso()}")
print(f"Altura del arbol: {arbol1.altura()}")
print(f"Orden (grado máximo alcanzado): {arbol1.orden()}")
print(f"Orden máximo permitido: {arbol1.ordenMaximo}")




