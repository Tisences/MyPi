class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        if gender == 'female':
            self.gender = 'female'
        elif gender == 'male':
            self.gender = 'male'
        else:
            pass
