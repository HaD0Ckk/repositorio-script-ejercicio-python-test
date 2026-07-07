def ordenar_prioridades(p1, p2, p3):
    # Pila 3 almacenará el resultado ordenado (tope = mínimo)
    while not p1.esta_vacia():
        # Paso 1: Encontrar el mínimo en P1 y moverlo a P3
        minimo = float('inf')
        
        # Mover todos los elementos de P1 a P2, registrando el mínimo
        while not p1.esta_vacia():
            num = p1.pop()
            if num < minimo:
                minimo = num
            p2.push(num)
        
        # Mover de P2 a P1, excepto el mínimo (que va a P3)
        while not p2.esta_vacia():
            num = p2.pop()
            if num == minimo:
                p3.push(num)  # Guardar el mínimo en P3
            else:
                p1.push(num)  # Volver a P1 para reprocesar
    
    # Paso 2: P3 tiene los elementos ordenados en orden inverso (tope = menor)
    # Si se necesita el tope = mayor, mover todo a P1
    while not p3.esta_vacia():
        p1.push(p3.pop())
    
    return p1  # Ahora P1 está ordenada de menor a mayor (tope = mínimo)

# Crear las pilas (P1 = objetivos desordenados, P2 y P3 vacías)
p1 = Pila()
p2 = Pila()
p3 = Pila()

# Objetivos de hackeo (ej: 5 = servidor Blume, 1 = router débil)
p1.push(5)
p1.push(3)
p1.push(1)
p1.push(4)
p1.push(2)
p1.push(8)

print("Pila 1 (antes):", p1.mostrar())  # [5, 3, 1, 4, 2, 8] (tope = 5)

# Ordenar
p1_ordenada = ordenar_prioridades(p1, p2, p3)

print("Pila 1 (después):", p1_ordenada.mostrar())  # [1, 2, 3, 4, 5, 8] (tope = 1)