class Pila:

    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if self.isEmpty():
            return None

        return self._elementos.pop()

    def isEmpty(self):
        return len(self._elementos) == 0

    def top(self):
        if self.isEmpty():
            return None

        return self._elementos[-1]

    def size(self):
        return len(self._elementos)

    def reverse(self):

        nueva = Pila()

        for elemento in self._elementos:
            nueva.push(elemento)

        return nueva

    def pushAll(self, otraPila):

        for elemento in otraPila._elementos:
            self.push(elemento)

    def contiene(self, elemento):

        for item in self._elementos:

            if item == elemento:
                return True

        return False

    def copiar(self):

        nueva = Pila()

        for elemento in self._elementos:
            nueva.push(elemento)

        return nueva

    def __str__(self):
        return f"Pila({self._elementos})"

