

import MySQLdb
from employe import Employee




class Office:
    db = MySQLdb.connect("127.0.0.1", "root", "1234", "Office")
    cursor = db.cursor()

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
    
    def get_all_employees():
        Office.cursor.execute("select * from employees")
        data = Office.cursor.fetchall()
        for emp in data :
            print(emp[0])
            print(emp[1])
            print("############################")

    
    def get_employee(empId):
        Office.cursor.execute(f"select * from employees where id ={empId}")
        data = Office.cursor.fetchone()
        print(data)


    
    def Hire(Employee):

        Office.cursor.execute(f'insert into employees values("{Employee.id}","{Employee.full_name}" , "{Employee.email}" , "{Employee.is_manager}")')
        Office.db.commit()
        print("done")

    
    def Fire(empId):
        Office.cursor.execute(f'delete from employees where id = {empId}')
        Office.db.commit()
        print("delete done")
