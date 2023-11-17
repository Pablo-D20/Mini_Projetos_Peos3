from src.contato import Contato
from src.identificador import Identificador

class Agenda:

    def __init__(self):
        self.contatos = []
        self.fones = []
    def getContatos(self) -> list:
        return sorted(self.contatos, key=lambda contato: contato.getName())

    def getQuantidadeDeContatos(self) -> int:
        return len(self.contatos)

    def getContato(self, nome: str) -> Contato:
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None


    def adicionarContato(self, contato: Contato) -> bool:  ###########
        if contato.getFones():
            if contato.getName() not in [c.getName() for c in self.contatos]:
                self.contatos.append(contato)
                self.fones.extend(contato.getFones())
                return True
            else:
                for contatos in self.contatos:
                    if contatos.getName() == contato.getName():
                        contatos.getFones().extend(contato.getFones()) #rescrever
                        self.fones = contatos.getFones() #self.fones.append(contatos.getFones())
                        return False
                    #return True

    def removerContato(self, nome: str) -> bool:
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True

    def removerFone(self, nome: str, index: int) -> bool:
        contato = self.getContato(nome)
        if contato and 0 <= index < len(contato.getFones()):
            contato.getFones().pop(index)

            # If the contact has no more phone numbers, remove the contact from the agenda
            if not contato.getFones():
                self.contatos.remove(contato)

            return True
        return False


    def getQuantidadeDeFonesPorIdentificador(self, identificador: Identificador = None) -> int: ########
        if identificador:
            return sum(
                fone.getIdentificador() == identificador for contato in self.contatos for fone in contato.getFones()
            )
        else:
            return sum(contato.getQuantidadeFones() for contato in self.contatos)

    def getQuantidadeTotalDeFones(self) -> int:
        return len(self.fones)

    def pesquisar(self, expressao:str) -> list:

        results = []
        for contato in self.contatos:
            if expressao.lower() in contato.getName().lower():
                results.append(contato)
            for fone in contato.getFones():
                if expressao.lower() in fone.getNumero().lower():
                    results.append(contato)
                    break
        return sorted(results, key=lambda contato: contato.getName())




