import random

elenco=['Rossi', 'Ferrari', 'Russo', 'Bianchi', 'Romano', 'Gallo', 'Costa', 'Fontana', 'Conti', 'Esposito', 'Ricci', 'Bruno', 'De Luca', 'Moretti', 'Marino', 'Greco']
elenco.sort()
numero=random.randint(1,16)
print('La persona sorteggiata è:', elenco[numero])
