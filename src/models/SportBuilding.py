from abc import ABC


class SportBuilding(ABC):

    def __init__(self, name="", location="", construction_year=0,
                 sport_season=None, viewers_number=0, sport_kind=None):
        self.name = name
        self.location = location
        self.construction_year = construction_year
        self.sport_season = sport_season
        self.viewers_number = viewers_number
        self.sport_kind = sport_kind

    def __str__(self):
        return "{" + "name='" + self.name + '\'' \
               + ", location='" + self.location + '\'' \
               + ", construction_year=" + str(self.construction_year) \
               + ", sport_season=" + str(self.sport_season) \
               + ", viewers_number=" + str(self.viewers_number) \
               + ", sport_kind=" + str(self.sport_kind)
