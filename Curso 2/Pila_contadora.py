class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        # contador oculto para las operaciones pop
        self.__pop_counter = 0

    def get_counter(self):
        # devuelve el valor actual del contador
        return self.__pop_counter

    def pop(self):
        # realiza el pop usando la implementación de la superclase
        val = super().pop()
        # actualiza el contador
        self.__pop_counter += 1
        return val


# prueba
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())  # debe imprimir 100