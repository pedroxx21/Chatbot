def exibeResposta_GUI(texto,resposta,nome):
    return resposta.replace('Chatbot',nome)

def saudacao_GUI(nome):
    import random
    frases = ['Bom dia, meu nome é: '+ nome + '. Como você está?', 'Olá!', 'Oi, tudo bem?']
    print(frases[random.randint(0,2)])

def recebeTexto_GUI():
    texto = 'Cliente: ' + input('Cliente: ')
    palavraProibida = ['bocó']
    for p in palavraProibida:
        if p in texto:
            print('Não vem não! Me respeite!')
            return recebeTexto_GUI()
        return texto

  

def buscaResposta_GUI(texto):
    with open('BaseDeconhecimento.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if jaccard(texto,viu) > 0.3:
                    proximaLinha = conhecimento.readline()
                    if 'Chatbot: ' in proximaLinha:
                        return proximaLinha
            else:
                conhecimento.write(texto)
                return 'Me desculpe não sei o que falar'        
            
def exibeResposta_GUI(resposta,nome):
    print(resposta.replace('Chatbot',nome))
    if resposta == 'fim':
        return 'fim'
    return 'continua'            

def salva_sugestao(sugestao):
    with open('BaseDeconhecimento.txt','a+') as conhecimento:
        conhecimento.write('\nChatbot: ' + sugestao)
    
def jaccard(textoUsuario, textobase):
    textoUsuario = limpa_frase(textoUsuario)
    textobase = limpa_frase(textobase)
    if len(textobase)<1: return 0
    else:
        palavras_em_comum=0
        for palavra in textoUsuario.split():
            if palavra in textobase.split():
                palavras_em_comum+=1
        return palavras_em_comum/len(textobase.split())  

def limpa_frase(frase):
    tirar = ['.',',','!','?',';','-','_','@','#','$','%','&','*','(',')','[',']','{','}','<','>']
    for i in tirar:
        frase = frase.replace(i,'')
    frase = frase.upper()
    return frase