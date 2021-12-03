def genera_lista():
    participantes = ['Juan', 'Luis','Maria']

    print(participantes)
    return participantes

part = ['Juan', 'Luis','Maria'].append("Rodrigo")

part = genera_lista()

part[0] = "Mario"

print(genera_lista())  #(['Juan', 'Luis','Maria'])

part = genera_lista

part()