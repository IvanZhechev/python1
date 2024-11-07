from student import Student
from group import Group, GroupLimitError

# Створюємо групу
gr = Group('PD1')

# Додаємо 10 студентів
for i in range(1, 11):
    student = Student('Male', 20 + i, f'FirstName{i}', f'LastName{i}', f'ID{i}')
    gr.add_student(student)

print("Група після додавання 10 студентів:")
print(gr)

# Спробуємо додати 11-го студента і обробимо помилку
try:
    st_extra = Student('Female', 25, 'Extra', 'Student', 'ID11')
    gr.add_student(st_extra)
except GroupLimitError as e:
    print(e)  # Виведе: "У групі не може бути більше 10 студентів"

print("Фінальний стан групи:")
print(gr)
