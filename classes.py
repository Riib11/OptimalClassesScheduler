class ClassManager:
    def __init__(self, total_classes, students_per_class):
        self.total_classes = total_classes
        self.students_per_class = students_per_class

        # generate all the classes
        self.classes = []
        self.create_classes()

    def get_classes_count(self):
        return len(self.classes)

    def create_classes(self):
        for i in range(self.total_classes):
            self.classes.append(Class(i, self.students_per_class))


class Class:
    def __init__(self, class_num, students_per_class):
        self.class_num = class_num
        self.students_per_class = students_per_class
        self.students = []

    def is_full(self):
        return len(self.students) >= self.students_per_class

    def add_student(self, student):
        self.students.append(student)

    def can_accept_student(self, student):
        if self.is_full() or student in self.students:
            return False

        return True