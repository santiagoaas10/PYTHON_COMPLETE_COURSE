from collections import deque

friends = deque(('rolf', 'santi', 'ana', 'jose'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield 
        print(f'{greeting} {friend}')

def greet(g):
    g.send(None) #todo estode la linea 12 a la 15 se puede resumir en un "add yield from g", aunque no es bien visto
    while True:
        greeting = yield
        g.send(greeting)

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

# PIPELINE DE GENERADORES:
# tu codigo -> greet() -> friend_upper()
#
# greet() es un intermediario: recibe el saludo desde afuera con yield
# y lo reenvía adentro con g.send(greeting) a friend_upper().
# friend_upper() toma el nombre, lo pone en mayusculas, y espera
# el saludo para imprimir el resultado.
#
# El send(None) inicial hace el priming de ambos generadores en cadena:
# greet() hace el priming de friend_upper() internamente,
# y tu haces el priming de greet() desde afuera.
#
# POR QUE ESTO SE LLAMA CORRUTINA:
# Un generador normal solo entrega valores hacia afuera (yield).
# Cuando un generador tambien RECIBE valores desde afuera (yield + .send()),
# se convierte en una CORRUTINA — una funcion que puede pausarse,
# ceder el control, y luego reanudarse con nuevos datos.
# La diferencia clave es la comunicacion bidireccional:
#   generador normal:  datos fluyen solo hacia afuera  ->
#   corrutina:         datos fluyen en ambas direcciones <->
# asyncio formalizo esto con async/await, donde cada "await"
# es exactamente un yield que pausa la corrutina y espera datos externos.
#
# POR QUE ES BIDIRECCIONAL:
# Una funcion normal solo va en una direccion:
#   def suma(a, b):
#       return a + b
#   -> tu le mandas datos, ella responde, se acaba.
#
# Una corrutina puede tener una conversacion:
#   g.send(None)     # tu: "arranca"
#   g.send('Hello')  # tu: "toma este saludo"
#   g.send('Hi')     # tu: "ahora toma este otro"
#   g.send('Hey')    # tu: "y este otro..."
# Cada send entra a la funcion, ella lo procesa, y vuelve a pausarse
# esperando el siguiente. No termina — sigue viva esperando mas datos.
#
# Una direccion   = tu mandas, funcion responde, se acaba.
# Bidireccional   = tu mandas, funcion procesa, se pausa, tu mandas de nuevo... indefinidamente.
# Es una conversacion de ida y vuelta en vez de una llamada de una sola vez.