recorrido = []

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value
        self.left = left    # Left child
        self.right = right  # Right child

entradas = []
entradas.append("S->AB|SS|AC|BD|BA")
entradas.append("A->a")
entradas.append("B->b")
entradas.append("C->SB")
entradas.append("D->SA")

def imprimir_matriz(matriz):
    for x in matriz:
        print(x)

def obtener_produccion(p_1, p_2):
    if p_1 is None or p_2 is None:
        return None
    else:
        return p_1+p_2



def generar_arbol_de_derivacion(matriz, n):
    s = matriz[0][n-1]
    root = Node(s[0])  
    generar_arbol_aux(root, s[1], s[2], matriz)

    imprimir_arbol_de_derivacion(root)

    print(recorrido)
    

def generar_arbol_aux(current: Node, l, r, matriz):
    if l is None:
        current.left = None
        current.right = None

    else:
        a = matriz[l[0]][l[1]]
        b = matriz[r[0]][r[1]]
        print(a[0], b[0])
        current.left = Node(a[0])
        current.right = Node(b[0])
        generar_arbol_aux(current.left, a[1], a[2], matriz)
        generar_arbol_aux(current.right, b[1], b[2], matriz)
        



















def imprimir_arbol_de_derivacion(root):
   
        # Base Case 
    if root is None: 
        return
      
    # Create an empty queue for level order traversal 
    queue = [] 
  
    # Enqueue Root and initialize height 
    queue.append(root) 
  
    while(len(queue) > 0): 
        # Print front of queue and remove it from queue 
        recorrido.append(queue[0].value) 
        node = queue.pop(0) 
  
        #Enqueue left child 
        if node.left is not None: 
            queue.append(node.left) 
   
        # Enqueue right child 
        if node.right is not None: 
            queue.append(node.right) 
   


cadena = list("aabbab")
print(cadena)
n = len(cadena)

producciones = {}
generadores = {}

for e in entradas: #llenado de diccionario de producciones
    generador, terminales = e.split("->")
    for terminal in terminales.split("|"):
        producciones[terminal] = generador
        generadores[generador] = terminal


matriz_sub = [[["0",None, None] for y in range(n)] for x in range(n)] #cracion de matriz de subcadenas

for i in range(n):
    matriz_sub[i][i][0] = producciones[cadena[i]]


for i in range(1, n):
    for j in range(i, n):
        for k in range(i):
            p_1 = matriz_sub[j-i][j-i+k][0]
            p_2 = matriz_sub[j-i+k+1][j][0]
            produccion = obtener_produccion(p_1, p_2)
            if produccion in producciones:
                matriz_sub[j-i][j] = [producciones[produccion], [j-i, j-i+k], [j-i+k+1, j]]
                break
            elif k == i-1:
                matriz_sub[j-i][j][0] = None


print("\n")
imprimir_matriz(matriz_sub)
print("\n")

if matriz_sub[0][n-1][0] == "S":
    print("La cadena si pertenece a la Gramatica")
    #imprimir_arbol_de_derivacion()
    generar_arbol_de_derivacion(matriz_sub, n)
else:
    print("La cadena no pertene a la gramatica")


recorrido_str = ""
for x in recorrido:
    if x == "null":
        recorrido_str += "null,"
    else:
        recorrido_str += str(ord(x)) + ","

print(recorrido_str)
