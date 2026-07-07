class NodoAmenaza:
    def __init__(self, nivel_amenaza):
        self.nivel_amenaza = nivel_amenaza  # Valor numérico de la amenaza (ej: 5 = servidor crítico)
        self.siguiente = None  # Apuntador al siguiente nodo

    def getValor(self):
        return self.nivel_amenaza  # Método para acceder al valor

class ListaAmenazas:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista

    def agregar_amenaza(self, nivel_amenaza):
        """Añade un nuevo nodo al final de la lista."""
        nuevo_nodo = NodoAmenaza(nivel_amenaza)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def contar_picos(self):
        """Retorna la cantidad de nodos que son 'picos' de amenaza (mayores que sus vecinos)."""
        if not self.cabeza or not self.cabeza.siguiente:
            return 0  # Lista vacía o con solo 1 nodo

        count = 0
        anterior = None
        actual = self.cabeza
        siguiente = actual.siguiente

        while siguiente:
            # Caso general: comparar con anterior y siguiente
            if (anterior is None or actual.getValor() > anterior.getValor()) and \
               (siguiente is None or actual.getValor() > siguiente.getValor()):
                count += 1
            anterior = actual
            actual = siguiente
            siguiente = siguiente.siguiente

        return count

    def mostrar_amenazas(self):
        """Muestra la lista de amenazas (para debugging)."""
        actual = self.cabeza
        while actual:
            print(actual.getValor(), end=" → " if actual.siguiente else "")
            actual = actual.siguiente
        print()

    # Crear lista de amenazas en sistemas ctOS
lista_dedsec = ListaAmenazas()
lista_dedsec.agregar_amenaza(3)  # Cámara de baja prioridad
lista_dedsec.agregar_amenaza(5)  # Servidor Blume (alto riesgo)
lista_dedsec.agregar_amenaza(1)  # Router desactualizado
lista_dedsec.agregar_amenaza(4)  # Base de datos con información sensible
lista_dedsec.agregar_amenaza(2)  # Dispositivo IoT
lista_dedsec.agregar_amenaza(8)  # Core de ctOS (máxima prioridad)

# Mostrar lista y picos
print("Lista de amenazas monitorizadas por DedSec:")
lista_dedsec.mostrar_amenazas()  # Output: 3 → 5 → 1 → 4 → 2 → 8

picos = lista_dedsec.contar_picos()
print(f"\n¡DedSec ha identificado {picos} puntos críticos de hackeo!")  # Output: 2 (5 y 4)