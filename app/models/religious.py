from app.models.song import Song


class Religious(Song):
    def __init__(self, name="noname", duration_in_min=0, singer="uncknown", year=2000, genre="uncknown"):
        super().__init__(name=name, duration_in_min=duration_in_min, singer=singer, year=year)
        self.genre = genre

    def __str__(self):
        return super().__str__() + ", genre = {}".format(self.genre)
