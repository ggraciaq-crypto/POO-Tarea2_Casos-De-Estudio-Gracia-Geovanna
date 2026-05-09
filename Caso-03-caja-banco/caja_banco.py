from modelo.cola import Cola


class CajaBanco:

    def __init__(self):
        self._cola = Cola()

    def agregar_persona(self, persona):
        self._cola.push(persona)

    def atender(self):
        return self._cola.pop()

    def esta_vacia(self):
        return self._cola.isEmpty()

    def persona_abandona(self, nombre):

        cola_auxiliar = Cola()
        encontrada = False

        while not self._cola.isEmpty():

            persona = self._cola.pop()

            if persona.nombre == nombre and not encontrada:
                encontrada = True
            else:
                cola_auxiliar.push(persona)

        while not cola_auxiliar.isEmpty():
            self._cola.push(cola_auxiliar.pop())

        return encontrada