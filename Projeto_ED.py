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
        filme_novo = Filme(nome_filme, ano, genero, diretor)
        filme_novo.next = self.head
        self.head = filme_novo
lista_Filmes = Lista_de_Filmes()
print(lista_Filmes)

nome_filme = input("Digite o nome do filme:")
ano = int(input("Digiter o ano de lançamento do filme:"))
genero = input("Digite o genero do filme:")
diretor = input("Digite o nome do dirtetor do filme:")

print("Nome do filme:", nome_filme)
print("Ano de lançamento:", ano)
print("Gênero:", genero)
print("Diretor do filme", diretor)
