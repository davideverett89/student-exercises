import sqlite3
from student import Student
from exercise import Exercise
from cohort import Cohort
from instructor import Instructor

class StudentExerciseReport:

    def __init__(self):
        self.db_path = "/Users/davideverett/workspace/python/StudentExercises/studentexercises.db"

    def assignments_with_students(self):

        print("""
        +--+--+--+--+--+--+--+--+--+--+

           ASSIGNMENTS WITH STUDENTS

        +--+--+--+--+--+--+--+--+--+--+
        """)

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercises.name, students.first_name, students.last_name
            FROM exercises
            JOIN student_exercises ON student_exercises.exercise_id = exercises.id
            JOIN students ON students.id = student_exercises.student_id;
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_name = row[0]
                student_name = f'{row[1]} {row[2]}'
                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(f'{exercise_name} is being worked on by:')
                for student in students:
                    print(f'\t*   {student}')

    def students_with_assignments(self):

        print("""
        +--+--+--+--+--+--+--+--+--+--+

           STUDENTS WITH ASSIGNMENTS

        +--+--+--+--+--+--+--+--+--+--+
        """)

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT students.first_name, students.last_name, exercises.name
            FROM students
            JOIN student_exercises
            ON students.id = student_exercises.student_id
            JOIN exercises
            ON exercises.id = student_exercises.exercise_id;
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                student_name = f'{row[0]} {row[1]}'
                exercise_name = row[2]
                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(f'{student_name} is currently working on:')
                for exercise in exercises:
                    print(f'\t*     {exercise}')

class StudentReport():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/davideverett/workspace/python/StudentExercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from students s
            join cohorts c on s.cohort_id = c.id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            [print(s) for s in all_students]


class InstructorReport:

    def __init__(self):
        self.db_path = "/Users/davideverett/workspace/python/StudentExercises/studentexercises.db"

    def all_instructors(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[0], row[1], row[2], row[3], row[4])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT first_name, last_name, slack_handle, cohorts.name, specialty
            FROM instructors
            JOIN cohorts
            ON instructors.cohort_id = cohorts.id
            ORDER BY instructors.last_name
            """)

            all_instructors = db_cursor.fetchall()

            [print(i) for i in all_instructors]

class CohortReport:

    def __init__(self):
        self.db_path = "/Users/davideverett/workspace/python/StudentExercises/studentexercises.db"

    def all_cohorts(self):

        print("""
        +--+--+--+--+--+--+--+--+--+--+

           COHORTS WITH FULL ROSTER

        +--+--+--+--+--+--+--+--+--+--+
        """)

        cohorts = dict()

        def cohorts_and_students():

            with sqlite3.connect(self.db_path) as conn:

                db_cursor = conn.cursor()

                db_cursor.execute("""
                SELECT cohorts.name, students.first_name, students.last_name
                FROM cohorts
                JOIN students
                ON students.cohort_id = cohorts.id;
                """)

                dataset = db_cursor.fetchall()

                for row in dataset:
                    cohort_name = row[0]
                    student_name = f'{row[1]} {row[2]}'

                    if cohort_name not in cohorts:
                        cohorts[cohort_name] = dict()
                        cohorts[cohort_name]["students"] = list()
                    else:
                        if student_name not in cohorts[cohort_name]["students"]:
                            cohorts[cohort_name]["students"].append(student_name)
                        else:
                            cohorts[cohort_name]["students"] = [student_name]

        def cohort_and_instructors():

            with sqlite3.connect(self.db_path) as conn:

                db_cursor = conn.cursor()

                db_cursor.execute("""
                SELECT cohorts.name, instructors.first_name, instructors.last_name
                FROM cohorts
                JOIN instructors
                ON instructors.cohort_id = cohorts.id;
                """)

                dataset = db_cursor.fetchall()

                for row in dataset:
                    cohort_name = row[0]
                    instructor_name = f'{row[1]} {row[2]}'

                    if cohort_name not in cohorts:
                        cohorts[cohorts_name] = dict()

                    else:
                        if "instructors" not in cohorts[cohort_name]:
                            cohorts[cohort_name]["instructors"] = list()
                            cohorts[cohort_name]["instructors"].append(instructor_name)
                        else:
                            if instructor_name not in cohorts[cohort_name]["instructors"]:
                                cohorts[cohort_name]["instructors"].append(instructor_name)

        def print_to_terminal():

            for cohort_name, cohort in cohorts.items():
                print(f'''{cohort_name}:
======================
                ''')

                print("""\tStudents:
\t_________
                """)
                for student in cohort["students"]:
                    print(f'\t\t*    {student}\n')
                
                print("""\tInstructors:
\t____________
                """)
                for instructor in cohort["instructors"]:
                    print(f'\t\t*     {instructor}\n')
        cohorts_and_students()
        cohort_and_instructors()
        print_to_terminal()
                      

class ExerciseReports:

    """Class for building exercise objects"""

    def __init__(self):
        self.db_path = "/Users/davideverett/workspace/python/StudentExercises/studentexercises.db"


    def all_exercises(self):

        """Function for querying exercises from database"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT name, language
            FROM exercises
            ORDER BY name
            """)

            all_exercises = db_cursor.fetchall()

            [print(e) for e in all_exercises]

    def javascript_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT name, language
            FROM exercises
            WHERE language = "JavaScript"
            OR language = "React"
            ORDER BY name
            """)

            javascript_exercises = db_cursor.fetchall()

            [print(e) for e in javascript_exercises]

    def python_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT name, language
            FROM exercises
            WHERE language = "Python"
            ORDER BY name
            """)

            python_exercises = db_cursor.fetchall()

            [print(e) for e in python_exercises]

    def c_sharp_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT name, language
            FROM exercises
            WHERE language
            LIKE "%C#%"
            ORDER BY name
            """)

            c_sharp_exercises = db_cursor.fetchall()

            [print(e) for e in c_sharp_exercises]



# student_reports = StudentReport()
# student_reports.all_students()

cohort_report = CohortReport()

# exercise_reports = ExerciseReports()
# exercise_reports.all_exercises()
# exercise_reports.javascript_exercises()
# exercise_reports.python_exercises()

# instructor_report = InstructorReport()
# instructor_report.all_instructors()

# exercise_reports.c_sharp_exercises()

# student_exercise_report = StudentExerciseReport()

# student_exercise_report.students_with_assignments()

# student_exercise_report.assignments_with_students()

cohort_report.all_cohorts()