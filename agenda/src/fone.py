

from src.identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero


    @staticmethod
    def validarNumero(numero) -> bool:
        cont = "0123456789 ()-"
        for i in numero:
            if i not in cont:
                return False
        return True

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getNumero(self) -> str:
        return self.numero
