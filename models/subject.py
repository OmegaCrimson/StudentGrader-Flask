class Subject:
    
    """
    Represents a school subject with grading information and teacher assignment.

    A Subject tracks the student's grade in a specific subject, the maximum
    possible grade, and the teacher responsible for the subject. Input values
    are validated to ensure consistency and correctness.

    Attributes
    ----------
    name : str
        The name of the subject (3–30 characters).
    maxGrade : float
        The maximum achievable grade for the subject (0 < maxGrade <= 1000).
    grade : float
        The student's grade in the subject (0 <= grade <= maxGrade).
    teacher : str
        The teacher's name (3–30 characters).

    Methods
    -------
    name : property
        Get or set the subject name with validation.
    maxGrade : property
        Get or set the maximum grade with validation.
    grade : property
        Get or set the student's grade with validation.
    teacher : property
        Get or set the teacher's name with validation.
    """

    def __init__(self,name: str,maxGrade: float,grade:float ,teacher: str) -> None:
        self.name = name
        self.maxGrade = maxGrade
        self.grade = grade
        self.teacher = teacher

    @property
    def name(self) -> str:
        return self.__name 
    
    @name.setter
    def name(self,value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("subject name must be string")
        value = value.strip()
        if len(value) > 2 and len(value) <= 30:
            self.__name = value
        else:
            raise ValueError("subject name length must be between 3 - 30")
        
    @property
    def maxGrade(self) -> float:
        return round(self.__maxGrade,0)
    
    @maxGrade.setter
    def maxGrade(self,value: float) -> None:
        if isinstance(value,int):
            value = float(value)
        elif not isinstance(value,float):
            raise TypeError("max grade must be a number")
        if value > 0.0 and value <= 1000.0:
            self.__maxGrade = round(value,0)
        else:
            raise ValueError("max grade value must be between 0 - 1000")

    @property
    def grade(self) -> float:
        return round(self.__grade,2)
    
    @grade.setter
    def grade(self,value: float) -> None:
        if isinstance(value,int):
            value = float(value)
        elif not isinstance(value,float):
            raise TypeError("grade must be number")
        if value >= 0 and value <= self.maxGrade:
            self.__grade = value
        else:
            raise ValueError(f"grade value must be between 0 - {self.maxGrade}")
        
    @property
    def teacher(self) -> str:
        return self.__teacher
    
    @teacher.setter
    def teacher(self,value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("teacher name must be string")
        value = value.strip()
        if len(value) > 2 and len(value) <= 30:
            self.__teacher= value
        else:
            raise ValueError("teacher name length must be between 3 - 30")
        
    def averageGrade(self) -> float:
        return round(self.grade/self.maxGrade,2)*100
    
    def __str__(self) -> str:
        return f"Subject Name: {self.name.title()} | Taught by: {self.teacher.title()} | Maximum Grade: {self.maxGrade} | Student's Grade: {self.grade}"