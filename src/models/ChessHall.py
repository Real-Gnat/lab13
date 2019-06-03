from src.models.SportBuilding import SportBuilding


class ChessHall(SportBuilding):

    def __init__(self, name="", location="", construction_year=0, sport_season=None,
                 viewers_number=0, sport_kind=None, tables_number=0):
        super().__init__(name, location, construction_year, sport_season, viewers_number, sport_kind)
        self.tables_number = tables_number

    def __str__(self):
        return "ChessHall" + super().__str__() \
               + ", tables_number=" + str(self.tables_number) + "}"
