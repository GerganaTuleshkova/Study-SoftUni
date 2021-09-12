countries = input().split(", ")
capitals = input().split(", ")

dict_countries = dict(zip(countries, capitals))

for country, capital in dict_countries.items():

    print(f"{country} -> {capital}")

