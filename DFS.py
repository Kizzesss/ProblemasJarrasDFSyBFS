from jarra import Nodo

def llenarGrande(dato_nodo, nodos_siguiente, nodos_visitados):
    if dato_nodo[0] == 0:
        hijo = [4, dato_nodo[1]]

        hijo_1 = Nodo(hijo)

        if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_siguiente):
            nodos_siguiente.append(hijo_1)
            return hijo_1


def llenarPeque(dato_nodo, nodos_siguiente, nodos_visitados):
    if dato_nodo[1] == 0:
        
        hijo = [dato_nodo[0], 3]

        hijo_2 = Nodo(hijo)

        if not hijo_2.en_lista(nodos_visitados) and not hijo_2.en_lista(nodos_siguiente):
            nodos_siguiente.append(hijo_2)
            return hijo_2


def vaciarGrande(dato_nodo, nodos_siguiente, nodos_visitados):
    if dato_nodo[0] > 0:
        
        hijo = [0, dato_nodo[1]]

        hijo_3 = Nodo(hijo)

        if not hijo_3.en_lista(nodos_visitados) and not hijo_3.en_lista(nodos_siguiente):
            nodos_siguiente.append(hijo_3)
            return hijo_3


def vaciarPeque(dato_nodo, nodos_siguiente, nodos_visitados):
    if dato_nodo[1] > 0:
        
        hijo = [dato_nodo[0], 0]

        hijo_4 = Nodo(hijo)

        if not hijo_4.en_lista(nodos_visitados) and not hijo_4.en_lista(nodos_siguiente):
            nodos_siguiente.append(hijo_4)
            return hijo_4


def traspasarGrandePeque(dato_nodo, nodos_siguiente, nodos_visitados):
    if dato_nodo[0] > 0 and dato_nodo[1] < 3:
        actual_grande = dato_nodo[0]
        actual_peque = dato_nodo[1]
        fin_grande = actual_grande
        fin_peque = actual_peque

        puedo_traspasar = 3 - actual_peque

        if puedo_traspasar > 0:
            if actual_grande <= puedo_traspasar:
                fin_peque = actual_peque + fin_grande
                fin_grande = 0

                if fin_peque > 3:
                    fin_peque = 3
            else:
                fin_peque = puedo_traspasar + actual_peque
                fin_grande = actual_grande - puedo_traspasar
                

        hijo = [fin_grande, fin_peque]

        hijo_5 = Nodo(hijo)

        if not hijo_5.en_lista(nodos_visitados) and not hijo_5.en_lista(nodos_siguiente):
            nodos_siguiente.append(hijo_5)
            return hijo_5


def traspasarPequeGrande(dato_nodo, nodos_siguiente, nodos_visitados):
    if dato_nodo[1] > 0 and dato_nodo[0] < 4:
        actual_grande = dato_nodo[0]
        actual_peque = dato_nodo[1]
        fin_grande = actual_grande
        fin_peque = actual_peque

        puedo_traspasar = 4 - actual_grande

        if puedo_traspasar > 0:
            if actual_peque <= puedo_traspasar:
                fin_grande = actual_grande + fin_peque
                fin_peque = 0

                if fin_grande > 4:
                    fin_grande = 4
            else:
                fin_grande = puedo_traspasar + actual_grande
                fin_peque = actual_peque - puedo_traspasar

        hijo = [fin_grande, fin_peque]

        hijo_6 = Nodo(hijo)

        if not hijo_6.en_lista(nodos_visitados) and not hijo_6.en_lista(nodos_siguiente):
            nodos_siguiente.append(hijo_6)
            return hijo_6


def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_siguiente = []

    # Agrego el estado inicial a la lista de nodos siguientes
    nodoInicial = Nodo(estado_inicial)
    nodos_siguiente.append(nodoInicial)

    # Mientras no se haya encontrado la solución y no se haya llegado a un estado de visitado
    while (not solucionado) and len(nodos_siguiente) != 0:
        #Sacamos el nodo que vamos a visitar
        nodo = nodos_siguiente.pop() 
        # print(nodo)
        #Agregamos el nodo visitado a la lista de visitados
        nodos_visitados.append(nodo)  

        #Si el nodo es la solucion lo marcamos como solucionado
        if nodo.get_datos()[0] == solucion[0]:
            solucionado = True

            #Recorremos la lista de visitados para obtener la solucion final
            return nodo
        else:  #Si no es la solucion, seguimos buscando
            dato_nodo = nodo.get_datos()

            
            #Llenamos el peque
            hijo_2 = llenarPeque(dato_nodo, nodos_siguiente, nodos_visitados)
            #Llenamos el grande
            hijo_1 = llenarGrande(dato_nodo, nodos_siguiente, nodos_visitados)
            #Vaciamos el grande
            hijo_3 = vaciarGrande(dato_nodo, nodos_siguiente, nodos_visitados)
            #Vaciamos el peque
            hijo_4 = vaciarPeque(dato_nodo, nodos_siguiente, nodos_visitados)
            #Traspasamos el grande a peque
            hijo_5 = traspasarGrandePeque(dato_nodo, nodos_siguiente, nodos_visitados)
            #Traspasamos el peque a grande
            hijo_6 = traspasarPequeGrande(dato_nodo, nodos_siguiente, nodos_visitados)
            #Agregamos los hijos a la lista de siguientes nodos a visitar
            listaHijos = []
            if hijo_1 != None:
                listaHijos.append(hijo_1)
            if hijo_2 != None:
                listaHijos.append(hijo_2)
            if hijo_3 != None:
                listaHijos.append(hijo_3)
            if hijo_4 != None:
                listaHijos.append(hijo_4)
            if hijo_5 != None:
                listaHijos.append(hijo_5)
            if hijo_6 != None:
                listaHijos.append(hijo_6)
                
            nodo.set_hijos(listaHijos)
            print("Padre: ",nodo)
            print("Hijos: ",hijo_1, hijo_2, hijo_3, hijo_4, hijo_5, hijo_6)
            # print(nodo)

if __name__ == '__main__':
    estado_inicial = [0, 0]
    solucion = [2, 3]

    # Buscamos la solución usando el algoritmo DFS y la imprimimos por pantalla 
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)

    # Creo una lista de todos los padres del nodo solución
    resultado = []
    nodo = nodo_solucion

    # Mientras el nodo no sea None (no es la raíz) agregamos el nodo al resultado y obtenemos el padre del nodo
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    # Agregamos la raíz al resultado y lo imprimimos
    resultado.append(estado_inicial)
    resultado.reverse()

    print("Solución: ", resultado)
