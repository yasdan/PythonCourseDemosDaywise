class employee:
    def setdata(self,name,adress,salary):
        self.name = name
        self.adress= adress
        self.__salary = salary  # private variable

    def printEmployeeDetails(self):
        print(f'name is {self.name},residing at {self.adress}'
              f' getting a salary of {self.__salary}  ')

emp= employee()
emp.setdata("Abdul","Vijayawada",234566)
emp.printEmployeeDetails()
emp.name="Salman"
emp.adress="Hyderabad"
emp.printEmployeeDetails()
