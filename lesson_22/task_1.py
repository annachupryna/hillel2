from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import random
import sqlite3
import pandas as pd

Base = declarative_base()

student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_course, back_populates='students')


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship('Student', secondary=student_course, back_populates='courses')


db_url = 'sqlite:///students.db'
engine = create_engine(db_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

courses = [Course(title=f'Course {i}') for i in range(1, 6)]
session.add_all(courses)
session.commit()

students = [Student(name=f'Student {i}') for i in range(1, 21)]
for student in students:
    student.courses = random.sample(courses, k=random.randint(1, 3))
session.add_all(students)
session.commit()


def add_student(name, course_title):
    student = Student(name=name)
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        student.courses.append(course)
    session.add(student)
    session.commit()


def get_students_by_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    return [student.name for student in course.students] if course else []


def get_courses_by_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    return [course.title for course in student.courses] if student else []


def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()


def delete_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        session.delete(student)
        session.commit()


add_student("New Student", "Course 1")
print(get_students_by_course("Course 1"))
print(get_courses_by_student("New Student"))
update_student_name("New Student", "Updated Student")
delete_student("Updated Student")

# Зчитати базу
conn = sqlite3.connect("students.db")
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

students = pd.read_sql("SELECT * FROM students;", conn)
print(students)

conn.close()
