class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} login")

    def logout(self):
        print(f"{self.name} logout")


class Student(User):
    def submit_task(self):
        print(f"{self.name} task submitted")


class Mentor(User):
    def check_task(self):
        print(f"{self.name} task checked")

    def login(self):
        super(Mentor, self).login()
        print(f"{self.name} login as mentor")


student = Student('John', 'john@example.com')
mentor = Mentor("Smith", "smith@example.com")
student.login()
student.submit_task()
student.logout()
mentor.login()
mentor.check_task()
mentor.logout()