def countLetter(word,letter):

    arWord = list(word)
    i = 0
    countOne = 0

    while i < len(word):
        if letter == arWord[i]:
            countOne += 1
        i+=1

    print(f'\na letra "{letter}" aparece {countOne} vezes')

word = input('escolha uma palavra: ')
letter = input('escolha uma letra: ')

countLetter(word,letter)

