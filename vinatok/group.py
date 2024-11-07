from student import Student

class GroupLimitError(Exception):
    """Виняток для перевищення ліміту студентів у групі."""
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupLimitError()
        self.students.add(student)

    def delete_student(self, last_name):
        self.students = {s for s in self.students if s.last_name != last_name}

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return f"Group {self.name}: " + ", ".join(str(s) for s in self.students)
