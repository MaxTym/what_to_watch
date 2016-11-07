from movies import Movie
from user import User
from ratings import Rating
import csv
import os

def main():
    os.system('clear')
    user_input()


def get_top_movies_never_seen(user_id):
    l = Rating.get_top_movies()
    r = Rating.get_all_movies_for_user(user_id)
    l = cleaner(l)
    r = cleaner(r)
    for item in l:
        if item not in r:
            print(Movie.get_movie_name_by_id(item))


def get_top_15_movies():
    l = Rating.get_top_movies()
    l = cleaner(l)
    for item in l:
        print(Movie.get_movie_name_by_id(item))


def user_input():
    while True:
        user_id = input("Enter your user id please: ")
        if user_id in Rating.get_list_of_users():
            break
        else:
            print("Wrong user id")
            continue
    while True:
        choice = input("""To get a list of top movies you've never seen, press '1' \nTo get a list of top movies, press '2'\n""").lower()
        if choice == '1':
            get_top_movies_never_seen(user_id)
            break
        elif choice == '2':
            get_top_15_movies()
            break
        else:
            print("Choose 1 or 2")
            continue

def cleaner(item):
    clean_list = []
    for row in item:
        for i in row:
            clean_list.append(i)
    clean_list = [int(i) for i in clean_list]
    return clean_list


main()
