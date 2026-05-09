from modelo.persona import Persona
from caja_banco import CajaBanco


def main():

    caja = CajaBanco()

    nombres = [
        "Geovanna Gracia",
        "Julian Mera",
        "Jorge Menéndez",
        "Valeria Cedeño",
        "Roberto Anchundia",
    ]

    print("=" * 40)
    print(" Banco Bolivariano — Caja #1")
    print("=" * 40)

    print("\nClientes llegando a la fila:\n")

    for nombre in nombres:
        persona = Persona(nombre)
        caja.agregar_persona(persona)
        print(f"  >> Turno #{persona.turno} - {persona.nombre} toma un turno y espera.")

    print("\nUna persona abandona la fila...\n")

    resultado = caja.persona_abandona("Julian Mera")

    print(f"Julian Mera abandonó la fila: {resultado}")

    print("\nCajero listo. Iniciando atención...\n")

    while not caja.esta_vacia():

        persona = caja.atender()

        print(f"  [CAJERO] Turno #{persona.turno} - {persona.nombre} ha sido atendida.")

    print("\nTodos los clientes han sido atendidos.")


main()