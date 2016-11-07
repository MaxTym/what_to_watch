import csv


class Movie:


    def __init__(self, **kwargs):
        self.movie_id = kwargs['movie_id']
        self.movie_title = kwargs['movie_title']
        self.release_date = kwargs['release_date']
        self.video_release_date = kwargs['video_release_date']
        self.imdb_url = kwargs['imdb_url']
        self.unknown = kwargs['unknown']
        self.action = kwargs['action']
        self.adventure = kwargs['adventure']
        self.animation = kwargs['animation']
        self.children = kwargs['children']
        self.comedy = kwargs['comedy']
        self.crime = kwargs['crime']
        self.documentary = kwargs['documentary']
        self.drama = kwargs['drama']
        self.fantasy = kwargs['fantasy']
        self.film_noir = kwargs['film_noir']
        self.horror = kwargs['horror']
        self.musical = kwargs['musical']
        self.mystery = kwargs['mystery']
        self.romance = kwargs['romance']
        self.sci_fi = kwargs['sci_fi']
        self.thriller = kwargs['thriller']
        self.war = kwargs['war']
        self.western = kwargs['western']


    def __repr__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}  {} {} {} {} {} {} ".format(self.movie_id, self.movie_title, self.release_date,
                                                            self.video_release_date, self.imdb_url, self.unknown,
                                                            self.action, self.adventure, self.animation, self.children,
                                                            self.comedy, self.crime, self.documentary, self.drama,
                                                            self.fantasy, self.film_noir, self.horror, self.musical,
                                                            self.mystery, self.romance, self.sci_fi, self.thriller,
                                                            self.war, self.western,)



    def read_movies():
        movie_data = []
        with open ('u.item', encoding="latin_1") as f:
            reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', 'release_date',
                                        'video_release_date', 'imdb_url', 'unknown', 'action',
                                        'adventure', 'animation', 'children', 'comedy',
                                        'crime', 'documentary', 'drama', 'fantasy', 'film_noir',
                                        'horror', 'musical', 'mystery', 'romance', 'sci_fi', 'thriller',
                                        'war', 'western'], delimiter='|')
            for row in reader:
                movie_data.append(row)
            return movie_data


    def get_movie_name_by_id(movie_id):
        movie_rows_list = Movie.read_movies()
        movie_row = movie_rows_list[movie_id - 1]
        movie_title = movie_row['movie_title']
        return movie_title
