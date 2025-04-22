from bigtree import Node
from bigtree import print_tree

#Nodo Raíz
raiz = Node(1)

#Nodos hijos de Raíz
nodo_2 = Node(2, parent=raiz)
nodo_3 = Node(3, parent=raiz)
nodo_4 = Node(4, parent=raiz)

#Nodos hijos de 2
nodo_5= Node(5, parent=nodo_2)
nodo_6 = Node(6, parent=nodo_2)

#Nodos hijos de 3
nodo_7= Node(7, parent=nodo_3)
nodo_8 = Node(8, parent=nodo_3)

#Nodos hijos de 4
nodo_9= Node(9, parent=nodo_4)
nodo_10 = Node(10, parent=nodo_4)
nodo_11= Node(11, parent=nodo_4)
nodo_12= Node(12, parent=nodo_4)

print("EJEMPLIFICACIÓN DE EJECUCIÓN ÁRBOL MEDIANTE BIG TREE.")
print_tree(raiz)