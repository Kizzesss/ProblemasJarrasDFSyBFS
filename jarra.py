class Nodo:
    def __init__(self, datos, hijos=None) -> None:
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos) -> None:
        self.hijos = hijos

        if self.hijos != None:
            for i in self.hijos:
                i.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre) -> None:
        self.padre = padre

    def set_datos(self, datos) -> None:
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_coste(self, coste) -> None:
        self.coste = coste

    def get_coste(self):
        return self.coste

    def igual(self, nodo) -> bool:
        if self.get_datos() == nodo.get_datos():
            return True

        return False

    def en_lista(self, lista_nodos) -> bool:
        en_la_lista = False

        for i in lista_nodos:
            if self.igual(i):
                en_la_lista = True

        return en_la_lista

    def __str__(self) -> str:
        return str(self.get_datos())