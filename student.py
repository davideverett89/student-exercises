class Student:

    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.assignments = set()

    def setAssignment(self, assignment):
        self.assignments.add(assignment)

    def __str__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}.  His/her slack handle is {self.slack_handle}.'