# ICP4


class Employee:

    employeeCount = 0

    def __init__(self, employeedt):
        self.emp_details = employeedt
        self.employeeCount = len(employeedt)
        self.display_employee_details()

    def display_employee_details(self):
        print("Total Number of Employees : ", self.employeeCount)
        employeeSalary = 0
        for count in range(len(self.emp_details)):
            if count <= len(self.emp_details):
                employeeSalary = employeeSalary + float(self.emp_details.get(count)[2])
                print("Employee %s Details :" % str(count+1))
                print("Employee Name : %s, Employee Family : %s, Employee Salary : %f, Employee Designation : %s "
                      % (str(self.emp_details.get(count)[0]), str(self.emp_details.get(count)[1]),
                         float(self.emp_details.get(count)[2]), str(self.emp_details.get(count)[3])))
        print("Employees Average Salary: %f " % (employeeSalary/self.employeeCount))


class FullTimeEmployee(Employee):

    employeedt = {0: ["bhavesh", "polareddy", float(2400.45), "engineer"], 1: ["venkata", "polareddy", float(2600.45), "senior engineer"]}
    employee = Employee(employeedt)


    def __init__(self, employeedt):
        Employee.__init__(self, employeedt)


moreData = "yes"
employeeInfo = {}
empId = 0
while moreData[0] == 'y':
    print("Enter Below Details to get some Info")
    empName = input("Please Enter Employee Name: ")
    empFamily = input("Please Enter Employee Family: ")
    empSalary = input("Please Enter Employee Salary: ")
    empDesignation = input("Please Enter Employee Designation: ")
    employeeInfo[empId] = [empName, empFamily, empSalary, empDesignation]
    empId += 1
    moreData = input("Do u have more numbers(yes or no)? ")

empFinal = Employee(employeeInfo)
