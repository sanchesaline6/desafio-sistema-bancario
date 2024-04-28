from .Cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento) -> None:
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento