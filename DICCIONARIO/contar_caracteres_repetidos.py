##  da errores "pararfo="anita lava la tina"

parrafo="pablito clavó un clavito cuando estaba en el kinder en 1980"
entry=input ("entry a lookup character: ")
ocurences={} 

for character in parrafo:
        if character in ocurences: 
        ocurences[character] += 1
        else:
        ocurences [character] =0
        
print(ocurences)
