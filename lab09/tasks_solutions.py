import modul

help(modul)
avg_age = modul.get_average_from_file('daty.in', mode = 'liberalny')
print(f'Średnia wieku osób wynosi: {avg_age} lat')