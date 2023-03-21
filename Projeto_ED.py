class Filmes:
    def __init__(self, nome_filme, ano, genero, diretor):
        self.nome_filme = nome_filme
        self.ano = ano
        self.genero = genero
        self.diretor = diretor
        self.next = None
class Lista_de_Filmes:
    def __init__(self):
        self.head = None
    def adiciona_filmes(self, nome_filme, ano, genero, diretor):
        filme_novo = Filmes(nome_filme, ano, genero, diretor)
        filme_novo.next = self.head
        self.head = filme_novo
    def remove_filmes(self, nome_filme):
        filme_atual = self.head
        previous = None
        while filme_atual is not None:
            if filme_atual.nome_filme == nome_filme:
                if previous is None:
                    self.head = filme_atual.next
                else:
                    previous.next = filme_atual.next
                return True
            previous = filme_atual
            filme_atual = filme_atual.next
        return False
    def mostrar_filmes(self):
        filme_atual = self.head
        while filme_atual is not None:
            print("Nome do filme:", filme_atual.nome_filme)
            print("Ano de lançamento:", filme_atual.ano)
            print("Gênero:", filme_atual.genero)
            print("Diretor:", filme_atual.diretor)
            print("=" * 30)
            filme_atual = filme_atual.next
lista_Filmes = Lista_de_Filmes()
while True:
    print("1 - Adicionar Filme")
    print("2 - Remover Filme")
    print("3 - Mostrar Filmes")
    print("4 - Fechar")
    opcao = int(input("Digite a opção:"))
    if opcao == 1:
        nome_filme = input("Digite o nome do filme:")
        ano = int(input("Digiter o ano de lançamento do filme:"))
        genero = input("Digite o gênero do filme:")
        diretor = input("Digite o nome do diretor do filme:")
        lista_Filmes.adiciona_filmes(nome_filme, ano, genero, diretor)
        print("Filme adicionado com sucesso!")
    elif opcao == 2:
        nome_filme = input("Digite o nome do filme que deseja remover:")
        if lista_Filmes.remove_filmes(nome_filme):
            print("Filme Removido com sucesso!")
        else:
            print("Filme não encontrado!")
    elif opcao == 3:
        if lista_Filmes.head is None:
            print("Nenhum filme encontrado!")
        else:
            lista_Filmes.mostrar_filmes() 
    elif opcao == 4:
        break
    else:
        print("Opção inválida, tente novamente!")
