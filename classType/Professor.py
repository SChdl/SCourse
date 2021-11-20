class Professor:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def __str__(self):
        s = 'Professor: ' + self.name + ', Rating: ' + str(self.rating)
        return s