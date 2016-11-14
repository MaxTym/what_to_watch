import csv


class Movie:
    def __init__(self, **kwargs):
        self.movie_id = int(kwargs["movie_id"])
        self.title = kwargs["title"]

    def __repr__(self):
        return "{} {}".format(self.movie_id, self.title)


class User:
    def __init__(self, **kwargs):
        self.user_id = int(kwargs["user_id"])
        self.age = kwargs["age"]
        self.gender = kwargs["gender"]
        self.occupation = kwargs["occupation"]

    def __repr__(self):
        return "{} {} {} {}".format(self.user_id, self.occupation, self.age, self.gender)

class Rating:
    def __init__(self, **kwargs):
        self.user_id = int(kwargs["user_id"])
        self.movie_id = int(kwargs["movie_id"])
        self.rating = float(kwargs["rating"])

    def __repr__(self):
        return "{} {} {}".format(self.user_id, self.movie_id, self.rating)
