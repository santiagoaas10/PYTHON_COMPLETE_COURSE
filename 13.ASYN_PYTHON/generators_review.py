# ============================================================
# GENERADORES EN PYTHON
# ============================================================
# Un generador es una funcion especial que en vez de "return" usa "yield".
# La diferencia clave: un generador NO calcula todo de una vez,
# sino que produce los valores UNO A UNO, bajo demanda (lazy evaluation).
#
# Esto los hace muy eficientes en memoria, porque no guardan
# todos los valores en una lista gigante.
# ============================================================


# ------------------------------------------------------------
# EJEMPLO 1: Funcion normal vs generador
# ------------------------------------------------------------

def numeros_normal():
    # Calcula TODO de una vez y devuelve una lista completa
    resultado = []
    for i in range(5):
        resultado.append(i)
    return resultado

def numeros_generador():
    # Produce un valor a la vez, cuando se lo piden
    for i in range(5):
        yield i  # "pausa" la funcion aqui y entrega el valor

print("--- Funcion normal ---")
print(numeros_normal())  # [0, 1, 2, 3, 4] -> lista completa en memoria

print("--- Generador ---")
print(numeros_generador())  # <generator object ...> -> NO es una lista

# Para obtener los valores de un generador, hay que iterarlo:
for n in numeros_generador():
    print(n)


# ------------------------------------------------------------
# EJEMPLO 2: Como funciona yield paso a paso
# ------------------------------------------------------------

def contador():
    print("Inicio")
    yield 1
    print("Despues del primer yield")
    yield 2
    print("Despues del segundo yield")
    yield 3
    print("Fin")

print("\n--- Demostracion de yield ---")
gen = contador()       # crea el generador, pero NO ejecuta nada todavia
print(next(gen))       # ejecuta hasta el primer yield -> imprime "Inicio" y devuelve 1
print(next(gen))       # continua hasta el segundo yield -> devuelve 2
print(next(gen))       # continua hasta el tercer yield -> devuelve 3
# Si llamas next() una vez mas, lanza StopIteration porque ya no hay mas yields


# ------------------------------------------------------------
# EJEMPLO 3: Ventaja de memoria
# ------------------------------------------------------------
# Imagina que quieres procesar 10 millones de numeros.
# Con una lista, tendrias 10 millones de numeros en memoria.
# Con un generador, solo tienes UNO a la vez.

def millones_lista():
    return [x**2 for x in range(10_000_000)]  # gasta MUCHA memoria

def millones_generador():
    for x in range(10_000_000):
        yield x**2  # gasta muy poca memoria

# El generador es ideal cuando procesas datos grandes uno por uno
print("\n--- Procesando con generador ---")
gen = millones_generador()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
# Solo se calculan los que necesitas, no los 10 millones


# ------------------------------------------------------------
# EJEMPLO 4: Generator expression (version corta)
# ------------------------------------------------------------
# Igual que una list comprehension pero con parentesis en vez de corchetes

lista = [x*2 for x in range(5)]        # list comprehension -> [0, 2, 4, 6, 8]
generador = (x*2 for x in range(5))    # generator expression -> objeto generador

print("\n--- Generator expression ---")
print(lista)
print(generador)
for valor in generador:
    print(valor)


# ------------------------------------------------------------
# EJEMPLO 5: Caso practico - leer un archivo grande linea por linea
# ------------------------------------------------------------
# Si el archivo pesa 10GB, NO puedes cargarlo entero en memoria.
# Un generador te permite procesarlo linea por linea.

def leer_archivo_grande(ruta):
    with open(ruta) as archivo:
        for linea in archivo:
            yield linea.strip()  # entrega una linea a la vez

# uso:
# for linea in leer_archivo_grande("archivo_enorme.txt"):
#     procesar(linea)  # solo una linea en memoria a la vez


# ============================================================
# RESUMEN
# ============================================================
# - yield pausa la funcion y devuelve un valor
# - next() reanuda la ejecucion hasta el siguiente yield
# - Los generadores son perezosos (lazy): calculan bajo demanda
# - Ahorran memoria porque no guardan todos los valores
# - Ideales para: archivos grandes, streams de datos, secuencias infinitas
# ============================================================
