import json

# Menu inicial
def menu():
    print("\n===RPG - Jogadores e Personagens===")
    print("1. Adicionar Jogador")
    print("2. Atualizar Jogador")
    print("3. Adicionar Personagem")
    print("4. Atualizar Personagem")
    print("5. Listar")
    print("6. Excluir")
    print("0. Sair")

# Lê os dados Json
def ler_dados():
    with open("jogadores.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

# Salva dados no json
def salvar_dados(dados):
    with open("jogadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

# Função para adicionar um jogador
def adicionar_jogador():
    
    print("\n===Adicione um Novo Jogador===")

    nome = input("Nome: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")

    dados = ler_dados()

    dados["jogadores"].append({ # Colocamos "jogadores" para ele salvar no lugar certo do Json
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    })

    salvar_dados(dados)
    print("\nJogador Adicionado com Sucesso!")

# Adiciona personagem
def adicionar_personagem():

    print("\n===Adicione um Novo Personagem===")

    nome = input("Nome: ")
    idade = input("Idade: ")
    classe = input("Classe: ")
    jogador = input("Jogador: ")

    dados = ler_dados()

    dados["personagens"].append({ # Igual ao anterior, só que salva em personagens
        "nome": nome,
        "idade": idade,
        "classe": classe,
        "jogador": jogador
    })

    salvar_dados(dados)
    print("\nPersonagem Adicionado com Sucesso!")

# Aqui é uma função de escolher grupo que é usada no excluir e no listar
def escolher_grupo():
    print("\n===Jogadores ou Personagens===")

    print("1. Jogadores")
    print("2. Personagens")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        return "jogadores"
    
    elif opcao == "2":
        return "personagens"
    
    else:
        print("Opção Inválida")
        return None

# Lista as informações do Json e o escolher grupo é usado para o programa saber se queremos listar jogadores ou personagens
def listar():

    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()
    print(f"\nLista de {grupo.upper()}: ")

    for index, item in enumerate(dados[grupo], start=1): # Faz uma lista enumerada (começando do 1) com as informações na frente
        
        # Aqui temos a parte em comum de jogadores e personagens
        print(f"\n{index}. Nome: {item['nome']} | Idade: {item['idade']}", end="")

        # Já aqui, é uma parte específica para Jogadores
        if grupo == "jogadores":
            print(f" | Telefone: {item['telefone']}")
        
        # E aqui uma parte específica para Personagens
        else:
            print(f" | Classe: {item['classe']} | Jogador: {item['jogador']}")
    # Essas partes fazem com que, na hora da listagem, se você escolher jogador listará as caracteristicas atribuidas a ele como nome, idade e telefone; já no personagem lista nome, idade, classe e jogador

# Atualiza as informações de um jogador
def  atualizar_jogador():
    
    dados = ler_dados()

    index = int(input("Index do Jogador: ")) -1 #O usuario entende que o indice começa em 1, mas no python começa em 0, então temos que diminuir 1, porque se a pessoa se refere ao indice 4, ele na verdade é 3

    if 0 <= index < len(dados["jogadores"]): # Confirma se o número não é negativo, se não for acessa a parte de jogadores do Json e atualiza as informações
        nome = input("Novo nome: ")
        idade = input("Nova Idade: ")
        telefone = input("Novo telefone: ")

        dados["jogadores"][index] = {
            "nome":nome,
            "idade": idade,
            "telefone":telefone
        }

        salvar_dados(dados)
        print("\nJogador Atualizado com Sucesso!")
    else:
        print("Índice Inválido")

# Atualiza as informações de um personagem
def  atualizar_personagem():
    
    dados = ler_dados()

    index = int(input("Index do Personagem: ")) -1

    if 0 <= index < len(dados["personagens"]):
        nome = input("Novo nome: ")
        idade = input("Nova Idade: ")
        classe = input("Nova Classe: ")
        jogador = input("Novo Jogador: ")

        dados["personagens"][index] = {
            "nome":nome,
            "idade": idade,
            "classe":classe,
            "jogador":jogador
        }

        salvar_dados(dados)
        print("\nPersonagem Atualizado com Sucesso!")
    else:
        print("Índice Inválido")

# Exclui algum personagem/jogador
def excluir():
    grupo = escolher_grupo()

    if not grupo:
        return
    
    dados = ler_dados()

    index = int(input(f"Index do {grupo}: ")) -1

    if 0<= index < len(dados[grupo]):
        dados[grupo].pop(index)

        salvar_dados(dados)
        print("\nExcluído com Sucesso!")

    else:
        print("Índice Inválido")

# Função main, onde se iniciará o código. Ele começa com o nosso menu e cada numero dele corresponde a uma função
def main():
    while True:
        menu()
        
        opcao = input("\nEscolha uma Opção: ")
        
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
            print("\nEncerrando o programa...")
            break

        else: 
            print("\nOpção Inválida")
main()
