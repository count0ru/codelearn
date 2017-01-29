class Person:
    
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    
    def __init_ (self, firstName, lastName, idNumbera, score):
        Person.__init__(self, firstName, lastName, idNumber)
        self.score = score.split(" "))


    def calculate(self):
        tests_amount = int(input().strip())
        tests_results = int(input().split(" "))
        scores_amount = sum(scores_amount)/len(scores_amount)
        print(("O")[scores_amount in range(90,100)]) 
        print(("E")[scores_amount in range(80,90)]) 
        print(("A")[scores_amount in range(70,80)]) 
        print(("P")[scores_amount in range(55,70)]) 
        print(("D")[scores_amount in range(40,55)]) 
        print(("T")[scores_amount in range(0,40)])


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
