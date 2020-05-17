class Song:

    def __init__(self, name="noname", duration_in_min=0, singer="uncknown", year=2000):
        self.duration_in_min = duration_in_min
        self.name = name
        self.year = year
        self.singer = singer

    def __str__(self):
        return "Song : name = {}, duration_in_min = {}min, singer = {}, year = {} ".format(self.name,
                                                                                           self.duration_in_min,
                                                                                           self.singer, self.year)
