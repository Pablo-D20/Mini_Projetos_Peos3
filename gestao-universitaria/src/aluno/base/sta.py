from src.aluno.base.funcionario import Funcionario


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        self.cpf = cpf
        self.nome = nome
        self.nivel = nivel
