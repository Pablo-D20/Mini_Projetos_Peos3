from src.aluno.base.funcionario import Funcionario
from src.cliente.irh_service import IRHService
from src.aluno.base.professor import Professor
from src.aluno.base.sta import STA
from src.aluno.base.terceirizado import Terceirizado
from src.cliente.tipo import Tipo

class RHService(IRHService):

    def __init__(self):
        self.divisaoNosLucros = 0
        self.funcionarios = []

    def cadastrar(self, funcionario: Funcionario):
        if isinstance(funcionario, Professor):
            if 'A' <= funcionario.classe <= 'E':
                if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True

        elif isinstance(funcionario, STA):
            if 1 <= funcionario.nivel <= 30:
                if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True
                return False
            return False

        else:
            if funcionario.getCpf() not in [c.getCpf() for c in self.funcionarios]:
                self.funcionarios.append(funcionario)
                return True
        return False

    def remover(self, cpf: str):
        for f in self.funcionarios:
            if f.getCpf() == cpf:
                self.funcionarios.remove(f)
                return True
        return False

    def obterFuncionario(self, cpf: str):
        for i in self.funcionarios:
            if i.getCpf() == cpf:
                return i
        return None

    def getFuncionarios(self):
        return sorted(self.funcionarios, key=lambda funcionario: funcionario.nome)

    def getFuncionariosPorCategorias(self, tipo):

        if tipo == tipo.PROF:
            for funcionario in self.funcionarios:
                if isinstance(funcionario, Professor):
                    type_funcionario = funcionario
        elif tipo == tipo.STA:
            for funcionario in self.funcionarios:
                if isinstance(funcionario, STA):
                    type_funcionario = funcionario
        elif tipo == tipo.TERC:
            for funcionario in self.funcionarios:
                if isinstance(funcionario, Terceirizado):
                    type_funcionario = funcionario
        else:
            return 0
        type_funcionario.sort(key=lambda x: x.nome)
        return type_funcionario


    def getTotalFuncionarios(self):
        return len(self.funcionarios)

    def solicitarDiaria(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                if funcionario.getTipo == 1:
                    if funcionario.getDiarias() < 3:
                        funcionario.adicionarDiaria()
                        return True
                elif funcionario.getTipo == 2:
                    if funcionario.getDiarias() < 1:
                        funcionario.adicionarDiaria()
                        return True
                else:

                    return False
            return False
        return False

    def partilharLucros(self, valor: float):

        if not self.funcionarios:
            return False

        valorPorFuncionario = valor / len(self.funcionarios)
        for funcionario in self.funcionarios:
            funcionario.aumentarSalario(valorPorFuncionario)

    def iniciarMes(self):
        for f in self.funcionarios:
            f.zerarDiarias()

    def calcularSalarioDoFuncionario(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                salario_base = 0

                if funcionario.getTipo() == Tipo.PROF:

                    classe = funcionario.getClasse()
                    if classe == "A":
                        salario_base = 3000
                    elif classe == "B":
                        salario_base = 5000
                    elif classe == "C":
                        salario_base = 7000
                    elif classe == "D":
                        salario_base = 9000
                    elif classe == "E":
                        salario_base = 11000
                elif funcionario.getTipo() == Tipo.STA:

                    nivel = funcionario.getNivel()
                    salario_base = 1000 + 100 * nivel
                elif funcionario.getTipo() == Tipo.TERC:

                    if funcionario.getInsalubre():
                        salario_base = 1500
                    else:
                        salario_base = 1000


                salario_total = salario_base + (funcionario.getDiarias() * 100) + self.divisaoNosLucros
                return salario_total

            return 0

    def calcularFolhaDePagamento(self):

        return sum(f.calcularSalario() for f in self.funcionarios)
