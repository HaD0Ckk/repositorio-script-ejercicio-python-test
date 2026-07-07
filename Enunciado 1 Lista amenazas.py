class NodoAmenaza:
    def __init__(self, nivel_amenaza):
        self.nivel_amenaza = nivel_amenaza
        self.siguiente = None

    def getValor(self):
        return self.nivel_amenaza
        
class ListaAmenazas:
    def __init__(self):
        self.cabeza = None

    def agregar_amenaza(self, nivel_amenaza):
        nuevo_nodo = NodoAmenaza(nivel_amenaza)
        if not self.cabeza:
            self.cabeza = nuevo_nodo

        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def contar_picos(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return 0
        
        contador= 0
        ant = None
        actual = self.cabeza
        siguiente = actual.siguiente 

        while siguiente:
            if (ant is None or actual.getValor() > ant.getValor()) and \
               (siguiente is None or actual.getValor() > siguiente.getValor()):
                contador=+ 1
                ant = actual
                actual = siguiente
                siguiente = siguiente.siguiente
        return contador
    
    def mostrar_amenazas(self):
        actual = self.cabeza
        while actual:
            print(actual.getValor(), end= "->" if actual.siguiente else "")
            actual = actual.siguiente
        print()

lista_dedsec = ListaAmenazas()
lista_dedsec.agregar_amenaza(3)  # Cámara de baja prioridad
lista_dedsec.agregar_amenaza(5)  # Servidor Blume (alto riesgo)
lista_dedsec.agregar_amenaza(1)  # Router desactualizado
lista_dedsec.agregar_amenaza(4)  # Base de datos con información sensible
lista_dedsec.agregar_amenaza(2)  # Dispositivo IoT
lista_dedsec.agregar_amenaza(8)  # Core de ctOS (máxima prioridad)

print("Lista de amenazas monitorizadas por DedSec:")
lista_dedsec.mostrar_amenazas()  # Output: 3 → 5 → 1 → 4 → 2 → 8
picos = lista_dedsec.contar_picos()
print(f"\n¡DedSec ha identificado {picos} puntos críticos de hackeo!")  # Output: 2 (5 y 4)

