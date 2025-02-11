import string

#Regresa el texto sin signos de puntuación
def deletePunctuation(text):
    textFile = open(text, "r", encoding="utf8")
    punctuationText = textFile.read()
    newText = punctuationText.translate(str.maketrans("","", string.punctuation))
    textFile.close()
    return newText

#Devuelve un set para recuperar las palabras sin repetir del texto
def getSetFromText(text):
        wordsSet = set(text.split())
        return wordsSet

#Escribe el nuevo archivo embedding
def writeEmbedding(fastTextFile, embeddingFile, wordsSet):
    with open(fastTextFile, "r", encoding="utf8") as readingFastTextFile:
        with open(embeddingFile, "w", encoding="utf8") as writingEmbeddingFile:
           for line in readingFastTextFile:
                lineWords = set(line.split()) 
                #Si alguna palabra del set coincide con alguna palabra de la línea, escribe la línea en el nuevo embedding 
                if wordsSet & lineWords:  
                    writingEmbeddingFile.write(line)


book = "El Alquimista.txt"
fastTextFile = "cc.es.300.vec"

noPunctuationBook = deletePunctuation(book)
bookWordsSet = getSetFromText(noPunctuationBook)
print(bookWordsSet)
writeEmbedding(fastTextFile, "New embedding file.txt", bookWordsSet)