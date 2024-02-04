from statistics import mean


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_sc(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def avg_grade(self):
        new_p = []
        for k, v in self.grades.items():
            new_p += v
            new_z: float = sum(new_p) / len(new_p)
            return new_z

    def __str__(self):
        courses_in_progress_string = ", ".join(self.courses_in_progress)
        finished_courses_string = ", ".join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашнее задание: {self.avg_grade()}\n"
            f"Курсы в процессе обучени: {courses_in_progress_string}\n"
            f"Завершенные курсы: {finished_courses_string}"
        )

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}\n"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        new_p = []
        for k, v in self.grades.items():
            new_p += v
            new_z: float = sum(new_p) / len(new_p)
            return new_z

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.avg_grade()}\n"
        )

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()


lecturer_1 = Lecturer("Ivan", "Pupsov")
lecturer_1.courses_attached += ["Python"]

lecturer_2 = Lecturer("Moko", "Poko")
lecturer_2.courses_attached += ["Python"]

rewiewer_1 = Reviewer("Olga", "Bull")
rewiewer_1.courses_attached += ["Python"]
rewiewer_1.courses_attached += ["C++"]

rewiewer_2 = Reviewer("Alina", "Bull")
rewiewer_2.courses_attached += ["Python"]
rewiewer_2.courses_attached += ["C++"]

student_1 = Student("Katya", "Smirnova")
student_1.courses_in_progress += ["Python"]
student_1.finished_courses += ["C#"]

student_2 = Student("Oleg", "Olegovich")
student_2.courses_in_progress += ["Python"]
student_2.finished_courses += ["C#"]

rewiewer_1.rate_hw(student_1, "Python", 3)
rewiewer_1.rate_hw(student_1, "Python", 3)
rewiewer_1.rate_hw(student_1, "Python", 6)

rewiewer_2.rate_hw(student_2, "Python", 2)
rewiewer_2.rate_hw(student_2, "Python", 4)
rewiewer_2.rate_hw(student_2, "Python", 6)

student_1.rate_sc(lecturer_1, "Python", 8)
student_1.rate_sc(lecturer_1, "Python", 9)
student_1.rate_sc(lecturer_1, "Python", 10)

student_1.rate_sc(lecturer_2, "Python", 8)
student_1.rate_sc(lecturer_2, "Python", 9)
student_1.rate_sc(lecturer_2, "Python", 10)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def student_rating(course):
    avg_grade_student = []
    for student in student_list:
        for course1, grades in student.grades.items():
            if course == course1:
                avg_grade_student.extend(grades)
                new_z: float = sum(avg_grade_student) / len(avg_grade_student)
                return f"{new_z}"
            else:
                return


def lecturer_rating(course):
    avg_grade_lecturer = []
    for lecturer in lecturer_list:
        for course1, grades in lecturer.grades.items():
            if course == course1:
                avg_grade_lecturer.extend(grades)
                new_z: float = sum(avg_grade_lecturer) / len(avg_grade_lecturer)
                return f"{new_z}"
            else:
                return


print(lecturer_1, rewiewer_1, student_1, "\n")  ## проверка на __str__
print()
print(
    student_1 < student_2, student_1 > student_2, lecturer_2 == lecturer_1, sep="\n"
)  ## проверка на методы сравнения
print()
print(f"Средняя оценка всех студентов курса 'Python' - {student_rating('Python')}")
print()
print(f"Средняя оценка всех лекторов курса 'Python' - {lecturer_rating('Python')}")
