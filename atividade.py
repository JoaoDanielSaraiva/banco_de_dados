data_base = {}

# Nome
# senha
# email

def cadastrar():
    nome = input()
    senha = input()
    r_senha = input()
    email = input()
    

def escolha(c):
    if c == '1':
        print('cadastrar()')
    elif c == '2':
        print('consultar()')
    elif c == '0':
        print('sair()')
    else:
        print("Escolha inválida")
    
def interface():
    print("banco de dados")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("0 - Sair")
    c = input()
    escolha(c)

interface()