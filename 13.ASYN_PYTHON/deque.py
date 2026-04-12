# ============================================================
# DEQUE (Double Ended Queue)
# ============================================================
# Una deque es una cola de doble entrada — puedes agregar y
# quitar elementos tanto por el INICIO como por el FINAL,
# y ambas operaciones son O(1) (instantaneas).
#
# Una lista normal tambien puede hacerlo, pero insertar/quitar
# al inicio es O(n) porque tiene que mover todos los elementos.
# La deque esta optimizada para exactamente eso.
# ============================================================

from collections import deque

# ------------------------------------------------------------
# EJEMPLO 1: Operaciones basicas
# ------------------------------------------------------------

d = deque([1, 2, 3])
print("deque inicial:", d)

d.append(4)        # agrega al final
d.appendleft(0)    # agrega al inicio
print("despues de append y appendleft:", d)  # deque([0, 1, 2, 3, 4])

d.pop()            # quita del final
d.popleft()        # quita del inicio
print("despues de pop y popleft:", d)  # deque([1, 2, 3])


# ------------------------------------------------------------
# EJEMPLO 2: deque con maxlen (tamano maximo)
# ------------------------------------------------------------
# Cuando le pones un limite, al agregar un elemento nuevo
# el del lado contrario se descarta automaticamente.
# Util para guardar los ultimos N elementos (historial, logs, etc.)

historial = deque(maxlen=3)
historial.append("pagina 1")
historial.append("pagina 2")
historial.append("pagina 3")
print("\nhistorial:", historial)  # deque(['pagina 1', 'pagina 2', 'pagina 3'])

historial.append("pagina 4")  # pagina 1 se descarta automaticamente
print("despues de agregar pagina 4:", historial)  # deque(['pagina 2', 'pagina 3', 'pagina 4'])


# ------------------------------------------------------------
# EJEMPLO 3: rotate — rotar elementos
# ------------------------------------------------------------
# rotate(n) mueve n elementos del final al inicio
# rotate(-n) mueve n elementos del inicio al final

d = deque([1, 2, 3, 4, 5])
d.rotate(2)   # mueve los 2 ultimos al inicio
print("\nrotate(2):", d)   # deque([4, 5, 1, 2, 3])

d.rotate(-2)  # mueve los 2 primeros al final
print("rotate(-2):", d)   # deque([1, 2, 3, 4, 5])


# ============================================================
# RESUMEN
# ============================================================
# - append / appendleft  -> agrega al final / inicio  O(1)
# - pop / popleft        -> quita del final / inicio  O(1)
# - maxlen               -> descarta automaticamente el lado opuesto
# - rotate               -> rota los elementos
# - Ideal para: colas, historiales, buffers, sliding windows
# ============================================================
