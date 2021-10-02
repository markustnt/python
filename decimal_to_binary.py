n=int(input('INSERISCI NUMERO DECIMALE:'))
b=''
while n>0:
    if  n%2==0:
        b='0'+b
    else:
        b='1'+b
    n=int(n/2)

print(b)
