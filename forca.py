palavra_secreta = 'LARANJA'
tamanho = len(palavra_secreta)
acertos = 0
ja_foi = []

partes_corpo = ['Cabeça', 'Tronco', 'Braço esquerdo', 'Braço direito',
                'Perna esquecer', 'Perna direita']

digitadas = []
for letra in palavra_secreta:
    digitadas.append('___')

def mostrar_digitadas():
    print('palvra_secreta: ', end='')
    for item in digitadas:
        print(f'{item}', end='')

def salvar_letra(letra):
    ind = 0
    encontrou = 0
    for c in palavra_secreta:
        if (c == letra):
            digitadas[ind] = letra
            encontrou += 1
        ind += 1
    return encontrou

print('\n\n\t##########################')
print('\t#Bem Vindo ao Jogo da Forca #')
print('\t#############################\n\n')

mostrar_digitadas()

while True:
        letra = input('\nDigite uma letra:').upper()

        if letra in ja_foi:
            print('\nJá foi Digitada! Tente outra.')
            continue

        ja_foi.append(letra)

        if (letra in palavra_secreta):
            print('\nAcertou! Tente outra ')
            acertos += salvar_letra(letra)
            mostrar_digitadas()

            if (acertos == tamanho):
                print('\nVocê venceu, Parabéns !!')
                break

        else:
            print('\nErrou! Enforcou:', partes_corpo[0])
            del partes_corpo[0]
            if(len(partes_corpo) == 0):
                print('\n Você perdeu! HAHAHAHA')
                break






