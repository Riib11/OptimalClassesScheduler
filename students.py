import random
random.seed()

class StudentManager:
    def __init__(self, total_students, classes_per_student, total_classes):
        self.total_students = total_students
        self.classes_per_student = classes_per_student
        self.total_classes = total_classes

        self.running_num = 0

        # generate all the students
        self.students = []
        self.create_students()

    def create_student(self):
        s = Student(self.running_num, self.classes_per_student, self.total_classes)
        s.choose_preferences()
        self.students.append(s)

        self.running_num += 1

    def create_students(self):
        for i in range(self.total_students):
            self.create_student()


class Student:
    def __init__(self, student_num, classes_count, total_classes):
        self.student_num = student_num
        self.classes_count = classes_count
        self.total_classes = total_classes
        self.preferences = []
        self.classes = []
        self.choose_preferences

    def choose_preferences(self):
        self.preferences = [x for x in range(self.total_classes)]
        random.shuffle(self.preferences)

    def add_class(self, c):
        self.classes.append(c)

    def is_full(self):
        return len(self.classes) == self.classes_count

    def classes_to_preferences(self):
        print([c.class_num for c in self.classes])
        print(self.preferences)