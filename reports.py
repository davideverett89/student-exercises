import sqlite3
from student import Student
from exercise import Exercise
from cohort import Cohort
from instructor import Instructor


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
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT name FROM Cohorts
            ORDER BY name
            """)

            all_cohorts = db_cursor.fetchall()

            [print(cohort) for cohort in all_cohorts]
                

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

# cohort_report = CohortReport()
# cohort_report.all_cohorts()

exercise_reports = ExerciseReports()
# exercise_reports.all_exercises()
# exercise_reports.javascript_exercises()
# exercise_reports.python_exercises()

# instructor_report = InstructorReport()
# instructor_report.all_instructors()

exercise_reports.c_sharp_exercises()