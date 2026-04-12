def simple_gen(num):
    while num > 0:
        yield num
        num -= 1


c1 = simple_gen(10)
c2 = simple_gen(20)

#empezamos una tarea
print(next(c1))
#empezamos otra tarea mientras la primera esta parada
print(next(c2))
#volvemos a la primera tarea
print(next(c1))
#volvemos a la segunda tarea
print(next(c2))

