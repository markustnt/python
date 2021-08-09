#markusTNT                *****QUIZ*****

print("Quiz Game")


lista=['mercurio','venere','terra','marte','giove','saturno','urano','nettuno','plutone']
lista1=['mercurio','venere','terra','marte','giove','saturno','urano','nettuno','plutone']
i=1
while i==1:
    if len(lista)==0:
        i=0
        break
    else:
        parola=input("Pianeti del sistema solare:").lower()
        if parola in lista:
            print(parola)
            lista.remove(parola)
        elif parola in lista1:
            print('già inserito')
        else:
            print('errato')

print('HAI INDOVINATO TUTTE LE PAROLE!!')
