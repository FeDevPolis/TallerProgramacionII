#planet_moons = {
#   "mercury": 0,
#   "venus": 0,
#   "earth": 1,
#   "mars": 2,
#   "jupiter": 79,
#   "saturn": 82,
#   "uranus": 27,
#   "neptune": 14,
#   "pluto": 5,
#   "haumea": 2,
#   "makemake": 1,
#   "eris": 1
#}
#Calcular cantidad de lunas del sistema solar.
#Calcular promedio de lunas por planetas.

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
total_moons = 0

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Thera are {total_moons} moons')

print(f'Each planet has an average of {average} moons')
