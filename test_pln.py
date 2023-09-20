import nltk
import collections

def extrair_palavras_mais_comuns(texto):
    # Tokenizar o texto
    tokens = nltk.word_tokenize(texto)

    # Remover as stopwords
    stopwords = nltk.corpus.stopwords.words("portuguese")
    tokens = [token for token in tokens if token not in stopwords]

    # Contar o número de ocorrências de cada palavra
    frequencia = collections.Counter(tokens)

    # Ordenar as palavras por frequência
    palavras_mais_comuns = frequencia.most_common()

    # Imprimir as palavras mais comuns
    for palavra, frequencia in palavras_mais_comuns:
        print(f"{palavra}: {frequencia}")


if __name__ == "__main__":
    # Carregar o texto
    texto = """
    Olá, mundo!

    Este é um exemplo de mineração de texto em Python.

    Neste exemplo, vamos extrair as palavras mais comuns de um texto.

    Para isso, vamos utilizar a biblioteca nltk.

    """

    # Extrair as palavras mais comuns
    extrair_palavras_mais_comuns(texto)