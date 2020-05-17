from app.models.song import Song


class Fork(Song):
    def __init__(self, name="noname", duration_in_min=0, singer="uncknown", year=2000, period="yes"):
        super().__init__(name=name, duration_in_min=duration_in_min, singer=singer, year=year)
        self.period = period

    def __str__(self):
        return super().__str__() + ", period = {}".format(self.period)
