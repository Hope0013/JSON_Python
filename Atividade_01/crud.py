import json

def menu():
    print("\n===RPG - Jogadores e Personagens===")
    print("1. Adicionar Jogador")
    print("2. Atualizar Jogador")
    print("3. Adicionar Personagem")
    print("4. Atualizar Personagem")
    print("5. Listar")
    print("6. Excluir")
    print("0. Sair")

    
def ler_dados():
    with open("jogadores.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_dados(dados):
    with open("jogadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def adicionar_jogador():
    
    print("\n===Adicione um Novo Jogador===")

    nome = input("Nome: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")

    dados = ler_dados()

    dados["jogadores"].append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    })

    salvar_dados(dados)
    print("\nJogador Adicionado com Sucesso!")

def adicionar_personagem():

    print("\n===Adicione um Novo Personagem===")

    nome = input("Nome: ")
    idade = input("Idade: ")
    classe = input("Classe: ")
    jogador = input("Jogador: ")

    dados = ler_dados()

    dados["personagens"].append({
        "nome": nome,
        "idade": idade,
        "classe": classe,
        "jogador": jogador
    })

    salvar_dados(dados)
    print("\nPersonagem Adicionado com Sucesso!")

def escolher_grupo():
    print("\n===Jogadores ou Personagens===")

    print("\n1. Jogadores")
    print("2. Personagens")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        return "jogadores"
    
    elif opcao == "2":
        return "personagens"
    
    else:
        print("Opção Inválida")
        return None

def listar():

    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()
    print(f"\nLista de {grupo.upper()}: ")

    for index, item in enumerate(dados[grupo], start=1): 
        # Parte comum: Nome e Idade
        print(f"\n{index}. Nome: {item['nome']} | Idade: {item['idade']}", end="")

        # Parte específica para Jogadores
        if grupo == "jogadores":
            print(f" | Telefone: {item['telefone']}")
        
        # Parte específica para Personagens
        else:
            print(f" | Classe: {item['classe']} | Jogador: {item['jogador']}")

def  atualizar_jogador():
    
    dados = ler_dados()

    index = int(input("Index do Jogador: ")) -1

    if 0 <= index < len(dados):
        nome = input("Novo nome: ")
        idade = input("Nova Idade: ")
        telefone = input("Novo telefone: ")

        dados[index] = {
            "nome":nome,
            "idade": idade,
            "telefone":telefone
        }

        salvar_dados(dados)
        print("Jogador Atualizado com Sucesso!")
    else:
        print("Índice Inválido")

def  atualizar_personagem():
    
    dados = ler_dados()

    index = int(input("Index do Personagem: ")) -1

    if 0 <= index < len(dados):
        nome = input("Novo nome: ")
        idade = input("Nova Idade: ")
        classe = input("Nova Classe: ")
        jogador = input("Novo Jogador: ")

        dados[index] = {
            "nome":nome,
            "idade": idade,
            "classe":classe,
            "jogador":jogador
        }

        salvar_dados(dados)
        print("Personagem Atualizado com Sucesso!")
    else:
        print("Índice Inválido")

def excluir():
    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()

    index = int(input(f"Index do {grupo}: ")) -1

    if 0<= index < len(dados[grupo]):
        dados[grupo].pop(index)

        salvar_dados(dados)
        print("Excluído com Sucesso!")

    else:
        print("Índice Inválido")

def main():
    while True:
        menu()
        
        opcao = input("Escolha uma Opção:")
        
        if opcao == "1":
            adicionar_jogador()

        elif opcao == "2":
            atualizar_jogador()
        
        elif opcao == "3":
            adicionar_personagem()
        
        elif opcao == "4":
            atualizar_personagem()

        elif opcao == "5":
            listar()

        elif opcao == "6":
            excluir()
        
        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else: 
            print("Opção Inválida")

main()