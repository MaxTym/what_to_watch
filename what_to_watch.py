import csv
import math
from movies import *
movie_filename = "u.item"
rating_filename = "u.data"
user_filename = "u.user"


def load_movies(movie_filename):
    movie_dict = {}
    with open(movie_filename, encoding="latin-1") as f:
        headers = ["movie_id", "title"]
        reader = csv.DictReader(f, fieldnames=headers, delimiter="|")
        for row in reader:
            del row[None]
            m = Movie(**row)
            movie_dict[m.movie_id] = m
    return movie_dict



def load_users(user_filename):
    user_dict = {}
    with open(user_filename, encoding="latin-1") as f:
        headers = ["user_id", "age", "gender", "occupation"]
        reader = csv.DictReader(f, fieldnames=headers, delimiter="|")
        for row in reader:
            del row[None]
            u = User(**row)
            user_dict[u.user_id] = u
    return user_dict


def load_ratings(rating_filename):
    ratings_by_movie_id = {}
    ratings_by_user_id = {}
    with open(rating_filename, encoding="latin-1") as f:
        headers = ["user_id", "movie_id", "rating"]
        reader = csv.DictReader(f, fieldnames=headers, delimiter="\t")
        for row in reader:
            del row[None]
            r = Rating(**row)
            ratings_by_movie_id.setdefault(r.movie_id, []).append(r)
            ratings_by_user_id.setdefault(r.user_id, []).append(r)
    return ratings_by_movie_id, ratings_by_user_id


md = load_movies(movie_filename)
ud = load_users(user_filename)
rdbm, rdbu = load_ratings(rating_filename)


def avg_rating_by_movie_id(movie_id):
    list_of_ratings = rdbm[movie_id]
    avg = sum([r.rating for r in list_of_ratings])/len(list_of_ratings)
    return avg


def top_x_movies(x, min_ratings=5):
    avg_ratings = {}
    for movie in md.values():
        if len(rdbm[movie.movie_id]) < min_ratings: continue
        avg = avg_rating_by_movie_id(movie.movie_id)
        avg_ratings[movie.title] = avg
    count = 0
    for title, avg_rating in sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True):
        if count >= x:
            return
        count += 1
        print(count, title, avg_rating)


def main():
    print("Welcome to movie database")
    while True:
        get_top_movies = input("\n'1' -- top 10 movies\n'2' -- top 50\n'3' -- top 100\n'4' -- quit\n")
        if get_top_movies == '1':
            top_x_movies(10, 5)
        elif get_top_movies == '2':
            top_x_movies(50, 5)
        elif get_top_movies == '3':
            top_x_movies(100, 5)
        elif get_top_movies == '4':
            exit()
        else:
            print("try again")



if __name__ == "__main__":
    main()
