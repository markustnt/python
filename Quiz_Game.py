#markusTNT                *****QUIZ*****

print("Quiz Game")


lista=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto']
lista1=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto']
i=1
while i==1:
    if len(lista)==0:
        i=0
        break
    else:
        word=input("Planets of the solar system:").lower()
        if word in lista:
            print(word)
            lista.remove(word)
        elif word in lista1:
            print('already inserted')
        else:
            print('incorrect')

print('CONGRATULATION, YOU GUESSED ALL THE PLANETS!!')
