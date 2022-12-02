import 
import os

def logo_inicial():
    print(r"""
_________ _______  _______  _______             ______   _______             _______  _______  _______  _______  _______ 
\__    _/(  ___  )(  ____ \(  ___  )           (  __  \ (  ___  )           (  ____ \(  ___  )(  ____ )(  ____ \(  ___  )
   )  (  | (   ) || (    \/| (   ) |           | (  \  )| (   ) |           | (    \/| (   ) || (    )|| (    \/| (   ) |
   |  |  | |   | || |      | |   | |   _____   | |   ) || (___) |   _____   | (__    | |   | || (____)|| |      | (___) |
   |  |  | |   | || | ____ | |   | |  (_____)  | |   | ||  ___  |  (_____)  |  __)   | |   | ||     __)| |      |  ___  |
   |  |  | |   | || | \_  )| |   | |           | |   ) || (   ) |           | (      | |   | || (\ (   | |      | (   ) |
|\_)  )  | (___) || (___) || (___) |           | (__/  )| )   ( |           | )      | (___) || ) \ \__| (____/\| )   ( |
(____/   (_______)(_______)(_______)           (______/ |/     \|           |/       (_______)|/   \__/(_______/|/     \| 

by Gianluca Zugno
    """)

def wordlist():
    # [] cria uma lista
    palavras = []
    with open("C:/Users/skyla/Desktop/Forca/palavras.txt", "r", encoding="utf-8") as list:
        # loop para ler todas palavras.
        for linha in list:
            # strip remove os espaços em branco
            linha = linha.strip()
            # append junta a palavra selecionada com a lista.
            palavras.append(linha)

    # len retorna o comprimentro.
    numero = random.randrange(0, len(palavras))
    # upper deixa a palavra toda em maiúsculo
    resposta = palavras[numero].upper()
    return resposta

def acertos(palavra):
    return ["_" for letra in palavra]

def input_alt():
    chute = input("Digite a letra: ")
    chute = chute.strip().upper()
    return chute

def correto(chute, lc, resposta):
    index = 0
    for letra in resposta:
        if (chute == letra):
            lc[index] = letra
        index += 1

def vitoria():
    # r """ permite que possa fazer um print de ascii
    print(r"""
        .-=========-.
        \'-=======-'/
        _|   .=.   |_
        ((| {{1}}  |))
        \|   /|\   |/
         \__ '`' __/
           _`) (`_
         _/_______\_
        /___________\  
    """)

def derrota(resposta):
    os.system("cls")
    print("Perdeu")
    print("A palavra era {}".format(resposta))
    print(r"""  
        __  __
        \ \/ /
         >  < 
        /_/\_\
    """)

def ascii_erro(erros):


    if(erros == 1):
        os.system("cls")
        print(r"""
          _______   
        |/      |  
        |      (_)   
        |            
        |            
        """)

    if(erros == 2):
        os.system("cls")
        print('Você ainda tem {} tentativas'.format(7-erros))
        print(r"""
          _______   
        |/     |  
        |     (_)   
        |     \     
        |            
        |            
        """)

    if(erros == 3):
        os.system("cls")
        print('Você ainda tem {} tentativas'.format(7-erros))
        print(r"""
          _______   
        |/     |  
        |     (_)   
        |     \|    
        |            
        |            
        """)

    if(erros == 4):
        os.system("cls")
        print('Você ainda tem {} tentativas'.format(7-erros))
        print(r"""" 
          _______   
        |/      |  
        |      (_)   
        |      \|/  
        |            
        |              
        """)

    if(erros == 5):
        os.system("cls")
        print('Você ainda tem {} tentativas'.format(7-erros))
        print(r"""
          _______   
        |/      |  
        |      (_)   
        |      \|/   
        |       |    
        |              
        """)

    if(erros == 6):
        os.system("cls")
        print('Você ainda tem {} tentativas'.format(7-erros))
        print(r""""
          _______   
        |/      |  
        |      (_)   
        |      \|/   
        |       |    
        |      /     
        """)

    if (erros == 7):
        os.system("cls")
        print('Você ainda tem {} tentativas'.format(7-erros))
        print(r"""
          _______   
        |/      |  
        |      (_)   
        |      \|/   
        |       |    
        |      / \   
        """)

    print(r""""
         |            
        _|___     
    
    """)    
    print()

def forca():

    logo_inicial()

    resposta = wordlist()

    lc = acertos(resposta)

    errou = False
    acertou = False
    erros = 0
    faltando = len(lc)

    print(lc)
    while (not acertou and not errou):

        chute = input_alt()

        if (chute in resposta):
            correto(chute, lc, resposta)
            # count retorna o numero de elementos com o valor especifico
            faltando = str(lc.count('_'))
            if (faltando == "0"):
                print("Acerto '{}'".format(resposta.upper()))
        else:
            erros += 1
            print(lc)
            print('Ainda faltam acertar {} letras'.format(faltando))
            ascii_erro(erros)

        errou = erros == 7
        acertou = "_" not in lc

        print(lc)

    if (acertou):
        vitoria()
    else:
        derrota(resposta)

    print("Fim do jogo")

if(__name__ == '__main__'):
    forca()
