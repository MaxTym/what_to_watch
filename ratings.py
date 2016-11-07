import csv
import math

class Rating:


    def __init__(self, **kwargs):
        self.user_id = int(kwargs['user_id'])
        self.movie_id = int(kwargs['movie_id'])
        self.rating = int(kwargs['rating'])
        self.timestamp = kwargs['timestamp']


    def __repr__(self):
        return "{} {} {}  {} ".format(self.user_id, self.movie_id, self.rating, self.timestamp)


    def read_ratings_for_movie():
        ratings_for_movie = {}
        with open ('u.data', encoding="latin_1") as f:
            reader = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating',
                                        'timestamp'], delimiter='\t')
            for row in reader:
                ratings_for_movie.setdefault(row['movie_id'], []).append([row['rating']])
            return ratings_for_movie



    def read_user_movies():
        with open ('u.data', encoding="latin_1") as f:
            data = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating',
                                        'timestamp'], delimiter='\t')
            dict_of_user_movies = {}
            for row in data:
                dict_of_user_movies.setdefault(row['user_id'], []).append([row['movie_id']])
            return dict_of_user_movies


    def get_all_movies_for_user(user_id):
        users_list = Rating.read_user_movies()
        l = users_list[user_id]
        return l


    def get_all_ratings_for_movie(movie_id):
        movies_list = Rating.read_ratings_for_movie()
        l = movies_list[movie_id]
        print(l)


    def get_avg_rating_for_movie(movie_id):
        movies_list = Rating.read_ratings_for_movie()
        l = movies_list[movie_id]
        r = []
        total = 0
        for row in l:
            for i in row:
                r.append(i)
        r = [int(i) for i in r]
        avg = (sum(r)/len(r))
        avg = round(avg,2)
        top_list = []
        if avg >= 4.5:
            top_list.append(movie_id)
        return top_list
        #print("%.2f" % avg, "Movie: ", movie_id)


    def get_list_of_users():
        with open ('u.data', encoding="latin_1") as f:
            data = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating',
                                        'timestamp'], delimiter='\t')
            list_of_users = []
            for row in data:
                list_of_users.append(row['user_id'])
            return list_of_users

    def write_top_movies_to_file():
        movies_list = Rating.read_ratings_for_movie()
        top_movies = []
        count = 0
        for l in movies_list:
            count += 1
            print(count)
            h = Rating.get_avg_rating_for_movie(l)
            top_movies += h
            print(top_movies)
            with open('avg_ratings', 'w') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter='\n')
                wr.writerow(top_movies)

    def get_top_movies():
        movie_data = []
        with open ('avg_ratings', encoding="latin_1", ) as f:
            reader = csv.reader(f)
            for row in reader:
                movie_data.append(row)
            return movie_data
