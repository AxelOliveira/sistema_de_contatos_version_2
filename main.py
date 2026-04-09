ARQUIVO = 'contatos.txt'

# 1 - Função para salvar contatos no arquivo
def salvar_contatos(contatos):
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        for contato in contatos:
            arquivo.write(f"{contato['nome']};{contato['telefone']}\n")

# 2 - Função para carregar contatos do arquivo
def carregar_contatos():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            contatos = []
            for linha in arquivo:
                nome, telefone = linha.strip().split(';')
                contatos.append({'nome': nome, 'telefone': telefone})
            return contatos
    except FileNotFoundError:
        return []
    
# 3 - Função para padronizar o nome
def padronizacao_nome(nome_contato):
    palavras = [palavra.capitalize() for palavra in nome_contato.split()]
    return ' '.join(palavras)

# 4 - Função para validar telefone
def contato_telefone():
    while True:
        numero_telefone = input('Digite o número do contato: ')
        if not numero_telefone.isdigit():
            print('Informar somente números.')
            continue

        if len(numero_telefone) != 11:
            print('O telefone deve conter 11 dígitos.')
            continue

        return numero_telefone
    
# 5 - Função para verificar duplicado
def verificar_duplicado(nome, telefone, contatos):
    for contato in contatos:
        if contato['nome'] == nome and contato['telefone'] == telefone:
            return True
        
    return False

# 6 - Função formatar número
def formatar_telefone(telefone):
    return f"({telefone[0:2]}) {telefone[2:3]} {telefone[3:7]}-{telefone[7:11]}"

# 7 - Função principal para adicionar contato
def adicionar_contato(contatos):
    while True:
        nome_contato = input('Digite o nome do contato: ')
        valido = True

        for letra in nome_contato:
            if letra.isdigit():
                valido = False
                break

            if not valido:
                print('O nome não pode conter números.')
                continue
            else:
                break

        nome = padronizacao_nome(nome_contato)

        telefone = contato_telefone()

        if verificar_duplicado(nome, telefone, contatos):
            print('Contato já existe.')
            return
        
        contato = {
            'nome': nome,
            'telefone': telefone
        }

        contatos.append(contato)

        salvar_contatos(contatos)

        print('Contato adicionado com sucesso!')

# 8 - Função para listar contatos
def listar_contatos(contatos):
    if not contatos:
        print('Nenhum contato adicionado.')
        return
    
    print('\n--- CONTATOS ---')
    for contato in contatos:
        telefone_formatado = formatar_telefone(contato['telefone'])
        print(f'{contato['nome']} - {telefone_formatado}')
    print()

# 9 - Programa principal
contatos = carregar_contatos()

while True:
    print('Comandos: adicionar, listar, sair')
    comando = input('Digite um comando: ')

    if comando == 'adicionar':
        adicionar_contato(contatos)

    elif comando == 'listar':
        listar_contatos(contatos)

    elif comando == 'sair':
        print('Encerrado...')
        break

    else:
        print('Comando inválido.')