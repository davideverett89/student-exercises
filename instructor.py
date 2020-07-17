import random

class Instructor:

    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.specialty = specialty
    
    def give_assignment_to_student(self, student, list_of_assignments):
        random_assignment = random.choice(list_of_assignments)
        student.setAssignment(random_assignment)

    def __str__(self):
        return f'{self.first_name} {self.last_name} teaches in {self.cohort}.  His/her slack handle is {self.slack_handle}.'
