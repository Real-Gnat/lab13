from src.models.SportBuilding import SportBuilding


class FootballField(SportBuilding):

    def __init__(self, name="", location="", construction_year=0, sport_season=None,
                 viewers_number=0, sport_kind=None, field_width=0, field_length=0):
        super().__init__(name, location, construction_year, sport_season, viewers_number, sport_kind)
        self.field_width = field_width
        self.field_length = field_length

    def __str__(self):
        return "FootballField" + super().__str__() \
               + ", field_width=" + str(self.field_width) \
               + ", field_length=" + str(self.field_length) + "}"
