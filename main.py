class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def __str__(self):
        return f"{self.street}, {self.city} {self.postal_code}"


class Person:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Professor(Person):
    def __init__(self, name, email, address, staff_id):
        super().__init__(name, email, address)
        self.staff_id = staff_id


class Course:
    def __init__(self, code, title, professor):
        self.code = code
        self.title = title
        self.professor = professor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)


class Student(Person):
    def __init__(self, name, email, address, student_id):
        super().__init__(name, email, address)
        self.student_id = student_id
        self.grades = {}  # {Course: grade}

    def enroll(self, course):
        course.add_student(self)
        self.grades[course] = None

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def get_average(self):
        valid_grades = [g for g in self.grades.values() if g is not None]
        return sum(valid_grades) / len(valid_grades) if valid_grades else 0.0


# --- Quick Test ---
if __name__ == "__main__":
    addr = Address("42 Oak St", "Boston", "02116")
    prof = Professor("Dr. Smith", "smith@uni.edu", addr, "P101")
    student = Student("Jane Doe", "jane@uni.edu", addr, "S001")

    cs101 = Course("CS101", "Intro to Python", prof)
    cs102 = Course("CS102", "OOP Basics", prof)

    student.enroll(cs101)
    student.enroll(cs102)
    student.set_grade(cs101, 88)
    student.set_grade(cs102, 94)

    print(f"Student: {student.name} ({student.student_id})")
    print(f"Address: {student.address}")
    print(f"Average Grade: {student.get_average():.1f}")
