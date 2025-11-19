import os 
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    RG: str
    CPF: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}. Data de nascimento: {self.data_nascimento}. RG: {self.RG}. CPF: {self.CPF}")

        lista_de_pessoas = []
        QUANTIDADE_DE_FUNCIONARIOS = 5
        for i in range(QUANTIDADE_DE_FUNCIONARIOS):
            pessoa = Funcionario(
                nome=input("Digite o seu nome: ")
                data_nascimento=input("Digite a sua data de nascimento: ")
                RG=input("Digite o seu RG: ")
                CPF=input("Digite o seu CPF: ")
            )
            lista_de_pessoas.append(funcionarios)
            print() # Pular uma linha
            nome_arquivo = "dados_funcionario.cvs"
            with open(nome_arquivo, "a") as arquivo_pessoas:
                for pessoa in lista_de_pessoas: 
                    arquivo_pessoas.write(f"{Funcionario.nome}, {Funcionario.data_nascimento}, {Funcionario.RG}, {Funcionario.CPF}\n")
                    print("Dados salvos com sucesso. ")
