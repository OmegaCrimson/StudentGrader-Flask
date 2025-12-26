from models.subject import Subject

class Student:
    """
    Represents a student with personal information and enrolled subjects.

    Attributes
    ----------
    name : str
        The student's name (3–30 characters).
    age : int
        The student's age (1–30 years).
    subjects : list of Subject
        A list of `Subject` instances representing the student's enrolled subjects.
    """

    def __init__(self, name: str, age: int, subjects: list[Subject]):
        self.name = name
        self.age = age
        self.subjects = subjects

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError("student name must be string")
        if 3 <= len(value) <= 30:
            self.__name = value
        else:
            raise ValueError("student name length must be between 3 - 30")

    @property
    def age(self) -> float:
        return float(self.__age)

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        if 0 < value <= 30:
            self.__age = value
        else:
            raise ValueError("age value must be between 0 - 30")

    @property
    def subjects(self) -> list[Subject]:
        return getattr(self, "_Student__subjects", [])

    @subjects.setter
    def subjects(self, value: list[Subject]) -> None:
        if not isinstance(value, list):
            raise TypeError("subjects must be a list")
        self.__subjects = value

    # ---------------- Methods ---------------- #

    def averageGrade(self) -> float:
        if not self.subjects:
            return 0.0
        total = sum(s.grade for s in self.subjects)
        return round(total / len(self.subjects), 2)

    def listSubjects(self) -> None:
        for subject in self.subjects:
            print(subject)

    def listSubjectsDetails(self) -> None:
        for i, subject in enumerate(self.subjects):
            print(f"{i}: {subject}")

    def addSubject(self, subject: Subject) -> None:
        self.subjects.append(subject)

    def removeSubject(self, index: int) -> None:
        if 0 <= index < len(self.subjects):
            self.subjects.pop(index)
        else:
            raise IndexError("Invalid subject index")

    def __str__(self) -> str:
        return f"Student: {self.name}, Age: {self.age}, Subjects: {len(self.subjects)}"
