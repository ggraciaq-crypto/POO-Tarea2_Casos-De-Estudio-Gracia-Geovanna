class Persona:

    contador_turnos = 0

    def __init__(self, nombre):
        Persona.contador_turnos += 1
        self._turno = Persona.contador_turnos
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @property
    def turno(self):
        return self._turno

    def __str__(self):
        return f"Turno #{self._turno} - {self._nombre}"