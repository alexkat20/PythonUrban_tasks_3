"""
Написать функцию get_mean_green_index,
которая в качестве аргумента принимает список объектов типа GreenZoneIndex и считает от них средний индекс озеленения.
"""


from task1 import GreenZoneIndex
from typing import List


def get_mean_green_index(green_zone_list: List[GreenZoneIndex]) -> float:
    """
    A function to get the mean green index
    :param green_zone_list: A list with GreenZoneIndex elements
    :return: a mean index of all the elements in the list
    """
    mean_index = 0
    for element in green_zone_list:
        mean_index += element.green_index

    mean_index /= len(green_zone_list)

    return mean_index


list_territories = [
    {"territory_name": "Пушкин", "territory_area": 28676, "green_zones": [302, 487, 420, 325, 471, 363, 404]},
    {"territory_name": "Павловск", "territory_area": 21025, "green_zones": [360, 375, 223, 258, 345, 296, 303]},
    {"territory_name": "Петергоф", "territory_area": 44274, "green_zones": [364, 447, 438, 223, 336, 431, 442]},
]

green_zone_territories = []

for green_zone_index in list_territories:
    new_green_zone_index = GreenZoneIndex(
        green_zone_index["territory_name"], green_zone_index["territory_area"], green_zone_index["green_zones"]
    )
    green_zone_territories.append(new_green_zone_index)


print(get_mean_green_index(green_zone_territories))
