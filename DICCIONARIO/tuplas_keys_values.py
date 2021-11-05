dict1 = {
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco"
   } 

for caracter in paragaph:
    if caracter in ocurrences:
        ocurences[character]+=1
        ocurences.update({character: 1})

dict1.items()>-return una lista de tuplas
#???????[('t',1), ('w', 4)]
# for key.value in ocurences.items):
#     print(f"el caracter '{key}' aparece{value} veces")

for im_a_tupple in ocurences.items():
    print(f"el caracter '{im_a_tupple[0]}' aparece{im_a_tupple[1]} veces")