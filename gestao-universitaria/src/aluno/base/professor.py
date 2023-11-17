from src.aluno.base.funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        self.cpf = cpf
        self.nome = nome
        self.classe = classe


