class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, мене звуть {self.name}"


class Student(Person):
    def is_student(self):
        return True


student = Student("Іван")

print(student.greet())
print(student.is_student())
