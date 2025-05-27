class Student(object):
    "name"
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def __dir__(self):
        return 'dir'
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)
