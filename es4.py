#markusTNT     *****ES riordinatore di liste*****

oggetti_raccolti=["legna","pietre", "legna", "pietre", "pietre", "diamante", "arco", 'arco', 'freccia','fiore', 'fiore', 'freccia', 'cibo','cibo','cibo','cibo', 'fiore', 'fiore']
inventario=[]

for index in oggetti_raccolti:
    if index in inventario:
        pass
    else:
        inventario.append(index)

print(oggetti_raccolti)
print()
print(inventario)
