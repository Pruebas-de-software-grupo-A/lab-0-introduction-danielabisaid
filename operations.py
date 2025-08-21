def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # BUG 1: división entre 0 no controlada
    return a / b  

def potencia(a, b):
    # BUG 2: error lógico, debería ser a ** b
    return a ^ b  

def raiz_cuadrada(x):
    # BUG 3: no maneja negativos, lanza error en math.sqrt
    import math
    return math.sqrt(x)

def promedio(lista):
    # BUG 4: si la lista está vacía, ZeroDivisionError
    return sum(lista) / len(lista)

def maximo(lista):
    # BUG 5: regresa el mínimo en vez del máximo
    return min(lista)


# Programa principal para pruebas
if __name__ == "__main__":
    print("Suma:", sumar(2, 3))          # ok

