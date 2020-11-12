course_modul = {
	    'max_mark_for_individual_project': 40,
	    'max_mark_for_one_lab': 10,
	    'amount_of_labs': 6,
	    'mark_for_auto_exam': 92
	}
class Student():
    def __init__(self, student_name, course_modul):
        self.student_name = student_name
        self.course_modul = course_modul


        self.lab_tries = 0
        self.last_lab_try_mark =  0

        self.lab_1_tries = 0
        self.lab_1_mark = 0

        self.lab_2_tries = 0
        self.lab_2_mark = 0

        self.lab_3_tries = 0
        self.lab_3_mark = 0

        self.lab_4_tries = 0
        self.lab_4_mark = 0

        self.lab_5_tries = 0
        self.lab_5_mark = 0

        self.lab_6_tries = 0
        self.lab_6_mark = 0

        self.ind_progect_tries = 0
        self.ind_progect_mark = 0

        self.total_course_mark = 0
 
    def marks_for_lab(self):
        self.lab_1_tries = input("Amount of lab 1 tries: ")
        self.lab_1_mark = input("Mark for lab 1: ")
        self.total_course_mark += int(self.lab_1_mark)

        self.lab_2_tries = input("Amount of lab 2 tries: ")
        self.lab_2_mark = input("Mark for lab 2: ")
        self.total_course_mark += int(self.lab_2_mark)

        self.lab_3_tries = input("Amount of lab 3 tries: ")
        self.lab_3_mark = input("Mark for lab 3: ")
        self.total_course_mark += int(self.lab_3_mark)

        self.lab_4_tries = input("Amount of lab 4 tries: ")
        self.lab_4_mark = input("Mark for lab 4: ")
        self.total_course_mark += int(self.lab_4_mark)

        self.lab_5_tries = input("Amount of lab 5 tries: ")
        self.lab_5_mark = input("Mark for lab 5: ")
        self.total_course_mark += int(self.lab_5_mark)

        self.lab_6_tries = input("Amount of lab 6 tries: ")
        self.lab_6_mark = input("Mark for lab 6: ")
        self.total_course_mark += int(self.lab_6_mark)

    def mark_for_individual_project(self):
        self.individual_project_tries = input("Amount of individual project tries: ")
        self.individual_project_mark = input("Mark for individual project: ")
        self.total_course_mark += int(self.individual_project_mark)


    def report(self):
        is_exam_auto = False
        if self.total_course_mark >= self.course_modul['mark_for_auto_exam']:
            is_exam_auto = True
        result_tuple = (self.total_course_mark, is_exam_auto)
        print(f'Total course mark: {result_tuple[0]}\nAuto exam: {result_tuple[1]}')

a = input("ENTER THE STUDENT'S NAME: ")
print("")
student = Student (a, course_modul)
student.marks_for_lab()
student.mark_for_individual_project()
student.report()
