def merge_countries_capitals():
    list_countries = input().split(", ")
    list_capitals = input().split(", ")
    countries_capitals = dict(zip(list_countries, list_capitals))
    for key, value in countries_capitals.items():
       print(f"{key} -> {value}")



merge_countries_capitals()
# print(merge_countries_capitals(countries_capitals))