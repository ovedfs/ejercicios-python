# Calculadora de estadísticas de una lista:

# Escribe una función que tome una lista de números como entrada.
# La función debe calcular y devolver la suma, el promedio, el valor máximo y el valor mínimo de los números en la lista.

def statistics(numbers):
    return suma(numbers), avg(numbers), max(numbers), min(numbers)


def suma(numbers):
    total = 0
    for number in numbers:
        total += number

    return total

def avg(numbers):
    return suma(numbers) / len(numbers)

def max(numbers):
    max = numbers[0]
    for number in numbers:
        max = number if number > max else max

    return max

def min(numbers):
    min = numbers[0]
    for number in numbers:
        min = number if number < min else min

    return min

suma, avg, max, min = statistics([1, 3, 4, 2, 0])

print(suma, avg, max, min)