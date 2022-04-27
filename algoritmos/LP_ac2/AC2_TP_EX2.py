def isTautograma(sentence):
    trueSentence = sentence.lower()
    sentenceArr = trueSentence.split(" ")
    verifyWords = []

    for words in sentenceArr:
        if words[0] == trueSentence[0]:
                verifyWords.append(words)
    
    if len(sentenceArr) == len(verifyWords):
        return "Y"
    else: 
        return "N"

sentence = input()
print(isTautograma(sentence))