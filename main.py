

class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}


    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]


    def average_grade(self):
        total_grade = 0
        total_subject = 0
        for grade in self.grades.values():
            total_subject += len(grade)
            total_grade += sum(grade)
        if grade == 0:
            return 0
        else:
            return total_grade / total_subject


    def display_details(self):
        return f"Student ID: {self.student_id}. Name: {self.name}, {self.grades}, Average Grades: {self.average_grade()}"

class StudentManagementSystem():

    def add_student(self):
        pass

    def show_student_details(self):
        pass

    def show_student_avarage_grade(self):
        pass



nika = Student("001", "Nika")
nika.add_grade("Math", 30)
nika.add_grade("Python", 10)
print(nika.display_details())



