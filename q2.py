#Escreva uma função que receba uma lista de palavras e retorne a maior dessas palavras

def maiorPalavra(listaPalavras):
    word_len = []
    for n in listaPalavras:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(maiorPalavra(["casa", "chiqueiro", "lua"]))

