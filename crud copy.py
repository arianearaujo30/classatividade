import os
import time
from dataclasses import dataclass
os.system("cls || clear") #Limpa o terminal em Windowns e Linux.

lista_clientes = []

@dataclass
class Cliente:
    # Atributos da classe.
    # Atributos são variáveis que pewrtence à classe
    nome: str
    email: str
    telefone: str

    # Método para exibir os dados dos clientes.
    # Método é o nome dado a uma função que pertence à classe.
    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefonje}")


# Função para verificar se a lista está vazia.
def verificar_lista_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False
# Função para adiconar um novo cliente na lista.
def adicionar_cliente(lista_clientes):
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email:")
    telefone = input("Digite seu t6elefone:")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nClente {nome} adicionado com sucesso0!")

# Função para encontrar um cliente na lista.
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar.lower(): 
            return cliente
    return None # None significa retornar vazio, sem conteúdo.

# Função para mostrar todos os clientes.
def mostrar_todos_clientes(lista_clientes):
    if  verificar_lista_vazia(lista_clientes):
        return
    
    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        print(f"{cliente.mostrar_dados()}")

# Função para atualiazar clientes.
def atualizar_cliente(lista_clientes):
    if verificar_lista_vazia(lista_clientes):
        return
    
    # Mostrar a lista para ajudar o usuário.
    mostrar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente ---")
    nome_buscar = input("\nDigite o nome do cliente:")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite od nopvos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome:")

        print(f"\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo e-mail:")

        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("novo telefone:")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone: 
            cliente_para_atualizar.telefone = novo_telefone

        print(f"\nDados do cliente {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nCliente com nome: {nome_buscar} não encontrado.")

#função para excluir cliente.
def excluir_cliente(lista_clientes):
    if verificar_lista_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)

    nome_buscar = input("\nDigite o nome do cliente que deseja excluir:")

    cliente_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCliente {nome_buscar} removido com sucesso!")
    else:
        print(f"\nCliente com nome: {nome_buscar} não encontrado.")



# Mostrando menu.
while True:
    print("""
--- Gerenciador de Clientes ---
1 - Adicionar
2 - mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
           """)
    opcao = int(input("escolha uma opção: "))

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2: 
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_cliente(lista_clientes)
        case 4: 
            excluir_cliente(lista_clientes)
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente")

    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)

    # Limpa tela.
    if opcao != 0: 
        os.system("cls || clear")
