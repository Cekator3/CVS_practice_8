# coding=utf-8
class Graph:
    #1. Написать функцию, принимающую от пользователя неориентированный невзвешенный граф.
    # Функция должна запоминать и хранить граф. Необходимо для выполнения дальнейших функций.
    def __init__(self, graph={}):
        self.graph = graph
    #2. Написать функцию, принимающую от пользователя неориентированный взвешенный граф.
    # Функция должна запоминать и хранить граф.
    def __init_weigthed_graph__(self, graph={}):
        self.weighted_graph = graph
    #3. Написать функцию, принимающую от пользователя ориентированный взвешенный граф.
    # Функция должна запоминать и хранить граф. Необходимо для выполнения дальнейших функций.

    #То же самое, что и в задании 2.

    #4. Написать функцию, поиска в неориентированном невзвешенном графе кратчайшего пути из вершины X в вершину Y.
    # Граф, вершину X и вершину Y задает пользователь.
    def f4(self, start, fin):
        graph = self.graph
        checked = []                                        #Все просмотренные узлы, согласно алгоритму Дейкстры, уже имеют оптимальный путь к себе. Нет смысла просматривать другие найденные пути к ним
        queue = []                                          #Создание уровневой очереди(уровень определяется близостью узла к стартовому узлу)
        parents = {key:None for key in graph.keys()}        #Словарь для формирования наикратчайшего пути к любому узлу(очень не наглядно, но другого пока что не придумал)

        def _add_neigbors_to_queue(ThisNode): #Функция добавления соседей этого узла в очередь и формирования к ним кратчайшего маршрута
            for neigbor in graph[ThisNode]:    #Берём соседа текущего узла
                if neigbor not in checked:     #Если к этому соседу не был сформирован кратчайший путь, то:
                    queue.append(neigbor)         #1.Добавляем соседа в очередь.
                    parents[neigbor] = ThisNode   #2.Формируем к нему кратчайший путь(тупо говорим, что пришли к соседу из текущего узла)
            checked.append(ThisNode)           #Помечаем этот узел как полностью рассмотренный. Более он нам не пригодится

        _add_neigbors_to_queue(start)      #Формирование стартовой очереди

        while parents[fin]==None:               #Пока кратчайший путь к нужному узлу не был сформирован:
            node = queue.pop(0)                     #1.Извлекаем первый по очереди узел
            _add_neigbors_to_queue(node)            #2.Добавляем в конец очереди соседей этого узла и формируем к ним кратчайший маршрут

        # Построение ответа-массива
        ans = [fin]
        i = parents[fin]
        while i!=start:
            ans += i
            i = parents[i]
        ans += i
        return ans[::-1]

    #5. Написать функцию, поиска в неориентированном невзвешенном графе лексикографически первого пути из вершины X.
    # Граф и вершину X задает пользователь.
    def f5(self, start):
        graph = self.graph
        graph = {
            'e': {'f', 'd'},
            'f': {'d', 'b', 'a'},
            'd': {'f', 'b', 'c'},
            'a': {'b'},
            'b': {'a','c'},
            'c': {'b'}
        }
        checked = []
        costs = {key:'' for key in graph.keys()}            #Лексиграфическая стоимость
        path = []

        def _find_highest_cost_node():                       #Функция поиска узла с наименьшей стоимостью для прихода к ним с начального узла
            highest_cost = ''
            highest_cost_node = None

            for node in costs:
                if costs[node] > highest_cost and node not in checked:
                    highest_cost = costs[node]
                    highest_cost_node = node
            return highest_cost_node

        node = start                    #Первый рассматриваемый узел
        while node is not None:         #Пока мы не рассмотрели абсолютно каждый узел:
            path += node
            neighbors = list(graph[node])
            for n in neighbors:      #Обновляем стоимость лексиграфическую стоимость соседей(если они уже не были рассмотренны ранее)
                if n not in checked:
                    costs[n] += str(len(graph)-len(checked))   #количество узлов в графе - количество просмотренных  = лексиграфическая стоимость
            checked.append(node)             #Данный узел был разобран
            node = _find_highest_cost_node() #Ищем следующий узел
        print(path)
        return costs

    #6. Написать функцию, поиска в неориентированном взвешенном графе кратчейших путей из вершины X до всех остальных вершин.
    # Граф и вершину X задает пользователь.
    def f6(self, start):
        graph = self.weighted_graph
        checked = []
        costs = {key:float("inf") for key in graph.keys()}  #Таблица стоимостей. Показывает длину наименьшего пути от начального к каждому узлу
        costs[start] = 0
        parents = {key:None for key in graph.keys()}        #Словарь для формирования наикратчайшего пути к любому узлу.

        def _find_lowest_cost_node():                       #Функция поиска узла с наименьшей стоимостью для прихода к ним с начального узла
            lowest_cost = float("inf")
            lowest_cost_node = None

            for node in costs:
                if costs[node] < lowest_cost and node not in checked:
                    lowest_cost = costs[node]
                    lowest_cost_node = node
            return lowest_cost_node

        node = start                    #Первый рассматриваемый узел(он же имеет нулевую стоимость)
        while node is not None:         #Пока мы не рассмотрели абсолютно каждый узел:
            neighbors = graph[node]
            for n in neighbors.keys():      #Обновляем стоимость прихода к каждому соседу с стартового узла
                new_cost = costs[node] + neighbors[n]  #стоимость узла + расстояние до соседа = расстояние от начального узла до соседа через текущий узел
                if new_cost < costs[n]:
                    costs[n] = new_cost
                    parents[n] = node

            checked.append(node)            #Данный узел был разобран
            node = _find_lowest_cost_node() #Ищем следующий узел
        return parents

    #7. Написать функцию, поиска в ориентированном взвешенном графе кратчейших путей из вершины X до всех остальных вершин.
    # Граф и вершину X задает пользователь.
    def f7(self, start):
        #Код абсолютно такой же, как в 6 задании
        graph = self.weighted_graph
        checked = []
        costs = {key:float("inf") for key in graph.keys()}
        costs[start] = 0
        parents = {key:None for key in graph.keys()}

        def _find_lowest_cost_node():
            lowest_cost = float("inf")
            lowest_cost_node = None
            for node in costs:
                if costs[node] < lowest_cost and node not in checked:
                    lowest_cost = costs[node]
                    lowest_cost_node = node
            return lowest_cost_node

        node = start
        while node is not None:
            neighbors = graph[node]
            for n in neighbors.keys():
                new_cost = costs[node] + neighbors[n]
                if new_cost < costs[n]:
                    costs[n] = new_cost
                    parents[n] = node

            checked.append(node)
            node = _find_lowest_cost_node()
        return parents

    #8. Написать функцию, поиска во взвешенном неориентированном графе такого поддерева, которое бы соединяло все его вершины,
    # и при этом обладало наименьшим весом (т.е. суммой весов рёбер) из всех возможных.
    # Такое поддерево называется минимальным остовным деревом или простом минимальным остовом.
    def f8(self, start):
        #https://www.youtube.com/watch?v=KDKACf8tcnM
        graph = self.weighted_graph
        U = set()  # список узлов, которые были связанны с другими узлами (для отслеживания изолированных узлов)
        D = {}     # словарь списка изолированных групп узлов (нужно для соединения всех изолированных друг от друга групп соединённых узлов)
        T = []     # список ребер готового минимального остовного дерева

        Rebra = [] #новый способ представления графа специально для этого алгоритма [длина ребра, узел 1, узел 2]
        for key in graph.keys():
            for key2 in graph[key].keys():
                 Rebra.append([i for i in [graph[key][key2], key,key2]])

        Rebra.sort(key=lambda x:x[0])   #Сортировка по длине ребра

        for r in Rebra:  #Сначала соединяем узлы по порядку, если хотя бы один из них не изолирован
            condition = (r[1] in U) | ((r[2] in U) * 0x10)  # 0x?? - двоичная система (наглядно при работе с бинарными операторами)
            #Условия:
            #0x0 - оба узла изолированны. В этом случае просто соединяем их, образуя новую изолированную от центра группу узлов
            #0x1 или 0x10 - только один узел изолирован. В этом случае присоединяем изолированный к группе неизолированного
            #0x11 - оба узла соединенны с какими-либо узлами.
            if condition != 0x11:               #Если хотя бы 1 узел изолирован
                if condition == 0x0:             #Если Оба узла изолированны
                    D[r[1]] = [r[1], r[2]]        #Тогда их просто соединяем
                    D[r[2]] = D[r[1]]             #Причём второй узел будет мысленно соединён со всеми узлами, которые были будут соединены с первым
                else:                           #Если изолирован только один узел
                    if condition & 0x1 == 0x1:    #если второй узел изолирован
                        D[r[1]].append(r[2])
                        D[r[2]] = D[r[1]]
                    else:                       #иначе первый узел присоединится к клубу кожевников
                        D[r[2]].append(r[1])
                        D[r[1]] = D[r[2]]

                T.append(r)  #добавляем ребро в остов
                U.add(r[1])  #добавляем узлы в множество поюзанных узлов (какие же множества в Python удобные, наверное)
                U.add(r[2])

            else:   #Если оба узла не изолированны, то нужно проверить обособленны ли друг от друга эти две группы соединённых узлов
                if r[2] not in D[r[1]]:  # если второй узел не входит в группу первого узла
                    gr1 = D[r[1]]  # Делаем эти в прошлом изолированные группы едиными
                    D[r[1]] += D[r[2]]
                    D[r[2]] += gr1
                    T.append(r)    # добавляем новообразованное соединение в минимальный остов
        return T
g = Graph()
gr = {
    'A': {'B':1, 'C':3},
    'B': {'D':7, 'E':2, 'A':1},
    'C': {'F':4},
    'D': {},
    'E': {'F':1},
    'F': {}
}
g.__init_weigthed_graph__(gr)
print(g.f8('A')) #A-C-F