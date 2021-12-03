def genera_lista():
    participantes = ['Juan', 'Luis','Maria']

    print(participantes)
    return participantes

part = genera_lista()

part[0] = "Mario"

print(genera_lista())