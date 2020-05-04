from app.models.genre import Genre
from app.models.popular import Popular


class InternetStoreManager:
    def __init__(self, popular_list=[]):
        self.popular_list = popular_list

    def find_popular_song_by_duration_in_min(self, duration_in_min):
        """
        find_popular_song_by_duration_in_min
        >>> popular_list=InternetStoreManager([Popular("numb",3,"linkin park",2003, Genre.rock),Popular("Astronimia",6,"tony igy",2010, Genre.electro),Popular("fire man",4,"miyagi&andy panda",2018, Genre.rap)])
        >>> popular_list.find_popular_song_by_duration_in_min(3)
        Song : name = numb, duration_in_min = 3min, singer = linkin park, year = 2003 , genre = Genre.rock
        >>> popular_list.find_popular_song_by_duration_in_min(4)
        Song : name = fire man, duration_in_min = 4min, singer = miyagi&andy panda, year = 2018 , genre = Genre.rap
        >>> popular_list.find_popular_song_by_duration_in_min(6)
        Song : name = Astronimia, duration_in_min = 6min, singer = tony igy, year = 2010 , genre = Genre.electro
        """
        lists = list(filter(lambda song: song.duration_in_min == duration_in_min, self.popular_list))
        return print("".join(str(output_list) for output_list in lists))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
