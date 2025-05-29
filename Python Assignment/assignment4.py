class department:
    def __init__(self, ID, name,location, head_of_department):
        self.ID = ID    
        self.name = name
        self.location = location
        self.head_of_department = head_of_department
    def display_department_info(self):
        print("\nDepartment information : ")
        print("------------------------------------------")
        print(f"Department ID: {self.ID}")
        print(f"Department Name: {self.name}")
        print(f"Department Location: {self.location}")
        print(f"Head of the Department: {self.head_of_department}")
no_of_departments = int(input("Enter the number of departments: "))
departments = {}
for i in range(no_of_departments):
    ID = input(f"Enter the ID for department {i+1}: ")
    name = input(f"Enter the name for department {i+1}: ")
    location = input(f"Enter the location for department {i+1}: ")
    head_of_department = input(f"Enter the head of department for department {i+1}: ") 
    department_instance = department(ID, name, location, head_of_department)
    departments[ID] = department_instance
for dept in departments.values():
    print("\nDepartment Information:")
    dept.display_department_info()
#---------------------------------------------------------------------------------------------------------------------------------

