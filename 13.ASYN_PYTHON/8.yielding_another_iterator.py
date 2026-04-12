from collections import deque

friends = deque(('rolf', 'santi', 'ana', 'jose'))

def get_friend():
    yield from friends 

c = get_friend()
print(next(c))
print(next(c))


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'Hello from {friend}'
        except StopIteration:
            pass

friends_generator = get_friend()
g = greet(friends_generator)
print(next(g))
print(next(g))

# NOVEDADES DE ESTE CODIGO:
#
# 1. yield from — en vez de iterar manualmente con un for loop,
#    "delega" el yield a cada elemento del iterable directamente.
#    Es mas limpio y funciona con cualquier iterable (listas, deques, generadores, etc.)
#
# 2. Generadores anidados — get_friend() produce nombres uno a uno,
#    y greet() consume ese generador internamente con next(g),
#    transformando cada valor antes de entregarlo.
#    Un generador alimenta a otro, formando un pipeline:
#
#    friends (deque) -> get_friend() -> greet() -> resultado final
#
#    Esto es muy poderoso: cada capa transforma los datos sin cargar
#    todo en memoria, solo bajo demanda.