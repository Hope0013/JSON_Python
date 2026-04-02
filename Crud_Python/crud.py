import json
import os

def carregar_dados():
    # Se oarquivo não existir, retorna uma lista vazia
    if not os.path.exists("dados.json"):
        return []
    
    #Abre o arquivo em modo leitura
    with open ("dados.json", "r", encoding = "utf-8") as arquivo:
        # R para abrir o arquivo em modo leitura (Read)
        return json.load(arquivo)
    
def salvar_dados(dados):
    # Abre o arquivo em modo escrita
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        #W para abrir o arquivo em modo escrita (Write)
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def criar_pessoa(nome, idade):
    dados = carregar_dados()

    # Gerar um ID simples
    novo_id = 1
    if dados:
        novo_id = dados[-1]["id"] +1
    pessoa = {
        "id": novo_id,
        "nome": nome,
        "idade": idade
    }

    dados.append(pessoa)
    salvar_dados(dados)

    print("Pessoa Cadastrada com Sucesso!")

def listar_pessoas():
    dados = carregar_dados()

    if not dados:
        print("Nenhum Registro Encontrado")
        return
    
    for pessoa in dados:
        print(f"ID: {pessoa['id']} | Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")

def atualizar_pessoa(id, novo_nome, nova_idade):
    dados = carregar_dados()

    for pessoa in dados:
        if pessoa["id"] == id:
            pessoa["nome"] = novo_nome
            pessoa["idade"] = nova_idade
            salvar_dados(dados)
            print("Pessoa Atualizada com Sucesso!")
            return
    print("ID não Encontrado")

def deletar_pessoa(id):
    dados = carregar_dados()
    dados = [pessoa for pessoa in dados if pessoa["id"] != id]

    salvar_dados(dados)
    print("Pessoa Removida (Se Existia)")

while True:
    print("\n1- Cadastrar")
    print("2- Listar")
    print("3- Atualizar")
    print("4- Deletar")
    print("0- Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input ("Nome: ")
        idade = int (input("Idade: "))
        criar_pessoa(nome, idade)
    
    elif opcao == "2":
        listar_pessoas()
    
    elif opcao == "3":
        id = int(input("ID: "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        atualizar_pessoa(id, nome, idade)
    
    elif opcao == "4":
        id = int(input("ID: "))
        deletar_pessoa(id)
    
    elif opcao =="0":
        break

    else:
        print("Opção Inválida!")