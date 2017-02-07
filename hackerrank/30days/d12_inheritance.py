class Person:
    
    def __init__(self, firstName, lastName, idNumber):
        
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    
    def printPerson(self):
        
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, score):
        
        Person.__init__(self, firstName, lastName, idNumber)
        self.score = score

    def calculate(self):
        
        scores_amount = sum(self.score)/len(self.score)
        
        if 0 < scores_amount < 40: 
            return("T")
        elif 40 <= scores_amount < 50: 
            return("D")
        elif 55 <= scores_amount < 70: 
            return("P")
        elif 70 <= scores_amount < 80: 
            return("A")
        elif 80 <= scores_amount < 90: 
            return("E")
        elif 90 <= scores_amount <= 100: 
            return("O")

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
