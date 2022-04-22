from logging import raiseExceptions
import re

from person import Person






class Employee(Person):
    id=0
    def __init__(self, full_name, money, sleepmood, healthRate, email, workmood, salary, is_manager):
        super().__init__(full_name, money, sleepmood, healthRate)

        ptrn = r'^[a-zA-z0-9]+@[a-z]+\.[a-z]{2,4}$'
        result = re.match(ptrn, email)

        if salary < 1000:
            raise ValueError("salary must be greater than 999 !")
        elif 0 > healthRate < 99:
            raise ValueError("Sorry, healthRate must be between 0 and 100")
        elif not result:
            raise ValueError("Sorry, email wrong ptrn!!")
        else:
            self.setID()
            self.email = email
            self.workmood = workmood
            self.salary = salary
            self.is_manager = is_manager

    @classmethod
    def setID(cals):
        cals.id+=1
    @staticmethod
    def sendEmail(to, subject, body, reciver):
        ptrn = r'^[a-zA-z0-9]+@[a-z]+\.[a-z]{2,4}$'
        result = re.match(ptrn, to)
        if result:
            MyEmail = open("Email.txt", "a")
            MyEmail.write("to: " + to + "\n")
            MyEmail.write("Subject: " + subject + "\n")
            MyEmail.write("Body: " + body + "\n")
            MyEmail.write("Reciver: " + reciver + "\n")
            MyEmail.write("================================= " + "\n")
            MyEmail.close()
        else:
            raiseExceptions("Sorry invalid email")

    def work(self, hours):
        if hours == 8:
            self.sleepmood = "happy"
        elif hours < 8:
            self.sleepmood = "Lazy"
        else:
            self.sleepmood = "tired"


marwa = Employee("marwa" , 50000 , "tired", 50 , "marwa@gmail.com" , "happy" , 20000 , 0)


