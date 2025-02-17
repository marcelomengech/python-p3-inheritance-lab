# lib/student.py

from user import User  # Ensure you import the User class from user.py

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, knowledge_string):
        self.knowledge.append(knowledge_string)