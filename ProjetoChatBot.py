def saudacoes(nome):
    import random
    frases = ['Bom dia, meu nome é: '+ nome + '. Como você está?', 'Olá!', 'Oi, tudo bem?']
    print(frases[random.randint(0,2)])

def recebeTexto():
    texto = 'Cliente: ' + input('Cliente: ')
    palavraProibida = ['bocó']
    for p in palavraProibida:
        if p in texto:
            print('Não vem não! Me respeite!')
            return recebeTexto()
        return texto

def buscaResposta(nome,texto):
    with open('BaseDeconhecimento.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if texto.replace('Cliente: ','') == 'Tchau':
                    print(nome+ ': volte sempre!')
                    return 'fim'
                elif viu.strip() == texto.strip():
                    proximaLinha = conhecimento.readline()
                    if 'Chatbot: ' in proximaLinha:
                        return proximaLinha
            else:
                print('Me desculpe, não sei responder isso!')
                conhecimento.write('\n' + texto)
                respota_user = input('O que esperava?\n')
                conhecimento.write('\nChatbot: ' + respota_user)
                return 'Hum... interessante!'

def exibeResposta(resposta,nome):
    print(resposta.replace('Chatbot',nome))
    if resposta == 'fim':
        return 'fim'
    return 'continua'            
