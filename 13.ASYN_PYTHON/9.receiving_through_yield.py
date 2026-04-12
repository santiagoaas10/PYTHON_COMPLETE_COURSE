def greet():
    friend = yield
    print(f'Hello, {friend}')

g = greet()
g.send(None) # PRIMING — arranca el generador hasta el primer yield y lo pausa ahi.
             # Es obligatorio como PRIMER llamado porque el generador aun no esta
             # pausado en ningun yield, no hay donde recibir un valor todavia.
             # next(g) hace exactamente lo mismo, es solo otra forma de escribirlo.
g.send('Adam') # .send(valor) manda un valor AL yield donde el generador esta pausado.
               # friend = 'Adam', el generador se reanuda y ejecuta el print.

# POR QUE ESTO ES LA BASE DE ASYNCIO:
#
# yield normalmente entrega valores hacia afuera.
# Pero aqui yield tambien RECIBE valores desde afuera con .send().
# Esto permite que una funcion se pause y espere a que alguien
# le mande datos cuando esten listos.
#
# asyncio usa exactamente este mecanismo por dentro:
#   resultado = yield tarea_io
#   -> el generador se pausa y cede el control
#   -> cuando el I/O termina, el event loop hace .send(resultado)
#   -> el generador se reanuda con el resultado ya disponible
#
# SCHEDULER:
# Un scheduler es un coordinador que decide que tarea corre en cada momento.
# Lleva registro de todas las tareas pausadas y les da turno una por una.
# El event loop de asyncio ES un scheduler:
# tiene una lista de corrutinas pausadas en yield/await,
# y cuando una tarea I/O termina, hace .send() para reanudarla.
# Es lo mismo que el while loop manual de 7.generators_insteadof_threads.py,
# pero formalizado y mucho mas sofisticado.

