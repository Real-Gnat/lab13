from src.managers.SportBuildingsManager import SportBuildingsManager
from src.models.AquaticsHall import AquaticsHall
from src.models.AthleticsPlayground import AthleticsPlayground
from src.models.ChessHall import ChessHall
from src.models.FootballField import FootballField
from src.models.ShootingPlayground import ShootingPlayground
from src.models.SportKind import SportKind
from src.models.SportSeason import SportSeason


def main():
    print("\tSport Buildings\n")

    manager = SportBuildingsManager(create_sport_buildings_list())
    selected_buildings = manager.find_by_viewers_number(100, 1000)
    manager.sort_by_sport_kind(selected_buildings)
    manager.print_sport_buildings_info(selected_buildings)


def create_sport_buildings_list():
    sport_buildings = list()

    sport_buildings.append(AquaticsHall("Aqua Hall", "Red st, 117", 1994, SportSeason.ALL_SEASONS,
                                        600, SportKind.AQUATICS, 8, 20))
    sport_buildings.append(AthleticsPlayground("Athletics playground", "Baker st, 88", 2003,
                                               SportSeason.SUMMER, 800, SportKind.ATHLETICS, 3000, 10))
    sport_buildings.append(ChessHall("Chess Hall", "Silent st, 204", 1990, SportSeason.ALL_SEASONS,
                                     90, SportKind.CHESS, 10))
    sport_buildings.append(FootballField("Football field", "Liberty st, 39", 1968, SportSeason.SUMMER,
                                         1100, SportKind.FOOTBALL, 30, 70))
    sport_buildings.append(ShootingPlayground("Winter Archery", "Silver st, 42", 1999, SportSeason.WINTER,
                                              500, SportKind.ARCHERY, 30, 15, 250))

    return sport_buildings
