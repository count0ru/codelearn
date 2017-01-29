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
        
        if scores_amount in range(0,39): 
            return("T")
        elif scores_amount in range(41,54): 
            return("D")
        elif scores_amount in range(55,69): 
            return("P")
        elif scores_amount in range(70,79): 
            return("A")
        elif scores_amount in range(80,89): 
            return("E")
        elif scores_amount in range(90,100): 
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
