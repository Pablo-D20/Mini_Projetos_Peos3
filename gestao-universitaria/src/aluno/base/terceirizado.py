from src.aluno.base.funcionario import Funcionario


class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubre: bool):
        self.cpf = cpf
        self.nome = nome
        self.insalubre = insalubre

