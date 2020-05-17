from app.models.genre import Genre
from app.models.popular import Popular


class InternetStoreManagerUtils:

    def __init__(self):
        return

    @staticmethod
    def sort_by_duration_in_min(sort_list):
        """
        sort_popular_song_by_duration_in_min

        >>> popular_list=([Popular("numb",3,"linkin park",2003, Genre.rock),Popular("Astronimia",6,"tony igy",2010, Genre.electro),Popular("fire man",4,"miyagi&andy panda",2018, Genre.rap)])
        >>> InternetStoreManagerUtils.sort_by_duration_in_min(popular_list)
        >>> print(popular_list[0])
        Song : name = numb, duration_in_min = 3min, singer = linkin park, year = 2003 , genre = Genre.rock
        >>> print(popular_list[1])
        Song : name = fire man, duration_in_min = 4min, singer = miyagi&andy panda, year = 2018 , genre = Genre.rap
        >>> print(popular_list[2])
        Song : name = Astronimia, duration_in_min = 6min, singer = tony igy, year = 2010 , genre = Genre.electro
        """
        sort_list.sort(key=lambda song: song.duration_in_min)

    @staticmethod
    def sort_by_year(sort_list):
        """
        sort_by_year

        >>> popular_list=([Popular("numb",3,"linkin park",2003, Genre.rock),Popular("Astronimia",6,"tony igy",2010, Genre.electro),Popular("fire man",4,"miyagi&andy panda",2018, Genre.rap)])
        >>> InternetStoreManagerUtils.sort_by_year(popular_list)
        >>> print(popular_list[0])
        Song : name = numb, duration_in_min = 3min, singer = linkin park, year = 2003 , genre = Genre.rock
        >>> print(popular_list[1])
        Song : name = Astronimia, duration_in_min = 6min, singer = tony igy, year = 2010 , genre = Genre.electro
        >>> print(popular_list[2])
        Song : name = fire man, duration_in_min = 4min, singer = miyagi&andy panda, year = 2018 , genre = Genre.rap
        """
        sort_list.sort(key=lambda song: song.year)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
