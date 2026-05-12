from cliente import Cliente
from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='errores.log', level=logging.ERROR)

# Clase abstracta Servicio
class Servicio(ABC):
    @abstractmethod
    def calcular_costo(self):
        pass


class Sala(Servicio):
    def __init__(self, horas):
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000


class Equipo(Servicio):
    def __init__(self, dias):
        self.dias = dias

    def calcular_costo(self):
        return self.dias * 30000


class Asesoria(Servicio):
    def __init__(self, horas):
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 80000


class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio

    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo()
            print(f"Reserva confirmada para {self.cliente.nombre} - Costo: {costo}")
        except Exception as e:
            logging.error(str(e))
            print("Error en la reserva")


# PRUEBAS
if __name__ == "__main__":
    try:
        c1 = Cliente("Duvan", "123")
        r1 = Reserva(c1, Sala(2))
        r1.confirmar()

        r2 = Reserva(c1, Equipo(3))
        r2.confirmar()

        r3 = Reserva(c1, Asesoria(1))
        r3.confirmar()

    except Exception as e:
        logging.error(str(e))
        print("Error general")
