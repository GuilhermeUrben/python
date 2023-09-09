# import sys

# sys.setrecursionlimit(10)


# def recursiva(inicio=0, fim=10):
#     if inicio >= fim:
#         return fim
#     print(inicio, fim)
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 10))


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
