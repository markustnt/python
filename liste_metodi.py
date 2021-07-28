#Una lista è una variabile che contiene più elementi
lista1=["ciao a tutti", 23, "buonasera"]
print(lista1)

#Per accedere ad ogni elemento della lista utilizziamo le slice
print(lista1[1])
print() #spazio
print(lista1[1:])
print() #spazio
print(lista1[:1])

#lista gestita con il cilco for

for indice in lista1: #esegui un ciclo che ha come indice una variabile indice per tutta la lista provola
    print(lista1)

#possiamo verificare se un elemento è all'interno della stringa
lista1=["ciao a tutti", 23, "buonasera"]
print("casa" in lista1) #va a verificare se è presente un pezzo ma l'intera variabile

#con .append verrà aggiunto un elemento alla lista

lista1=["ciao a tutti", 23, "buonasera"]
lista1.append("ciao")
print(lista1)

#per inserire un elemento alla lista in modo più preciso si utilizza .insert

lista1=["ciao a tutti", 23, "buonasera"]
lista1.insert(2,"eccomi")
print(lista1)


#per rimuovere un elemento dalla lista si utilizza .remove

lista1=["ciao a tutti", 23, "buonasera"]
lista1.remove("buonasera")
print(lista1)


#per capire in quale posizione della lista si trova un elemento si utilizza .index

print(lista1.index(23))


#per calcolare quante volte un elemento è presente nella lista si utilizza .count

lista1=[23,"ciao a tutti", 23, "buonasera",23]
print(lista1.count(23))


#per ordinare gli elementi in ordine alfabetico si utilizza .sort

lista1=["ciao a tutti", "buonasera", "abaco", "zucca", "marco"]
lista1.sort()
print(lista1)

#per cancellare completamente una lista si utilizza .clear

lista1.clear()
print(lista1)
