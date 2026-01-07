class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
    
class Employee(person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        super().display()
        print("Employee Id: ",self.emp_id)
        print("Salary: ",self.salary)

emp=Employee("Karma",19,"BI 250263",112500)
emp.display()