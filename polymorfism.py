
class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40

    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)

class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45

    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()

employee =Employee()
employee.setnumberofworkinghours()
print("number of working hours of employee:",end = ' ')
employee.displaythenumberofworkinghours()

trainee =Trainee()
trainee.setnumberofworkinghours()
print("number of working hours of trainee:",end = ' ')
trainee.displaythenumberofworkinghours()

trainee.resetnumberofworkinghours()
print("reset value",end = ' ')
trainee.displaythenumberofworkinghours()