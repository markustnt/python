#markustnt          *****CALCOLATRICE*****

continua="s"

while continua=="s":
        print('''Benvenuto nella calcolatrice
        Per effettuare una ADDIZIONE premere 1;
        Per effettuare una SOTTRAZIONE premere 2;
        Per effettuare una MOLTIPLICAZIONE premere 3;
        Per effettuare una DIVISIONE premere 4;''')

        print()
        a=int(input(''))
        print()
        if a==1:
            print("ADDIZIONE")
            num1=int(input("Inserisci il primo numero: "))
            num2=int(input("Inserisci il secondo numero: "))
            risultato=num1+num2
            print("Il risultato è:",risultato)
        elif a==2:
            print("SOTTRAZIONE")
            num1=int(input("Inserisci il primo numero: "))
            num2=int(input("Inserisci il secondo numero: "))
            risultato=num1-num2
            print("Il risultato è:",risultato)
        elif a==3:
            print("MOLTIPLICAZIONE")
            num1=int(input("Inserisci il primo numero: "))
            num2=int(input("Inserisci il secondo numero: "))
            risultato=num1*num2
            print("Il risultato è:",risultato)
        elif a==4:
            print("DIVISIONE")
            num1=int(input("Inserisci il primo numero: "))
            num2=int(input("Inserisci il secondo numero: "))
            risultato=num1/num2
            print("Il risultato è:",risultato)
        else:
            print("Il numero inserito non è corretto.")
            continua="a"

        continua=input("Digita 's' per continuare a fare calcoli, altrimenti premi un alto tasto: ")    


print("---OFF---")
return(0)
