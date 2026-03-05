def is_valid(cad):
    stack = []
    maps = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for c in cad: 
        if c in maps.values():# si es apertura
            stack.append(c)
        elif c in mapping: #si es cierre
            if not stack or stack[-1] != maps[c]:
                return False
            stack.pop()

    return len(stack) == 0


def es_palindromo(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def es_anagrama(palabra1, palabra2):
    
    # Normalizamos: todo minúscula y sin espacios
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    
    # Si tienen diferente longitud, imposible ser anagrama
    if len(palabra1) != len(palabra2):
        return False
    
    # Contar letras de palabra1
    conteo1 = {}
    for letra in palabra1:
        if letra in conteo1:
            conteo1[letra] = conteo1[letra] + 1
        else:
            conteo1[letra] = 1
    
    # Contar letras de palabra2
    conteo2 = {}
    for letra in palabra2:
        if letra in conteo2:
            conteo2[letra] = conteo2[letra] + 1
        else:
            conteo2[letra] = 1
    
    # Si los conteos son iguales → anagrama
    return conteo1 == conteo2