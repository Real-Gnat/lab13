class SportBuildingsManager:

    def __init__(self, sport_buildings):
        self.sport_buildings = list(sport_buildings)

    def find_by_viewers_number(self, min, max):
        return [building for building in self.sport_buildings
                if (min <= building.viewers_number <= max)]

    def sort_by_sport_kind(self, sport_buildings):
        sport_buildings.sort(key=lambda building: building.sport_kind.value)

    def sort_by_sport_season(self, sport_buildings):
        sport_buildings.sort(key=lambda building: building.sport_season.value)

    def print_sport_buildings_info(self, sport_buildings):
        for building in sport_buildings:
            print(building)
