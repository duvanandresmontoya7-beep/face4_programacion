class Cliente:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def mostrar_datos(self):
        print(f"Cliente: {self.nombre}")

cliente1 = Cliente("Duvan", "12345")
cliente1.mostrar_datos()
