class Employee:
    def __init__(self,EmpName,EmpId,Age,JoiningDate):
        self.EmpName = EmpName
        self.EmpId = EmpId
        self.Age = Age
        self.JoiningDate = JoiningDate
        
    
    def getEmpDetails(self):
        print("Employee name: ", self.EmpName)
        print("Employee Id: ", self.EmpId)
        print("Employee Age: ", self.Age)
        print("Employee Joining Date: ", self.JoiningDate)
        
class Admin(Employee): #inherits the properties of Employee class

    def __init__(self,EmpName,EmpId,Age,JoiningDate,IsAdmin):
        super().__init__(EmpName,EmpId,Age,JoiningDate)
        self.IsAdmin = IsAdmin
        
    def acessPermission(self):
        print("Is this is a Admin user ", self.IsAdmin)
        print("All permissions are granted")
Emp  = Employee("Selva",123,25,"may",True)    
Emp1 = Admin("susi",111,25,"may30",True)  #Admin employee is created
Emp1.getEmpDetails()     #accessing the functions from employee class
Emp1.acessPermission() 