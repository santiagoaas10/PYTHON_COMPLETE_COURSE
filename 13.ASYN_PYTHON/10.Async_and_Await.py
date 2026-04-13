from collections import deque
from types import coroutine

friends = deque(('rolf', 'santi', 'ana', 'jose'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield 
        print(f'{greeting} {friend}')

async def greet(g):
    print("starting")
    await g #esto espera a que todo el loop de friend upper se termien, pero se puede parar a la mitad, por el yield que hay en la linea 10, Y se termina cuando toooodo el array de friends se acabe, mire que si por ejemplo solo mando 2 saludos, aun me quedarian faltando ana y josey el ending no se imprimiria. pa que el entding se imprima tengo que mandar 4 saludos
    print("ending")

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
greeter.send('Holaa')
greeter.send('chaoo')
#greeter.send('hasta luego') este si lo acabaria
# ¿Qué es async def?
# Es azúcar sintáctica para decir "esta función es una corrutina". Internamente Python la convierte en un generador que puede pausarse y reanudarse — exactamente lo que hiciste a mano antes.

# ¿Qué es await?
# Es azúcar sintáctica para yield from. Le dice a la corrutina:

# Pausa aquí
# Delega el control a la corrutina g
# Reanúdate cuando g termine


# Exacto, es parte del mismo await.
# Cuando haces await g, Python delega todo a g — no solo espera, sino que también le reenvía automáticamente cualquier .send() que reciba greet.

# async def greet(g):
#     await g   # todo lo que entre por .send() a greet, 
#               # se reenvía automaticamente a g (friend_upper)
# Entonces cuando haces:
# greeter.send('Hello')
# El flujo es:
# .send('Hello') → greet → await g → friend_upper recibe 'Hello'
# await hace el trabajo que antes hacías a mano en 9b: