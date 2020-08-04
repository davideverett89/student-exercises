DELETE FROM cohorts;
DELETE FROM students;
DELETE FROM instructors;
DELETE FROM exercises;
DELETE FROM student_exercises;

DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS student_exercises;

CREATE TABLE cohorts (
    id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name   TEXT NOT NULL UNIQUE
);

CREATE TABLE students (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY('cohort_id') REFERENCES 'cohorts'('id')
);

CREATE TABLE instructors (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    specialty TEXT NOT NULL,
    FOREIGN KEY('cohort_id') REFERENCES 'cohorts'('id')
);

CREATE TABLE exercises (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    language TEXT NOT NULL
);

CREATE TABLE student_exercises (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    FOREIGN KEY('student_id') REFERENCES 'students'('id'),
    FOREIGN KEY('exercise_id') REFERENCES 'exercises'('id')
);

INSERT INTO cohorts (name)
VALUES ('Day Cohort 40');

INSERT INTO cohorts (name)
VALUES ('Evening Cohort 11');

INSERT INTO cohorts (name)
VALUES ('Day Cohort 41');

INSERT INTO cohorts (name)
VALUES ('Evening Cohort 12');

INSERT INTO exercises (name, language)
VALUES ('Products Cards', 'CSS');

INSERT INTO exercises (name, language)
VALUES ('Sorting Hat', 'JavaScript');

INSERT INTO exercises (name, language)
VALUES ('Pet Adoption', 'JavaScript');

INSERT INTO exercises (name, language)
VALUES ('Stocks Report', 'Python');

INSERT INTO exercises (name, language)
VALUES ('Cash to Coins', 'Python');

INSERT INTO exercises (name, language)
VALUES ('Coins to Cash', 'Python');

INSERT INTO exercises (name, language)
VALUES ('Kandy Korner', 'JavaScript');

INSERT INTO exercises (name, language)
VALUES ('Bear Watcher', 'JavaScript');

INSERT INTO exercises (name, language)
VALUES ('Tamagotchi', 'SASS');

INSERT INTO exercises (name, language)
VALUES ('Sports Roster', 'React');

INSERT INTO exercises (name, language)
VALUES ('Pinterest', 'JavaScript');

INSERT INTO exercises (name, language)
VALUES ('React Hoarder', 'React');

INSERT INTO exercises (name, language)
VALUES ('Hello World', 'C#');

INSERT INTO exercises (name, language)
VALUES ('Plan Your Heist', 'C#');

INSERT INTO exercises (name, language)
VALUES ('Chinook', 'C#');

INSERT INTO instructors (first_name, last_name, slack_handle, cohort_id, specialty)
SELECT 'Zoe', 'Ames', 'Zoe Ames', cohorts.id, 'Cats'
FROM cohorts
WHERE cohorts.name = "Evening Cohort 11";

INSERT INTO instructors (first_name, last_name, slack_handle, cohort_id, specialty)
SELECT 'Joe', 'Shepard', 'Joe Shepard', cohorts.id, 'Dad Jokes'
FROM cohorts
WHERE cohorts.name = 'Day Cohort 40';

INSERT INTO instructors (first_name, last_name, slack_handle, cohort_id, specialty)
SELECT 'Luke', 'Lancaster', 'Luke Lancaster', cohorts.id, 'Coffee'
FROM cohorts
WHERE cohorts.name = 'Evening Cohort 12';

