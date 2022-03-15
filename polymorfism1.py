class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 50

    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)

class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 55

    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)

    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()

employee = (Employee)()
employee.setnumberofworkinghours()
print("number of working hours:",end = ' ')
employee.displaythenumberofworkinghours()

trainee = (Trainee)()
trainee.setnumberofworkinghours()
print("number of working hours:",end = ' ')
trainee.displaythenumberofworkinghours()

trainee.resetnumberofworkinghours()
print("reset value:",end = ' ')
trainee.displaythenumberofworkinghours()




