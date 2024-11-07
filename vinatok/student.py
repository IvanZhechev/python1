class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.first_name, self.last_name) == (other.first_name, other.last_name)
        return False

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.student_id))
