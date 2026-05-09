class Cola:

    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):

        if self.isEmpty():
            return None

        return self._elementos.pop(0)

    def isEmpty(self):
        return len(self._elementos) == 0

    def top(self):

        if self.isEmpty():
            return None

        return self._elementos[0]

    def size(self):
        return len(self._elementos)

    def reverse(self):

        nueva = Cola()

        for elemento in reversed(self._elementos):
            nueva.push(elemento)

        return nueva

    def pushAll(self, otraCola):

        for elemento in otraCola._elementos:
            self.push(elemento)

    def contiene(self, elemento):

        for item in self._elementos:

            if item == elemento:
                return True

        return False

    def copiar(self):

        nueva = Cola()

        for elemento in self._elementos:
            nueva.push(elemento)

        return nueva

    def __str__(self):
        return f"Cola({self._elementos})"