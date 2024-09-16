def buscar_cercanos(lista, consultas):
    for consulta in consultas:
        izq, der = 0, len(lista) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if lista[medio] == consulta:
                izq = medio
                break
            elif lista[medio] < consulta:
                izq = medio + 1
            else:
                der = medio - 1

        menor = 'X' if izq == 0 else lista[izq - 1]
        mayor = 'X' if izq == len(lista) else lista[izq] if lista[izq] > consulta else lista[izq + 1] if izq + 1 < len(lista) else 'X'

        print(menor, mayor)

n = int(input("Tamaño de la lista: "))
lista = sorted(map(int, input("Lista de números: ").split()))
q = int(input("Número de consultas: "))
consultas = list(map(int, input("Números a consultar: ").split()))

buscar_cercanos(lista, consultas)
