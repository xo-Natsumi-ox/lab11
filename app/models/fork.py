from app.models.song import Song


class Fork(Song):
    def __init__(self, name="noname", duration_in_min=0, singer="uncknown", year=2000, is_fork="yes"):
        super().__init__(name=name, duration_in_min=duration_in_min, singer=singer, year=year)
        self.is_fork = is_fork

    def __str__(self):
        return super().__str__() + ", is fork? = {}".format(self.is_fork)
