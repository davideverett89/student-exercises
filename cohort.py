class Cohort:

    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def setStudent(self, student):
        self.students.append(student)
    
    def setInstructor(self, instructor):
        self.instructors.append(instructor)

    def __str__(self):
        return f'This is cohort {self.name}'