class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()

    # Функция реализует студентам возможность выставлять оценки
    # лекторам за лекции
    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Функция подсчета средней оценки
    def average_grades(self):
        count_grades = 0
        for i in self.grades:
            count_grades += len(self.grades[i])
        self.average_grade = sum(map(sum, self.grades.values())) / count_grades

    # Перегрузка магического метод __str__
    def __str__(self):
        self.average_grades()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.average_grade}\n'
                f'Курсы в процессе обучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    # Функция реализует возможность сравнивать (через операторы сравнения)
    # между собой студентов по средней оценке за домашние задания.
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Неверное сравнение')
            return
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    # Перегрузка магического метод __str__
    def __str__(self):
        self.average_grades()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade}')

    # Функция реализует возможность сравнивать (через операторы сравнения)
    # между собой лекторов по средней оценке за лекции
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Неверное сравнение')
            return
        return self.average_grade < other.average_grade


class Reviewer(Mentor):
    # Функция реализует проверяющим возможность выставлять оценки
    # студентам за домашние задания
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Перегрузка магического метод __str__
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Студенты
some_student_1 = Student('Ruoy', 'Eman')
some_student_1.finished_courses += ['Введение в программирование']
some_student_1.courses_in_progress += ['Python']

some_student_2 = Student('Petr', 'Petrov')
some_student_2.finished_courses += ['Введение в программирование']
some_student_2.courses_in_progress += ['Git']

# Лекторы
some_lecturer_1 = Lecturer('Sergey','Sergeyev')
some_lecturer_1.courses_attached += ['Python']

some_lecturer_2 = Lecturer('Semyon','Sidorov')
some_lecturer_2.courses_attached += ['Git']

# Проверяющие
some_reviewer_1 = Reviewer('Some', 'Buddy')
some_reviewer_1.courses_attached += ['Python']

some_reviewer_2 = Reviewer('Ivan', 'Ivanov')
some_reviewer_2.courses_attached += ['Git']

# Студенты выставляют оценки лекорам за лекции
some_student_1.rate_hw(some_lecturer_1, 'Python', 8)
some_student_1.rate_hw(some_lecturer_2, 'Git', 9)
some_student_2.rate_hw(some_lecturer_1, 'Python', 10)
some_student_2.rate_hw(some_lecturer_2, 'Git', 5)

# Проверяющие выставляют оценки студентам за домашнее задание
some_reviewer_1.rate_hw(some_student_1, 'Python', 7)
some_reviewer_2.rate_hw(some_student_1, 'Git', 8)
some_reviewer_1.rate_hw(some_student_2, 'Python', 10)
some_reviewer_2.rate_hw(some_student_2, 'Git', 8)

# список студентов
lst_students = [some_student_1, some_student_2]

#список лекторов
lst_lecturers = [some_lecturer_1, some_lecturer_2]

print('-' * 20)
print('Reviewer (Проверяющие):')
print()
print(some_reviewer_1, some_reviewer_2, sep='\n')

print('-' * 20)
print('Lecturer (Лекторы):')
print()
print(some_lecturer_1,some_lecturer_2, sep='\n')

print('-' * 20)
print('Student (Студенты):')
print()
print(some_student_1, some_student_2, sep='\n')

print('-' * 20)
print('Сравнение по средней оценики студентов: '
      f'{some_student_1 < some_student_2}')
print('Сравнение по средней оценики лекторов: '
     f'{some_lecturer_1 < some_lecturer_2}')
print('-' * 20)

# функция для подсчета средней оценки за домашние задания по всем студентам
# в рамках конкретного курса (в качестве аргументов принимаем список
# студентов и название курса);
def average_scope_students(students, course_name):
    sum_ = 0
    counter = 0
    for student in students:
        if student.courses_in_progress == [course_name]:
            sum_ += student.average_grade
            counter += 1
    overall_average_score = sum_ / counter
    return ('Средняя оценка за домашние задания по всем студентам по курсу '
            f'{course_name}: {overall_average_score}')


# функция для подсчета средней оценки за лекции всех лекторов
# в рамках курса (в качестве аргумента принимаем список лекторов
# и название курса).
def average_scope_lecturers(lecturers, course_name):
    sum_ = 0
    counter = 0
    for lecturer in lecturers:
        if lecturer.courses_attached == [course_name]:
            sum_ += lecturer.average_grade
            counter += 1
    overall_average_score = sum_ / counter
    return ('Средняя оценка за лекции всех лекторов в рамках курса '
            f'{course_name}: {overall_average_score}')

print(average_scope_students(lst_students, "Python"))
print(average_scope_students(lst_students, "Git"))
print()
print(average_scope_lecturers(lst_lecturers, "Git"))
print(average_scope_lecturers(lst_lecturers, "Python"))
print('-' * 20)
