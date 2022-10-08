list_cities = [
    {
        "name": "Москва",
        "population": 12 * 10**6,
    },
    {
        "name": "Санкт-Петербург",
        "population": 5 * 10**6,
    },
    {
        "name": "Ижевск",
        "population": 0.6 * 10**6,
    },
]

filter_population = 10**6

list_cities = [city for city in list_cities if city["population"] > 10**6]

print(*list_cities)
