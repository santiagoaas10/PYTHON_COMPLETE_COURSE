primos=[]
for i in range(2,10):
    for x in range (2,i): #2
        if i%x == 0:
            print(f"{i} es igual a {x} * {i//x}")
            break
    else: #si nunca hace el break, nuca va al else, estructura for else
        print(f"{i} es primo")
        primos.append(i)
print(primos)
