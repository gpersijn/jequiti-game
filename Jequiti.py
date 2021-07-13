print('Olá, tudo bem? Bem vindo à palavra sortida Jequiti.\n'
      'Caso você acerte qual é a palavra, ganhará um prêmio de R$100.000,00\n'
      'O tema da palavra é: Objeto\n'
      'Boa sorte!')

palavra_sortida = 'escada'
digitadas = []
recomece = 1
tente = ''
a = ['sim', 's']

while recomece == 1:
    x = 0
    while x < 5:
        letra = input('\nDigite uma letra: ')
        letra = letra.lower()

        if len(letra)>1:
            print('Você só pode digitar uma letra por vez!')
            continue

        if letra in palavra_sortida:
            digitadas.append(letra)
            print('Uaau! Você acertou uma letra!')
        else:
            print('Que penaa! Essa letra não tem na palavra!')

        palavra_secreta = ''
        for item in palavra_sortida:  # escada
            if item in digitadas:  # [e, c]
                palavra_secreta += item  # palavra_secreta = e*****
            else:
                palavra_secreta += '*'

        print(f'-----  Palavra: {palavra_secreta}  -----')
        x += 1
    digitadas.clear()

    if x == 5:

        palavra_sortida = 'escada'
        responda = input('\nSuas chances acabaram!\nHora da verdade: Você descobriu a palavra secreta? (S/N)\n')
        responda = responda.lower()
        if responda in a:
            resposta = input('Que bom! Qual é a resposta correta?\n')
            resposta = resposta.lower()
            if resposta == palavra_sortida:
                print('PARAAABÉEEENS! Você acaba de ganhar R$100.000,00 :)')
                recomece = 0
            else:
                tente = input('Infelizmente, a resposta não é essa. Não tem problema! Gostaria de tentar mais uma '
                              'vez? (S/N)\n')
        else:
            tente = input('Que pena... Gostaria de tentar mais uma vez? (S/N)\n')

        tente = tente.lower()
        if tente in a:
            recomece = 1
        else:
            recomece = 0

print('Obrigado por participar! Volte sempre!')
