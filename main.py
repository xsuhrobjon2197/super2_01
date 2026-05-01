#2-m
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
    def introdoue(self):
        print(f"{self.name}, {self.age}, {self.gender}")
        
    
class Studend(Person):
    def __init__(self, name, age, gender, grade, universtity):
