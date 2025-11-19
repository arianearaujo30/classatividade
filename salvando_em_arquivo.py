import os 
from dataclasses import dataclass

@dataclass
class Paciente: 
    nome: str
    idade: int
    peso: float
    altura: float
    CPF: str


    def exibir_dados(self):
        print(f"Nome: {self.nome}. Idade: {self.idade} anos. Peso: {self.peso}. Altura: {self.altura}. CPF: {self.CPF}")
              
lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2
for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente
    (
        nome=input("Digite o seu nome:")
        idade= int(input("Digite a sua idade:" ))
        peso= float(input("Digite o seu peso:"))
        altura= float(input("Digite a sua altura:"))
        CPF= str(input("Digite o seu CPF:"))
    )
    lista_de_pacientes.append(paciente)
    print() # Pular uma linha

    nome_arquivo = "dados_pacientes.cvs"
    with open(nome_arquivo, "a") as arquivo_pacientes:
        for paciente in lista_de_pacientes:
            arquivo_pacientes.write(f"{Paciente.nome}, {Paciente.iade}, {Paciente.peso}, {Paciente.altura}, {Paciente.CPF}\n")
        print("Dados salvos com sucesso.")

# print("\nExibindo lista de paciente:")
# for paciente in lista_de_paciente:
 #            paciente.exibir_dados()        
