# collect the list of students
# for each of the student collect the list of subject offered
# for each of the of subject collect the corresponding score of each student
# calculate the sum and average of the score for each students
# arrange the average in descending order to determine the students position
# run the loop for the len of the student list.
junior_class = ("mathematics", "english", "basic science", "agricultural science")

class Broadsheet:
    def __init__(self):
        self.number_of_student = None
        self.students = None
        self.subjects = None
        self.test = None
        self.exam = None
        self.total = None

    def student_num(self):
        self.number_of_student = int(input("how many student are in class? "))
        return int(self.number_of_student)

    def student_name(self):
        number = self.number_of_student
        student_list = []
        for i in range(1, number + 1):
            names = input(f"student {i}: ")
            student_list.append(names)
        return student_list

    def subjects(self):
        subject = self.student_name()
        for i in subject:
            result = dict.fromkeys(i, junior_class)
            return result



test = Broadsheet()
print(test.student_num())
print(test.student_name())
print(test.subjects())