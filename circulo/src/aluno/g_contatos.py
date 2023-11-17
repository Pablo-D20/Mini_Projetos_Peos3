from src.cliente.circulo_base import CirculoBase
from src.cliente.contato_base import ContatoBase
from base.contato import Contato
from base.circulo import Circulo
from src.cliente.icirculo_operations_manager import ICirculoOperationsManager
from src.cliente.icirculos_manager import ICirculosManager
from src.cliente.icontatos_manager import IContatosManager



class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):
    def __init__(self):
        self.contatos_exist = []
        self.circle_active = []

    def createContact(self, id: str, email: str) -> bool:

        if not len(self.contatos_exist) > 0:
            contato = Contato(id, email)
            self.contatos_exist.append(contato)
            return True

        for contact in self.contatos_exist:

            if contact.getId() == id:
                return False

            elif contact != self.contatos_exist[-1]:
                continue

            else:
                contato = Contato(id, email)
                self.contatos_exist.append(contato)
                return True
        return False

    def getAllContacts(self) -> list:
        return self.contatos_exist

    def updateContact(self, contato: Contato) -> bool:
        for contacto in self.contatos_exist:

            if contacto.getId() == contato.getId():
                contacto.setEmail(contato.getEmail())
                return True
        return False

    def removeContact(self, id: str) -> bool:

        for contacts in self.contatos_exist:

            if contacts.getId() == id:
                self.contatos_exist.remove(contacts)
                return True
        return False

    def getContact(self, id: str) -> Contato:

        for contacts in self.contatos_exist:

            if contacts.getId() == id:
                return contacts
        return None
    def getNumberOfContacts(self) -> int:
        return len(self.contatos_exist)

    def favoriteContact(self, idContato: str) -> bool:

        for contacts in self.contatos_exist:

            if contacts.getId() == idContato:
                contacts.favor = True
                return True
        return False

    def unfavoriteContact(self, idContato: str) -> bool:

        for contacts in self.contatos_exist:

            if contacts.getId() == idContato:
                contacts.favor = False
                return True
        return False

    def isFavorited(self, id: str) -> bool:

        for contacts in self.contatos_exist:

            if contacts.getId() == id:

                if contacts.favor:
                    return True
                else:
                    return False
        return False

    def getFavorited(self) -> list:
        favorito = []

        for contacts in self.contatos_exist:
            if contacts.favor:
                favorito.append(contacts)

        if len(favorito) > 0:
            return favorito
        else:
            return None

    def createCircle(self, id: str, limite: int) -> bool:

        if not len(self.circle_active) > 0:
            circulo = Circulo(id, limite)
            self.circle_active.append(circulo)
            return True

        for circulo in self.circle_active:
            if circulo.getId() == id:
                return False
            elif circulo != self.circle_active[-1]:
                continue
            else:
                circulo = Circulo(id, limite)
                self.circle_active.append(circulo)
                return True
        return False


    def updateCircle(self, circulo: Circulo) -> bool:

        for circle in self.circle_active:
            if circle.getId() == circulo.getId():
                if circulo.limite <= 0:
                    return False
                else:
                    circle.limite = (circulo.getLimite())
                    return True
        return False

    def getCircle(self, idCirculo: str) -> Circulo:

        for circulo in self.circle_active:
            if circulo.getId() == idCirculo:
                return circulo
        return None

    def getAllCircles(self) -> list:
        return self.circle_active

    def removeCircle(self, idCirculo: str) -> bool:

        for circle in self.circle_active:
            if circle.getId() == idCirculo:
                self.circle_active.remove(circle)
                return True
        return False

    def getNumberOfCircles(self) -> int:
        return len(self.circle_active)

    def tie(self, idContato: str, idCirculo: str) -> bool:

        for circle in self.circle_active:
            if circle.getId() == idCirculo:
                if circle.limite > len(circle.contatos):
                    for contacts in self.contatos_exist:
                        if contacts.getId() == idContato:
                            for contatos in circle.contatos:
                                if contacts.getId() == contatos.getId():
                                    return False
                            circle.contatos.append(contacts)
                            return True
                else:
                    return False
            else:
                pass
        return False

    def untie(self, idContato: str, idCirculo: str) -> bool:
        for circle in self.circle_active:
            if circle.getId() == idCirculo:
                for contacts in circle.contatos:
                    if contacts.getId() == idContato:
                        circle.contatos.remove(contacts)
                        return True
            else:
                pass
        return False

    def getContacts(self, id: str) -> list:
        for circle in self.circle_active:
            if circle.getId() == id:
                return circle.contatos
        return None

    def getCircles(self, id: str) -> list:
        lista_circ = []
        for circle in self.circle_active:
            for contacts in circle.contatos:
                if contacts.getId() == id:
                    lista_circ.append(circle)
                    return lista_circ
            else:
                pass
        return []

    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:
        lista = []
        lista1 = []
        contador = 0
        for contacts in self.contatos_exist:
            if idContato1 or idContato2 == contacts.getId:
               contador += 1
            else:
                pass
        if contador != 2:
            return None

        for circle in self.circle_active:
            for contacts in circle.contatos:
                if contacts.getId() == idContato1:
                    lista.append(circle)
                elif contacts.getId() == idContato2:
                    lista1.append(circle)
                else:
                    pass
        for circle1, circle2 in lista, lista1:
            for contacts1 in circle1:
                for contacts2 in circle2:
                    if contacts1 == contacts2:
                        return contacts1
                    else:
                        pass
        return None