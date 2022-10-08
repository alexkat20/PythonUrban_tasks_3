"""
Написать функцию filter_min_green_index,
которая в качестве аргументов принимает список объектов типа GreenZoneIndex
и минимальный порог озеленения, значение по умолчанию 0.1.

Результатом функции должно быть число территорий,
индекс озеленения которых ниже заданного минимального порога.
"""


from task1 import GreenZoneIndex
from typing import List


def filter_min_green_index(green_zone_list: List[GreenZoneIndex], green_threshold: float = 0.1) -> int:
    """
    A function to filter territories
    :param green_zone_list: A list with green zone territories
    :param green_threshold: A threshold to filter territories
    :return: The amount of territories with the index below green_threshold
    """

    areas_counter = 0

    for territory in green_zone_list:
        if territory.green_index < green_threshold:
            areas_counter += 1

    return areas_counter


list_territories = [
    {"territory_name": "Пушкин", "territory_area": 28676783675, "green_zones": [302, 487, 420, 325, 471, 363, 404]},
    {"territory_name": "Павловск", "territory_area": 21025234354, "green_zones": [360, 375, 223, 258, 345, 296, 303]},
    {"territory_name": "Петергоф", "territory_area": 44274, "green_zones": [364, 447, 438, 223, 336, 431, 442]},
]

green_zone_territories = []

for green_zone_index in list_territories:
    new_green_zone_index = GreenZoneIndex(
        green_zone_index["territory_name"], green_zone_index["territory_area"], green_zone_index["green_zones"]
    )
    green_zone_territories.append(new_green_zone_index)


print(filter_min_green_index(green_zone_territories))
