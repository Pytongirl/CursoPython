CURRENT_YEAR=2021     ##Aqui es mejor no hacer hard coded un valor k puede cambiar en el tiempo
def calc_year_born(x, y=CURRENT_YEAR):   ##Aqui es mejor p¿remplazar la variable CURRENT_YEAR por el año k deseamos
    year_born = (y - x)
    return f"Usted nació en el año:{year_born}"

print(calc_year_born(30))

# print(calc_year_born(30, 2025))
current_year =2025
print(calc_year_born(36))

###ef get_age(age: int):
##return age
##get_age("hola")