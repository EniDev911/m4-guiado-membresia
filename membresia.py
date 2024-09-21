from abc import ABC, abstractmethod


class Membresia(ABC):

    def __init__(self, correo, num_tarjeta):
        self.correo_suscriptor = correo
        self.numero_tarjeta = num_tarjeta

    @abstractmethod
    def _crear_nueva_membresia(self):
        pass


class Gratis(Membresia):
    VALOR = 0
    DISPOSITIVOS = 1

    def __init__(self, correo, num_tarjeta):
        super().__init__(correo, num_tarjeta)

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return Gratis(self.correo_suscriptor, self.numero_tarjeta)


class Basico(Gratis):
    VALOR = 3000
    DISPOSITIVOS = 2

    def __init__(self, correo, num_tarjeta):
        super().__init__(correo, num_tarjeta)

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia >= 2 and nueva_membresia <= 4:
            return super()._crear_nueva_membresia(nueva_membresia)
        else:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)

    def _cancelar_sucripcion(self):
        return Gratis(self._crear_nueva_membresia, self.numero_tarjeta)


class Familiar(Basico):
    VALOR = 5000
    DISPOSITIVOS = 5

    def __init__(self, correo, num_tarjeta):
        super().__init__(correo, num_tarjeta)
        self.dias_de_regalo = 7

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia in [1, 3, 4]:
            return super()._crear_nueva_membresia(nueva_membresia)
        else:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)

    def _cambiar_control_parental(self):
        pass


class SinConexion(Familiar):
    VALOR = 3500
    DISPOSITIVOS = 2

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia in [1, 2, 4]:
            return super()._crear_nueva_membresia(nueva_membresia)
        else:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)


class Pro(SinConexion):
    VALOR = 7000
    DISPOSITIVOS = 6

    def __init__(self, correo, num_tarjeta):
        super().__init__(correo, num_tarjeta)
        self.dias_de_regalo = 15

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia >= 1 and nueva_membresia <= 3:
            return super()._crear_nueva_membresia(nueva_membresia)
        else:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)


if __name__ == "__main__":
    gratis = Gratis("marco@gmail.com", "123-123-123")
    print("Suscritor:", type(gratis).__name__)
    print("Valor plan:", gratis.VALOR)
    print("Cantidad de dispositivos:", gratis.DISPOSITIVOS)
    print()
    basico = gratis._crear_nueva_membresia(1)
    print("Suscritor:", type(basico).__name__)
    print("Valor plan:", basico.VALOR)
    print("Cantidad de dispositivos:", basico.DISPOSITIVOS)
    print()
    familiar = basico._crear_nueva_membresia(2)
    print("Suscritor:", type(familiar).__name__)
    print("Valor plan:", familiar.VALOR)
    print("Cantidad de dispositivos:", familiar.DISPOSITIVOS)
    print("Días de regalo:", familiar.dias_de_regalo)
    print()
    sinconexion = familiar._crear_nueva_membresia(3)
    print("Suscritor:", type(sinconexion).__name__)
    print("Valor plan:", sinconexion.VALOR)
    print("Cantidad de dispositivos:", sinconexion.DISPOSITIVOS)
    print("Días de regalo:", sinconexion.dias_de_regalo)
    print()
    pro = sinconexion._crear_nueva_membresia(4)
    print("Suscritor:", type(pro).__name__)
    print("Valor plan:", pro.VALOR)
    print("Cantidad de dispositivos:", pro.DISPOSITIVOS)
    print("Días de regalo:", pro.dias_de_regalo)
    print()