from src.models.SportBuilding import SportBuilding


class ShootingPlayground(SportBuilding):

    def __init__(self, name="", location="", construction_year=0, sport_season=None, viewers_number=0,
                 sport_kind=None, bows_number=0, targets_number=0, arrows_number=0):
        super().__init__(name, location, construction_year, sport_season, viewers_number, sport_kind)
        self.bows_number = bows_number
        self.targets_number = targets_number
        self.arrows_number = arrows_number

    def __str__(self):
        return "ShootingPlayground" + super().__str__() \
               + ", bows_number=" + str(self.bows_number) \
               + ", targets_number=" + str(self.targets_number) \
               + ", arrows_number=" + str(self.arrows_number) + "}"
