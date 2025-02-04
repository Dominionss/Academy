class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def check_age(self):
        print(f"{self.name} {self.lastname} is {self.age} years old.")


class Student(Person):
    def __init__(self, name, lastname, age, scores: dict):
        super().__init__(name, lastname, age)
        self.scores = scores

    def calculate_average_score(self):
        average_score = 0
        for score in self.scores:
            average_score += self.scores[score]

        average_score /= len(self.scores)
        print(f"{self.name} {self.lastname} has the average score of {average_score}.")


class Teacher(Person):
    def __init__(self, name, lastname, age, salary_for_hour):
        super().__init__(name, lastname, age)
        self.salary_for_hour = salary_for_hour
        self.working_hours = 0

    def lead_lesson(self, subject, hours):
        print(f"{self.name} {self.lastname} has lead the lesson of {subject} and it took {hours} hour(s).")

    def calculate_all_salary(self):
        all_salary = self.salary_for_hour * self.working_hours
        print(f"{self.name} {self.lastname} has gain {all_salary} dollar(s) up to now.")

