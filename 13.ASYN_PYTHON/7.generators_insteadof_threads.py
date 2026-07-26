def countdown(num):
    while num > 0:
        yield num
        num -= 1


# c1 = countdown(10)
# c2 = countdown(20)

# #empezamos una tarea
# print(next(c1))
# #empezamos otra tarea mientras la primera esta parada
# print(next(c2))
# #volvemos a la primera tarea
# print(next(c1))
# #volvemos a la segunda tarea
# print(next(c2))



tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')


###explicacion de lo que es un Yield y el event loop:
'''
Va, versión corta y sin vueltas:

¿Qué es un generador?
Una función que no te da todos los resultados de golpe, sino de uno en uno, cuando se los pides.

¿Qué hace yield?
Es como un return que no mata la función: entrega un valor y la deja pausada en esa línea, con sus variables intactas.


def contar():
    yield 1   # entrega 1 y se pausa AQUÍ
    yield 2   # entrega 2 y se pausa AQUÍ
    yield 3

g = contar()    # no ejecuta NADA, solo crea el generador
next(g)  # → 1
next(g)  # → 2  (siguió desde donde se quedó)
next(g)  # → 3
next(g)  # 💥 StopIteration: ya no hay más


La analogía
Piensa en una máquina expendedora de tickets: no imprime los 100 tickets de una vez. Cada vez que aprietas el botón (next()), sale uno, y la máquina se queda esperando el siguiente botonazo, recordando en qué número va.

Eso es todo el concepto:

return → "toma el resultado, ya terminé, olvido todo".
yield → "toma un resultado, me quedo pausado aquí, llámame de nuevo para el siguiente".
Y en tu archivo, como cada generador recuerda dónde iba, puedes tener varios pausados y avanzarlos por turnos — por eso sirven para simular tareas concurrentes sin threads.

un generador que es? una funcion que yo creo que usa yield? o es el generador EN SI MISMO ?
¡Excelente pregunta! Porque en realidad son dos cosas distintas y la gente las llama igual, por eso confunde:

1. La función generadora (generator function)
Es la que tú escribes con yield adentro:


def countdown(num):      # ← esto es una FUNCIÓN GENERADORA
    while num > 0:
        yield num
        num -= 1
Es solo la receta. No guarda estado, no hace nada por sí sola.

2. El generador (generator object)
Es lo que te devuelve esa función cuando la llamas:


c1 = countdown(10)   # ← c1 es EL GENERADOR
c2 = countdown(10)   # ← c2 es OTRO generador, independiente
Este objeto es el que:

tiene el "botón de pausa" (se congela en los yield),
recuerda sus variables (num),
responde a next().
Puedes comprobarlo en Python:


type(countdown)      # <class 'function'>   ← la receta
type(countdown(10))  # <class 'generator'>  ← el objeto que se pausa
La analogía
La función generadora = el plano de la máquina de tickets.
El generador = la máquina ya construida, con su contador propio.
Por eso en tu archivo tasks = [countdown(10), countdown(5), countdown(20)] crea tres generadores a partir de la misma función: tres máquinas independientes, cada una recordando su propio número.

Resumen en una línea: la función con yield es la fábrica; el generador es el objeto que sale de llamarla, y ese es el que se pausa y reanuda.

7.generators_insteadof_threads.py#23-31
esto es como la creacion del yield, cierto? while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished') o sea esto es un yield sin yield jajaajjaa es como crearlo desde ceroo que ?
Casi, pero no exactamente 😄 Déjame ajustarte la idea:

Ese bloque no es un yield hecho desde cero — los yield ya existen dentro de countdown. Lo que ese while construye desde cero es otra cosa: el event loop (el planificador de tareas).

Son dos roles distintos:

El yield = el empleado que se pausa
Está en countdown. Es quien dice "hice un pedacito de trabajo, me pauso, aquí tienes el valor".

Tu while = el jefe que reparte turnos
No pausa nada él mismo. Su trabajo es decidir a quién le toca:


while tasks:
    task = tasks[0]          # agarra la primera tarea de la cola
    tasks.remove(task)       # la saca de la cola
    try:
        x = next(task)       # "te toca: avanza UN paso" (hasta su próximo yield)
        print(x)
        tasks.append(task)   # sigue viva → al final de la cola
    except StopIteration:
        print('Task finished')  # ya terminó → no vuelve a la cola
O sea:

yield (dentro del generador) → el mecanismo de pausarse.
Tu while (fuera) → el mecanismo de rotar entre los pausados.
Lo que sí es cierto de tu intuición: estás construyendo algo desde cero, pero no el yield, sino lo que asyncio te da gratis. En asyncio:

await hace el papel del yield (la tarea se pausa),
el event loop de asyncio hace el papel de tu while (decide quién sigue).
Entonces la frase correcta sería: "esto es un asyncio sin asyncio" — un event loop artesanal. El yield es la pausa; tu loop es el que aprovecha esas pausas para intercalar tareas. 👌
'''













# CONCLUSION:
# yield actua como un "pause button" — cada tarea avanza un paso y cede el control.
# El while las rota manualmente, simulando concurrencia sin threads ni GIL.
# Esto es exactamente el principio detras de asyncio:
# en vez de threads que se interrumpen entre si, las tareas cooperan
# y deciden ellas mismas cuando pausarse con yield (o await en asyncio).
#
# Ademas, los threads son bastante mas costosos: cada thread consume memoria propia,
# tiene overhead de creacion y destruccion, y el sistema operativo tiene que
# gestionarlos. Los generadores en cambio son objetos simples y livianos —
# puedes tener miles sin problema, mientras que miles de threads podrian
# colapsar el sistema.
    