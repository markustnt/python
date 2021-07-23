#es game 2
#Il gioco consiste nel far inserire, dall'utente, parole contenenti "gli"
a=1
punti=0
while a==1:
    parola=input("Inserisci una parola che contenga la parola 'cese': ")
    parola=parola.lower()
    if "gli" in parola:
        punti=punti+1
        print("GIUSTO!! {} su {}".format(punti, punti))
    else:
        a=2
        print("Errato")
        print("Gioco finito")

