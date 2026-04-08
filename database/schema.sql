PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Grades;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Groups;
DROP TABLE IF EXISTS Disciplines;

CREATE TABLE Groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_code TEXT NOT NULL UNIQUE,
    course INTEGER NOT NULL
);

CREATE TABLE Disciplines (
    disc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disc_name TEXT NOT NULL UNIQUE,
    teacher_name TEXT
);

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES Groups(group_id) ON DELETE SET NULL
);

CREATE TABLE Grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    disc_id INTEGER,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (disc_id) REFERENCES Disciplines(disc_id) ON DELETE CASCADE
);

INSERT INTO Groups (group_code, course) VALUES 
    ('IS-21', 2),
    ('IS-22', 2),
    ('PM-21', 2),
    ('EC-21', 2),
    ('IS-31', 3);

INSERT INTO Disciplines (disc_name, teacher_name) VALUES 
    ('Databases', 'Petrov I.S.'),
    ('Programming', 'Petrov I.S.'),
    ('Mathematics', 'Sidorova A.M.'),
    ('Economics', 'Kuznetsov D.A.'),
    ('English', 'Volkova E.P.');

INSERT INTO Students (full_name, group_id) VALUES 
    ('Nikulin Nikita', 1),
    ('Ivanov Artem', 1),
    ('Petrova Maria', 1),
    ('Sidorov Konstantin', 2),
    ('Kuznetsova Anastasia', 2),
    ('Vasiliev Egor', 3),
    ('Mikhailova Daria', 3),
    ('Novikov Ilya', 4),
    ('Fedorova Sofia', 4),
    ('Alekseev Maxim', 5);

INSERT INTO Grades (student_id, disc_id, grade) VALUES 
    (1, 1, 5),
    (1, 2, 5),
    (1, 3, 4),
    (2, 1, 4),
    (2, 2, 5),
    (3, 1, 3),
    (3, 2, 4),
    (4, 1, 5),
    (4, 2, 4),
    (5, 1, 4),
    (6, 3, 5),
    (7, 3, 4),
    (8, 4, 3),
    (9, 5, 5),
    (10, 1, 5),
    (10, 2, 4);

SELECT
    s.full_name AS "Student",
    g.group_code AS "Group",
    d.disc_name AS "Discipline",
    gr.grade AS "Grade",
    d.teacher_name AS "Teacher"
FROM Grades gr
JOIN Students s ON gr.student_id = s.student_id
JOIN Groups g ON s.group_id = g.group_id
JOIN Disciplines d ON gr.disc_id = d.disc_id
ORDER BY g.group_code, s.full_name;