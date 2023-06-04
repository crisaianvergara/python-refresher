class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Aian", (100, 100, 93, 78, 90))
student_two = Student("Bob", (90, 90, 93, 78, 90))

print(student_one.name)
print(student_one.grades)
print(student_one.get_average())

print(student_two.name)
print(student_two.grades)
print(student_two.get_average())
