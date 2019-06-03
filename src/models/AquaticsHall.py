from src.models.SportBuilding import SportBuilding


class AquaticsHall(SportBuilding):

    def __init__(self, name="", location="", construction_year=0, sport_season=None,
                 viewers_number=0, sport_kind=None, pools_number=0, average_pool_volume=0):
        super().__init__(name, location, construction_year, sport_season, viewers_number, sport_kind)
        self.pools_number = pools_number
        self.average_pool_volume = average_pool_volume

    def __str__(self):
        return "AquaticsHall" + super().__str__() \
               + ", pools_number=" + str(self.pools_number) \
               + ", average_pool_volume=" + str(self.average_pool_volume) + "}"
