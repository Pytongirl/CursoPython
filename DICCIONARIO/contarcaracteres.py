##ok Conta cierto caracer input en 1 prase

parrafo="pablito clavó un clavito cuando estaba en el kinder en 1980"
entry=input ("entry a lookup character: ")
counter = 0
for character in parrafo:
    if character == entry:
        counter+=1        
print(counter)