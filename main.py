import school
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

total_students = 100
classes_per_student = 4
total_classes = 50
students_per_class = 10
select_mode = "regular"

def class_values(rank):
    return rank**2

print()

means = []
stds = []

for i in tqdm(range(2000)):

    sch = school.School(total_students,
                        classes_per_student,
                        total_classes,
                        students_per_class,
                        class_values,
                        select_mode)
    sch.first_x_picks(3)
    
    data = sch.calculate_errors_data()

    # print("sample:")
    # sch.sm.students[0].classes_to_preferences()

    means.append(np.mean(data))
    stds.append(np.std(data))

print(np.mean(means),";",np.mean(stds))

# sch.sample_students(10)

print()

quit()