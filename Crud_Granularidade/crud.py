import json
import os

def menu():
    print("\n===Menu de Contatos===")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Sair")

def escolher_grupo():
    print("\n===Tipo de Contato===")
    print("1. Aluno")
    print("2. Professor")

    opcao = input("Escolha: ")

    if opcao == "1":
        return "alunos"
    
    elif opcao == "2":
        return "professores"
    
    else:
        print("Opção Inválida")
        return None
    
def ler_dados():
    with open("contatos.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_dados(dados):
    with open("contatos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def adicionar():
    grupo = escolher_grupo()

    if not grupo:
        return
    
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    dados = ler_dados()

    dados[grupo].append({
        "nome": nome,
        "telefone": telefone
    })

    salvar_dados(dados)
    print("\nContato Adicionado com Sucesso!")

def listar():
    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()
    print(f"\nLista de {grupo.upper()}: ")

    for index, contato in enumerate(dados[grupo], start=1): 
        print(f"{index}. {contato['nome']} - {contato['telefone']}")

def  atualizar():
    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()

    index = int(input("Index do Contato: ")) -1

    if 0 <= index < len(dados[grupo]):
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")

        dados[grupo][index] = {
            "nome":nome,
            "telefone":telefone
        }

        salvar_dados(dados)
        print("Contato Atualizado com Sucesso!")
    else:
        print("Índice Inválido")

def excluir():
    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()

    index = int(input("Index do Contato: ")) -1

    if 0<= index < len(dados[grupo]):
        dados[grupo].pop(index)

        salvar_dados(dados)
        print("Contato Excluído com Sucesso!")

    else:
        print("Índice Inválido")

def main():
    while True:
        menu()
        
        opcao = input("Escolha uma Opção:")
        
        if opcao == "1":
            adicionar()
        
        elif opcao == "2":
            listar()
        
        elif opcao == "3":
            atualizar()

        elif opcao == "4":
            excluir()

        elif opcao == "5":
            print("Encerrando o programa...")
            break

        else: 
            print("Opção Inválida")

main()