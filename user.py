import csv


class User:


    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.occupation = kwargs['occupation']
        self.zip_code = kwargs['zip_code']


    def __repr__(self):
        return "{} {} {} {} {}".format(self.user_id, self.age, self.gender,
                                        self.occupation, self.zip_code)


    def read_user_info():
        user_info = []
        with open ('u.user', encoding="latin_1") as f:
            reader = csv.DictReader(f, fieldnames=['user_id', 'age', 'gender',
                                        'occupation', 'zip_code'], delimiter='|')
            for row in reader:
                user_info.append(row)
            return user_info
