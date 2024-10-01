import os
class Livro:
    def __init__(self,autor,editora,ISBN,titulo,ano):
        self.autor = autor
        self.editora = editora
        self.isbn = ISBN
        self.titulo = titulo
        self.ano = ano
    def __str__(self):
        return f'Livro: {self.titulo.title()}, Editora: {self.editora.title()}, Autor: {self.autor.title()}, ISBN: {self.isbn}, Data: {self.ano}'

def linha():
    print('-' * 8)

livros = []

while True:
    print('LIVRARIA DUELOS')
    linha()
    print('SEJA BEM VINDO')
    print('''OPCOES:
    [1] Cadastrar livro
    [2] Buscar livro(titulo)
    [3] Buscar livro(autor)
    [4] Listar todos os livros
    [0] sair''')

    escolha = int(input('Digite sua opcao: '))

    if escolha == 1:
        autor = input("Digite o nome do autor: ")
        editora = input("Digite o nome da editora: ")
        isbn = int(input("Codigo do produto: "))
        titulo = input("Titulo do livro: ")
        ano = (input("Data: "))

        livro = Livro(autor,editora,isbn,titulo,ano)
        livros.append(livro)
        os.system('clear')
    elif escolha == 2:
        busca = input("Digite o titulo do livro que deseja buscar: ")
        chave = False
        for l in livros:
            if l.titulo == busca:
                print(l)
                chave = True
        if not chave:
            print("Nenhum livro encontrado.")

    elif escolha == 3:
        busca = input("Digite o nome do autor: ")
        chave = False
        for l in livros:
            if l.autor == busca:
                print(l)
                chave = True
        if not chave:
            print("Esse autor nao possui livros.")

    elif escolha == 4:
        for l in livros:
            print(l)

    elif escolha == 0:
        print('Saindo...')
        break

    else:
        print("Opcao invalida.")
        