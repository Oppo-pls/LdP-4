lista_livros = [] #Aqui criamos uma lista vazia para armazenar os dados que serão adicionados no programa.
id_global = 0 #aqui criamos o Id que será gerado para cada livro.

def cadastrar_livro(id): #criamos a função que será usada para cadastrar os livros
    global id_global
    id_global += 1  # Aqui adicionamos +1 no id de cada livro.
    print(f'Id do livro: {id_global}')
    nome = input('Nome: ')
    autor = input('Autor: ')
    editora = input('Editora: ')

    livro = {'id' : id_global, 'nome' : nome, 'autor' : autor, 'editora' : editora} #Aqui criamos um dicionário com os dados adicionados pelo utilizador
    lista_livros.append(livro.copy())#Aqui copiamos o dicionário e com .append adicionamos ele a lista lista_livros

def consultar_livro(id):#Função para consultar livros cadastrados
    while True:#Menu em loop para escolha das opções
        cons = int(input('Escolha a opção desejada:\n'
                         '1 - Consultar Todos os Livros.\n'
                         '2 - Consultar Livro por Id.\n'
                         '3 - Consultar Livro(s) por Autor.\n'
                         '4 - Retornar.\n'))
        if cons == 1:
           for livro in lista_livros: #criamos um laço for para que seja printado os dados do livro
               print(f'Id: {livro['id']}')#Aqui é definido Id para printar e a key que será puxada para o print.
               print(f'Nome: {livro['nome']}')
               print(f'Autor: {livro['autor']}')
               print(f'Editora: {livro['editora']}\n')
        elif cons == 2:
            id_livro = int(input('Digite o Id desejado: '))#Aqui pergunta o Id do livro a ser consultado
            for livro in lista_livros:
                if livro['id'] == id_livro:
                    print(f'Id: {livro['id']}')
                    print(f'Nome: {livro['nome']}')
                    print(f'Autor: {livro['autor']}')
                    print(f'Editora: {livro['editora']}\n')
        elif cons == 3:#Elif para consulta por autor, buscando por todos os livros que tenham o mesmo autor
            id_autor = input("Digite o Autor desejado: ")
            for livro in lista_livros:#
                if livro['autor'] == id_autor:
                    print(f'Id: {livro['id']}')
                    print(f'Nome: {livro['nome']}')
                    print(f'Autor: {livro['autor']}')
                    print(f'Editora: {livro['editora']}\n')
        elif cons == 4:#Aqui saímos do menu com break, retornando para o menu anterior
            print('Retornando...')
            break
        else:
            print('Opção inválida. Escolha novamente.\n')
            continue#Caso uma opção inválida, o programa reinicia o menu
def remover_livro():#função para remover livro pelo id
    id_remove = int(input('Digite o Id do livro a ser removido: '))#perguntamos pelo Id do livro
    for livro in lista_livros: #definimos que deve pesquisar pelo livro na lista_livros
        if livro['id'] == id_remove:#Aqui verificamos se o Id digitado corresponder a um livro em lista_livro
            lista_livros.remove(livro)#Caso o id seja validado, ele será removido da lista
            print('Livro removido com sucesso!\n')

print('Bem-vindo(a) a Livraria do Matheus Ferreira')
print('-'*46)
print('-'*15,'MENU PRINCIPAL','-'*15)

while True:
    menu = int(input('Escolha a opção desejada:\n'
                     '1 - Cadastrar Livro.\n'
                     '2 - Consultar Livro(s).\n'
                     '3 - Remover Livro.\n'
                     '4 - Sair.\n'))

    if menu == 1:
        cadastrar_livro(id_global)#Chamamos as funções que serão executadas

    elif menu == 2:
        consultar_livro(lista_livros)

    elif menu == 3:
        remover_livro()

    elif menu == 4:
        print('Encerrando...')
        break
    else:
        print('Opção inválida. Escolha novamente.\n')
        continue
