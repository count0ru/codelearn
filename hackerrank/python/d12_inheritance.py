class Student(Person):
    
    def __init__(self, fname, lname, id, score):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.score = score


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
