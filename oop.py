from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_sc(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_attached
            and course in lecturer.courses_in_progress
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
            f"Имя:{self.name}\n"
            f"Фамилия:{self.surname}\n"
            f"Средняя оценка за домашнее задание:{self.avg_grade()}\n"
            f"Курсы в процессе обучени:{courses_in_progress_string}\n"
            f"Завершенные курсы:{finished_courses_string}"
        )

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() < other.avg_grade()


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
        return f"Имя:{self.name}\n" f"Фамилия:{self.surname}\n"


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
            f"Имя:{self.name}\n"
            f"Фамилия:{self.surname}\n"
            f"Средняя оценка за домашнее задание:{self.avg_grade()}\n"
        )

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() < other.avg_grade()

