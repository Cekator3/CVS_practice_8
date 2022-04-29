# coding=utf-8
#master
#1. Написать функцию, принимающую от пользователя неориентированный невзвешенный граф.
# Функция должна запоминать и хранить граф. Необходимо для выполнения дальнейших функций.
#2. Написать функцию, принимающую от пользователя неориентированный взвешенный граф.
# Функция должна запоминать и хранить граф. Необходимо для выполнения дальнейших функций.
#3. Написать функцию, принимающую от пользователя ориентированный взвешенный граф.
# Функция должна запоминать и хранить граф. Необходимо для выполнения дальнейших функций.

#4. Написать функцию, поиска в неориентированном невзвешенном графе кратчайшего пути из вершины X в вершину Y.
# Граф, вершину X и вершину Y задает пользователь.
def f4(graph, start, fin):
    checked = [start]                #Для избежания лишних проверок и бесконечных циклов
    queue = []                  #Создание очереди
    parents = {key:None for key in graph.keys()}       #Лист создания кратчайшего пути к заданному узлу

    def _add_to_queue(queue, neigbors):     #Добавление соседей узла в очередь
        for neigbor in neigbors:
            if neigbor not in checked:
                queue.append(neigbor)

    _add_to_queue(queue, graph[start])      #Формирование стартовой очереди
    for key in graph[start]:                #И тут же формируем оптимальный путь к второуровневым узлам
        parents[key] = 'A'

    while parents[fin]==None:               #Если оптимальный путь сформирован, то цикл завершится
        node = queue.pop(0)                 #из очереди извлекается первый по очереди узел
        _add_to_queue(queue, graph[node]) #Добавляем в конец очереди соседей этого узла
        for key in graph[node]:           #И тут же формируем оптимальный путь к этим соседям
            parents[key] = node
        checked.append(node)

    # Построение ответа-массива
    ans = [fin]
    i = parents[fin]
    while i!=start:
        ans += i
        i = parents[i]
    ans += i
    return ans[::-1]
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'A'],
  'C' : ['F', 'A'],
  'D' : ['B'],
  'E' : ['F'],
  'F' : ['E','B']
}
print(f4(graph, 'A', 'F')) #A-C-F
#5. Написать функцию, поиска в неориентированном невзвешенном графе лексикографически первого пути из вершины X.
# Граф и вершину X задает пользователь.
#6. Написать функцию, поиска в неориентированном взвешенном графе кратчейших путей из вершины X до всех остальных вершин.
# Граф и вершину X задает пользователь.
def f6(graph, start):
    checked = []  # Для избежания лишних проверок и бесконечных циклов

    costs = {key:float("inf") for key in graph.keys()}  # Таблица стоимостей, нужно найти наименьший путь от начала и до каждого узла
    costs[start] = 0

    parents = {key:None for key in graph.keys()}  # Лист создания кратчайшего пути к заданному узлу

    def _find_lowest_cost_node():
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            if costs[node] < lowest_cost and node not in checked:
                lowest_cost = costs[node]
                lowest_cost_node = node
        return lowest_cost_node

    node = start  # Первый рассматриваемый узел
    while node is not None:
        neighbors = graph[node]
        for n in neighbors.keys():  # Обновляем стоимости соседей
            new_cost = costs[node] + neighbors[n]  #стоимость узла + расстояние до соседа = расстояние от начального узла до соседа через текущий узел
            if new_cost < costs[n]:  # Короче ли найденный путь?
                costs[n] = new_cost
                parents[n] = node

        checked.append(node)  # Данный узел был разобран
        node = _find_lowest_cost_node()  # Ищем следующий узел
    return parents

#7. Написать функцию, поиска в ориентированном взвешенном графе кратчейших путей из вершины X до всех остальных вершин.
# Граф и вершину X задает пользователь.
def f7(graph, start):
    checked = []  # Для избежания лишних проверок и бесконечных циклов

    costs = {key:float("inf") for key in graph.keys()}  # Таблица стоимостей, нужно найти наименьший путь от начала и до каждого узла
    costs[start] = 0

    parents = {key:None for key in graph.keys()}  # Лист создания кратчайшего пути к заданному узлу

    def _find_lowest_cost_node():
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            if costs[node] < lowest_cost and node not in checked:
                lowest_cost = costs[node]
                lowest_cost_node = node
        return lowest_cost_node

    node = start  # Первый рассматриваемый узел
    while node is not None:
        neighbors = graph[node]
        for n in neighbors.keys():  # Обновляем стоимости соседей
            new_cost = costs[node] + neighbors[n]  #стоимость узла + расстояние до соседа = расстояние от начального узла до соседа через текущий узел
            if new_cost < costs[n]:  # Короче ли найденный путь?
                costs[n] = new_cost
                parents[n] = node

        checked.append(node)  # Данный узел был разобран
        node = _find_lowest_cost_node()  # Ищем следующий узел
    return parents

#8. Написать функцию, поиска во взвешенном неориентированном графе такого поддерева, которое бы соединяло все его вершины,
# и при этом обладало наименьшим весом (т.е. суммой весов рёбер) из всех возможных.
# Такое поддерево называется минимальным остовным деревом или простом минимальным остовом.
def f8(graph, start):
    checked = []  # Для избежания лишних проверок и бесконечных циклов
    OstTreeLen = len( graph.keys() ) - 1    #Длина остовного дерева

    costs = {key:float("inf") for key in graph.keys()}  # Таблица стоимостей, нужно найти наименьший путь от начала и до каждого узла
    costs[start] = 0

    parents = {key:None for key in graph.keys()}  # Лист создания кратчайшего пути к заданному узлу

    def _find_lowest_cost_node():
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            if costs[node] < lowest_cost and node not in checked:
                lowest_cost = costs[node]
                lowest_cost_node = node
        return lowest_cost_node
    node = start  # Первый рассматриваемый узел
    while node is not None:
        neighbors = graph[node]
        for n in neighbors.keys():  # Обновляем стоимости соседей
            new_cost = costs[node] + neighbors[n]  #стоимость узла + расстояние до соседа = расстояние от начального узла до соседа через текущий узел
            if new_cost < costs[n]:  # Короче ли найденный путь?
                costs[n] = new_cost
                parents[n] = node

        checked.append(node)  # Данный узел был разобран
        node = _find_lowest_cost_node()  # Ищем следующий узел

    fin = ''                #Узел - минимальный остовное дерево
    min = float('inf')
    for key in graph.keys():    #Ищем минимальное остовное дерево
        if len(graph[key]) == OstTreeLen and costs[key]<min:
            fin=key
            min = costs[key]

    # Построение ответа-массива
    ans = [fin]
    i = parents[fin]
    while i!=start:
        ans += i
        i = parents[i]
    ans += i
    return ans[::-1]