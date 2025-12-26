from flask import Flask, render_template, request, redirect, url_for
from models.student import Student
from models.subject import Subject

app = Flask(__name__)

# Seed demo data
english = Subject("English", 100, 75, "Mr. Smith")
mathematics = Subject("Mathematics", 100, 88, "Dr. Johnson")
physics = Subject("Physics", 100, 92, "Dr. Brown")
chemistry = Subject("Chemistry", 100, 81, "Ms. Davis")
biology = Subject("Biology", 100, 85, "Dr. Wilson")
history = Subject("History", 100, 70, "Mr. Taylor")
geography = Subject("Geography", 100, 78, "Ms. Clark")
computerScience = Subject("Computer Science", 100, 95, "Dr. White")
art = Subject("Art", 100, 90, "Ms. Lewis")
physicalEducation = Subject("Physical Education", 100, 100, "Coach Martin")

students = [
    Student("Alice", 12, [english, chemistry, geography]),
    Student("Bob", 14, [physics, mathematics, history]),
    Student("Charlie", 13, [biology, computerScience])
]

@app.route("/")
def home():
    return render_template("index.html", students=students)

@app.route("/student/<int:student_id>")
def student_detail(student_id):
    student = students[student_id]
    return render_template("student.html", student=student, student_id=student_id)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        new_student = Student(name, age, [])
        students.append(new_student)
        return redirect(url_for("home"))
    return render_template("add_student.html")

@app.route("/add_subject/<int:student_id>", methods=["POST"])
def add_subject(student_id):
    student = students[student_id]
    name = request.form["name"]
    max_score = int(request.form["max_score"])
    score = int(request.form["score"])
    teacher = request.form["teacher"]
    new_subject = Subject(name, max_score, score, teacher)
    student.addSubject(new_subject)
    return redirect(url_for("student_detail", student_id=student_id))

@app.route("/remove_subject/<int:student_id>/<int:subject_index>")
def remove_subject(student_id, subject_index):
    student = students[student_id]
    student.removeSubject(subject_index)
    return redirect(url_for("student_detail", student_id=student_id))

if __name__ == "__main__":
    app.run(debug=True)
