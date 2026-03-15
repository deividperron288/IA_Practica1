class QueueError(Exception):  # nueva excepción
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)  # agregar al inicio

    def get(self):
        if len(self.__queue) == 0:    # verificar si está vacía
            raise QueueError
        return self.__queue.pop()     # sacar del final


que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")