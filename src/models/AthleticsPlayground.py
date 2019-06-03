from src.models.SportBuilding import SportBuilding


class AthleticsPlayground(SportBuilding):

    def __init__(self, name="", location="", construction_year=0, sport_season=None,
                 viewers_number=0, sport_kind=None, average_track_distance=0, tracks_number=0):
        super().__init__(name, location, construction_year, sport_season, viewers_number, sport_kind)
        self.average_track_distance = average_track_distance
        self.tracks_number = tracks_number

    def __str__(self):
        return "AthleticsPlayground" + super().__str__() \
               + ", average_track_distance=" + str(self.average_track_distance) \
               + ", tracks_number=" + str(self.tracks_number) + "}"
