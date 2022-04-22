from employe import Employee
from office import Office




while exit != "q":
    check = input("Type 'add' to add new EMP and 'show' to sell all EMPs Data or user 'user' to see specific user or delete 'delete' to delete uder  : ").lower()
    if check == 'add':
        name = input("Name: ")
        email = input("Email: ")
        Type = input("Manager or Normal Employee? :").lower()
        if Type == "manager":
            isManager = 1
        else:
            isManager = 0
        try:    
            empX=Employee(name,5000,"Happy" , 50 , email , "tired" , 50000 , isManager)
            Office.Hire(empX)
        except:
            print("Invalid email please try again")
        
    elif check == "show":
        Office.get_all_employees()

    elif check == "user":
        empId = input("please inter the user id : ")
        Office.get_employee(empId)

    elif check == "delete":
        empId = input("please inter the user id : ")
        Office.Fire(empId)   
    
    exit= input("press “q” to quit the application and press anything to Continue: ").lower()

    





        