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
    