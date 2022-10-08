"""
Дописаить класс GreenZoneIndex
"""


class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """

        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones

        self.green_index = self.calculate_green_index()  # индекс озеленения

    def calculate_green_index(self):
        """
        Метод для вычисления индекса озеленения.

        Индекс рассчитывается как отношение площади всех парков к площади территории
        """

        return round(sum(self.green_zones) / self.territory_area * 100, 2)


if __name__ == "__main__":

    territory_name = "Пушкин"
    territory_area = 28676
    green_zones = [302, 487, 420, 325, 471, 363, 404]
    my_green_zone_index = GreenZoneIndex(territory_name, territory_area, green_zones)
    print(my_green_zone_index.green_index)
    # Ожидаемый ответ Индекс озеленения территории Пушкин равен 9.67%
