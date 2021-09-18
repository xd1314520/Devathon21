from scholarship_portal import db
import datetime


class Student(db.Model):
    __tablename__ = "student"
    roll_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    branch = db.Column(db.String(8), nullable=False)
    caste = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(10), nullable=False)
    cgpa = db.Column(db.Float)
    applications = db.relationship("application")

    def __repr__(self) -> str:
        return f"Student(roll_no : {self.roll_no}, name : {self.name})"


class Application(db.Model):
    __tablename__ = "application"
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(120), nullable=False)
    stud_roll_no = db.Column(db.Integer, db.ForeignKey("student.id"))
    status = db.Column(db.Boolean, nullable=False, default=False)
    documents = db.relationship("document", backref="application", lazy=True)

    def __repr__(self) -> str:
        return f"Application(roll no : {self.stud_roll_no})"


class Document(db.Model):
    __tablename__ = "document"
    id = db.Column(db.Integer, db.ForeignKey("application.id"))
    filename = db.Column(db.String(120), nullable=False)


class Scholarship(db.Model):
    __tablename__ = "scholarship"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    opening_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    closing_date = db.Column(db.DateTime, nullable=False)
    stub = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    caste = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    program = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(10), nullable=False)
    required_cgpa = db.Column(db.Float)
    external_link = db.Column(db.String(240))

    def __repr__(self) -> str:
        return f"Scholarship(name : {self.name})"


class AdminUser(db.Model):
    __tablename__ = "adminuser"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"AdminUser(email : {self.email})"
