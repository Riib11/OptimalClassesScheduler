import students
import classes
import random
random.seed()

class School:
    def __init__(self, total_students, classes_per_student, total_classes, students_per_class, class_values_func, select_mode):
        self.class_values = class_values_func
        self.select_mode = select_mode
        self.sm = students.StudentManager(total_students, classes_per_student, total_classes)
        self.cm = classes.ClassManager(total_classes, students_per_class)

    # what would be the optimal score? (each student gets their top classes_per_student classes)
    def optimal(self):
        # the optimal score of a given student would be
        return sum([self.class_values(x) for x in range(self.sm.classes_per_student)])


    def add_student_to_class(self, student_index, class_index):
        # add student if the student can be accepted
        if self.cm.classes[class_index].can_accept_student(self.sm.students[student_index]):
            # print("added student",student_index,"to class",class_index)
            self.sm.students[student_index].add_class(self.cm.classes[class_index])
            self.cm.classes[class_index].add_student(self.sm.students[student_index])
            return True
        return False

    def student_pick(self, snum,students_left_indecies):
        if self.sm.students[snum].is_full():
                students_left_indecies.remove(snum)
                return

        for cnum in self.sm.students[snum].preferences:
            # keep trying until get a class that is open
            # has to work eventually!
            if self.add_student_to_class(snum, cnum):
                # remove from pool the indecies of students that are done
                if self.sm.students[snum].is_full():
                    students_left_indecies.remove(snum)
                # since successfully added class, go on to next student now
                break

    def select_student_regular(self, students_left_indecies):
        return random.choice(students_left_indecies)

    def select_student(self, students_left_indecies):
        if self.select_mode == "regular":
            return self.select_student_regular(students_left_indecies)
        elif self.select_mode == "normal":
            return self.select_student_normal(students_left_indecies)
        else:
            print("invalid mode")

    # distribute classes to students by choosing random students and letting them choose their class,
    # one at a time, until everyone has all their classes
    def random_distribute(self):
        # keep choosing until all students have all their classes
        students_left_indecies = [x for x in range(len(self.sm.students))]

        while not len(students_left_indecies) == 0:
            snum = self.select_student(students_left_indecies)
            self.student_pick(snum,students_left_indecies)

    # everyone picks a class, one at a time, x times. then random distribute
    def first_x_picks(self, x):
        # each student gets to pick their x fav classes, in a random order,
        # but each student gets at least one class before anyone gets more
        for i in range(x):
            students_left_indecies = [x for x in range(len(self.sm.students))]

            while not len(students_left_indecies) == 0:
                snum = self.select_student(students_left_indecies)
                self.student_pick(snum,students_left_indecies)
                # only get 1 pick at a time
                students_left_indecies.remove(snum)

        # then, do regular random distribute
        self.random_distribute()

    # everyone gets x classes. then, random pick
    def take_x_picks(self, x):
        # everyone races until everyone has x classes
        students_left_indecies = [x for x in range(len(self.sm.students))]

        while not len(students_left_indecies) == 0:
            snum = self.select_student(students_left_indecies)
            self.student_pick(snum,students_left_indecies)

            # remove if has the max classes for the take
            if len(self.sm.students[snum].classes) == x:
                students_left_indecies.remove(snum)
            

        # then, do regular random distribute
        self.random_distribute()

    # figure out how well the students were distributed among the classes
    def calculate_errors_data(self):
        op = self.optimal()

        # a students success is how high the sum of the rankings of classes not in their schedule is,
        # the idea being to get the highest priority classes with low rankings in their schedule
        errors = []
        for s in self.sm.students:
            # the classes that a student got
            class_nums = [s.classes[x].class_num for x in range(len(s.classes))]
        
            # sum up the preferences of the classes that the student got
            # index of preference is the 'rank of preference' of it, the value is the class that is prefered
            ranks_gotten = []
            for i in range(len(s.preferences)):
                if s.preferences[i] in class_nums:
                    ranks_gotten.append(i)
                if len(ranks_gotten) == self.sm.classes_per_student:
                    break

            error = sum(self.class_values(x) for x in ranks_gotten)
            errors.append(error - op)

        return errors

    def sample_students(self, sample_size):
        for i in range(sample_size):
            s = self.sm.students[i]
            print("S" + str(i),":")
            print("  prefers:",s.preferences[0:15])
            print("  classes", [c.class_num for c in s.classes])