from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

# Exercises

product_cards = Exercise('Product Cards', 'CSS')
sorting_hat = Exercise('Sorting Hat', 'JavaScript')
tamagotchi = Exercise('Tamagotchi', 'Sass')
pet_adoption = Exercise('Pet Adoption', 'JavaScript')
mushroom_picker = Exercise('Mushroom Picker', 'JavaScript')
sports_roster = Exercise('Sports Roster', 'JavaScript')
kandy_korner = Exercise('Kandy Korner', 'JavaScript')
stocks_report = Exercise('Stocks Report', 'Python')
cash_to_coins = Exercise('Cash To Coins', 'Python')
coins_to_cash = Exercise('Coins To Cash', 'Python')

exercises = [product_cards, sorting_hat, tamagotchi, kandy_korner, stocks_report, cash_to_coins, coins_to_cash, pet_adoption, mushroom_picker, sports_roster]

# Cohorts

evening_cohort_10 = Cohort('E10')
evening_cohort_11 = Cohort('E11')
day_cohort_40 = Cohort('C40')

cohorts = [evening_cohort_10, evening_cohort_11, day_cohort_40]

# Students

sarah = Student('Sarah', 'Holder', 'Sarah Holder', 'C40')
davis = Student('Davis', 'Lindell', 'Davis Lindell', 'C40')
michele = Student('Michele', 'Rawlins', 'MICHELE RAWLINS', 'E11')
joey = Student('Joey', 'Petrone', 'Joey Petrone', 'E10')

students = [sarah, davis, michele, joey]

# Instructors

zoe = Instructor('Zoe', 'Ames', 'Zoe Ames', 'E11', 'Dry Humor')
joe = Instructor('Joe', 'Shepard', 'Joe Shepard', 'C40', 'Dad Jokes')
luke = Instructor('Luke', 'Lancaster', 'Luke Lancaster', 'E11', 'Coffee')
brian = Instructor('Brian', 'Nilsen', 'Brian Nilsen', 'C40', 'Dad Jokes')

instructors = [zoe, joe, luke, brian]

def assignment_handout():
    for instructor in instructors:
        for student in students:
            for x in range(0, 2):
                instructor.give_assignment_to_student(student, exercises)

# zoe.give_assignment_to_student(sarah, exercises)
# zoe.give_assignment_to_student(sarah, exercises)
# zoe.give_assignment_to_student(davis, exercises)
# zoe.give_assignment_to_student(davis, exercises)
# zoe.give_assignment_to_student(michele, exercises)
# zoe.give_assignment_to_student(michele, exercises)
# zoe.give_assignment_to_student(joey, exercises)
# zoe.give_assignment_to_student(joey, exercises)

# joe.give_assignment_to_student(sarah, exercises)
# joe.give_assignment_to_student(sarah, exercises)
# joe.give_assignment_to_student(davis, exercises)
# joe.give_assignment_to_student(davis, exercises)
# joe.give_assignment_to_student(michele, exercises)
# joe.give_assignment_to_student(michele, exercises)
# joe.give_assignment_to_student(joey, exercises)
# joe.give_assignment_to_student(joey, exercises)

# luke.give_assignment_to_student(sarah, exercises)
# luke.give_assignment_to_student(sarah, exercises)
# luke.give_assignment_to_student(davis, exercises)
# luke.give_assignment_to_student(davis, exercises)
# luke.give_assignment_to_student(michele, exercises)
# luke.give_assignment_to_student(michele, exercises)
# luke.give_assignment_to_student(joey, exercises)
# luke.give_assignment_to_student(joey, exercises)

# brian.give_assignment_to_student(sarah, exercises)
# brian.give_assignment_to_student(sarah, exercises)
# brian.give_assignment_to_student(davis, exercises)
# brian.give_assignment_to_student(davis, exercises)
# brian.give_assignment_to_student(michele, exercises)
# brian.give_assignment_to_student(michele, exercises)
# brian.give_assignment_to_student(joey, exercises)
# brian.give_assignment_to_student(joey, exercises)

def report_to_terminal():
    assignment_handout()
    for student in students:
        string = ''
        string += f'{student.first_name} is working on '
        assignment_list = list(student.assignments)
        for assignment in assignment_list:
            if assignment_list.index(assignment) == len(assignment_list) - 1:
                string += f' and {assignment.name}. '
            else:
                string += f' {assignment.name},'
        print(string)

report_to_terminal()
