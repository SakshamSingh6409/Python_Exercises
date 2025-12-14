class Student:
    Class_Year = 2025
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def st_details(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}, Class Year: {Student.Class_Year}"
    
# Example usage
st1 = Student("Alice", 20, "Computer Science")
st2 = Student("Bob", 22, "Mathematics")
st3 = Student("Charlie", 21, "Physics")
st4 = Student("Diana", 23, "Chemistry")
st5 = Student("Ethan", 24, "Biology")
st = [st1, st2, st3, st4, st5]

for student in st:
    print(student.st_details())