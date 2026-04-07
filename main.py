# 1 - Função: adicionar_contato
def adicionar_contato(contatos):

# 2 - Valida nome:
    while True:

# 3 - Pede nome ao usuário
        nome_contato = input('Digite o nome do contato: ')

        valido = True

#       4 - Percorre todo o nome do contato
        for letra in nome_contato:

#               5 - Se tiver número no nome o sistema para
                if letra.isdigit():
                    valido = False
                    break

#       6 - Se inválido → pede novamente até corrigir
        if not valido:
             print('O nome não pode conter números.')
             continue
        
        # 7 - Se não tiver o sistema continua
        else:
             break
     
# Padroniza nome:
# 8 - Primeira letra de cada palavra maiúscula
def padronizacao_nome(nome_contato):
     
    # 9 - A variavel nome recebe o nome do contato
    nome = nome_contato

    # 10 - Retira todos os espaços do nome e formata para que todo nome tenha a primeira letra maiuscula
    palavras = [palavra.capitalize() for palavra in nome.split()]

    # 11 - Faz a junção dos nomes com letras maiusculas
    nome_padronizado = " ".join(palavras)

    return nome_padronizado

def contato_telefone():
    while True:  

# Pede telefone ao usuário
        numero_telefone = input('Digite o número do contato: ')

# Valida telefone:
#     - Deve conter apenas números
        if not numero_telefone.isdigit():
            print('Informar somente números.')
            continue
        
#     - Deve ter exatamente 11 dígitos
        if len(numero_telefone) != 11:
            print('Você está informado números insuficiente.')
            continue
        
        break

    return numero_telefone

# Verifica duplicado:
#     - Percorre a lista de contatos
    
#     - Para cada contato:
#         - Compara nome e telefone
#     - Se encontrar igual:
#         - Mostra mensagem de erro
#         - NÃO adiciona
#         - Encerra a função
# ↓
# Se não for duplicado:
#     - Cria dicionário:
#         {'nome': nome, 'telefone': telefone}
# ↓
# Adiciona o contato na lista
# ↓
# Salva a lista no arquivo
# ↓
# Mostra mensagem de sucesso
