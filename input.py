#markusTNT                       *****INPUT*****

nome=input("Inserisci il tuo nome: ")
età=input("Inserisci la tua età: ")

età=int(età)  #conersione variabile da stinga a intero

#si può anche scivere:
#età=int(input("Inserisci la tua età: ")) 

if età>=18:
    print("Complimenti {}, sei maggiorenne".format(nome))
else:
    print("Ci dispiace {}, ma non sei ancora maggiorenne".format(nome))