INSERT INTO instructors (first_name, last_name, slack_handle, cohort_id, specialty)
SELECT 'John', 'Doe', 'John Doe', cohorts.id, 'Being mysterious'
FROM cohorts
WHERE cohorts.name = 'Day Cohort 41';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'David', 'Everett', 'David Everett', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 40";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Davis', 'Lindell', 'Davis Lindell', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 40";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Bethany', 'Whitworth', 'Bethany Whitworth', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 11";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Aaron', 'Lain', 'Aaron Lain', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 11";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Anca', 'Simon', 'Anca Simon', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 11";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Kenny', 'McEastland', 'Kenny McEastland', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 11";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Liza', 'Star', 'Liza Star', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 11";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Daniel', 'Meza', 'Daniel Meza', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 40";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Evan', 'Reynolds', 'Evan Reynolds', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 40";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Luke', 'Esworthy', 'Luke Esworthy', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 40";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Kaleb', 'Moran', 'Kaleb Moran', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 41";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Kirk', 'Sudduth', 'Kirk Sudduth', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 41";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Brian', 'Cravens', 'Brian Cravens', cohorts.id
FROM cohorts
WHERE cohorts.name = "Day Cohort 41";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Todd', 'Spainour', 'Todd Spainhour', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 12";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Steven', 'Zelenak', 'Steven Zelenak', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 12";

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Sarah', 'Holder', 'Sarah Holder', cohorts.id
FROM cohorts
WHERE cohorts.name = "Evening Cohort 12";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "David Everett"
AND exercises.name = "Pet Adoption";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "David Everett"
AND exercises.name = "Sports Roster";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Davis Lindell"
AND exercises.name = "Sports Roster";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Davis Lindell"
AND exercises.name = "Products Cards";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Aaron Lain"
AND exercises.name = "Sorting Hat";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Aaron Lain"
AND exercises.name = "Pinterest";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Bethany Whitworth"
AND exercises.name = "React Hoarder";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Bethany Whitworth"
AND exercises.name = "Pinterest";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Anca Simon"
AND exercises.name = "Sports Roster";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Anca Simon"
AND exercises.name = "Stocks Report";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Kenny McEastland"
AND exercises.name = "Sorting Hat";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Kenny McEastland"
AND exercises.name = "Bear Watcher";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Liza Star"
AND exercises.name = "Tamagotchi";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Liza Star"
AND exercises.name = "Kandy Korner";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Daniel Meza"
AND exercises.name = "Tamagotchi";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Daniel Meza"
AND exercises.name = "Cash to Coins";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Evan Reynolds"
AND exercises.name = "Coins to Cash";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Evan Reynolds"
AND exercises.name = "Pet Adoption";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Luke Esworthy"
AND exercises.name = "Products Cards";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Luke Esworthy"
AND exercises.name = "Pinterest";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Kaleb Moran"
AND exercises.name = "Tamagotchi";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Kaleb Moran"
AND exercises.name = "React Hoarder";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Kirk Sudduth"
AND exercises.name = "Kandy Korner";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Kirk Sudduth"
AND exercises.name = "Coins to Cash";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Brian Cravens"
AND exercises.name = "Bear Watcher";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Brian Cravens"
AND exercises.name = "Stocks Report";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Todd Spainhour"
AND exercises.name = "Sorting Hat";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Todd Spainhour"
AND exercises.name = "Sports Roster";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Steven Zelenak"
AND exercises.name = "React Hoarder";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Steven Zelenak"
AND exercises.name = "Pinterest";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Sarah Holder"
AND exercises.name = "Coins to Cash";

INSERT INTO student_exercises (student_id, exercise_id)
SELECT students.id, exercises.id
FROM students, exercises
WHERE students.slack_handle = "Sarah Holder"
AND exercises.name = "Pet Adoption";

SELECT students.first_name AS "First Name", students.last_name AS "Last Name", exercises.name AS "Assignment"
FROM students
JOIN student_exercises
ON students.id = student_exercises.student_id
JOIN exercises
ON exercises.id = student_exercises.exercise_id;

SELECT exercises.name AS "Assignment", students.first_name AS "First Name", students.last_name AS "Last Name"
FROM exercises
JOIN student_exercises ON student_exercises.exercise_id = exercises.id
JOIN students ON students.id = student_exercises.student_id;

SELECT cohorts.name, students.first_name, students.last_name
FROM cohorts
JOIN students
ON students.cohort_id = cohorts.id;

SELECT cohorts.name, instructors.first_name, instructors.last_name
FROM cohorts
JOIN instructors
ON instructors.cohort_id = cohorts.id;

SELECT instructors.first_name, instructors.last_name, cohorts.name cohort_name, exercises.name
FROM instructors
JOIN cohorts
ON cohorts.id = instructors.cohort_id
JOIN students
ON students.cohort_id = cohorts.id
JOIN student_exercises
ON students.id = student_exercises.student_id
JOIN exercises
ON exercises.id = student_exercises.exercise_id;

SELECT 
    exercises.name as "Exercise", 
    instructors.first_name AS "Instructor First Name", 
    instructors.last_name AS "Instructor Last Name", 
    students.first_name AS "Student First Name", 
    students.last_name AS "Student Last Name"
FROM exercises
JOIN student_exercises ON exercises.id = student_exercises.exercise_id
JOIN students ON student_exercises.student_id = students.id
JOIN cohorts ON students.cohort_id = cohorts.id
JOIN instructors ON cohorts.id = instructors.cohort_id;