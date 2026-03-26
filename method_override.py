class Adult:
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        return True


class Child(Adult):
    def can_drive(self):
        return f"{self.name} is too young to drive."


name = input("What is your name? ")
age = int(input("What is your age? "))
eye_color = input("What is your eye color? ")
hair_color = input("What is your hair color? ")


if 18 <= age < 150:
    person = Adult(name, age, eye_color, hair_color)

elif 0 <= age < 18:
    person = Child(name, age, eye_color, hair_color)

else:
    print("Invalid age entered.")
    exit()


print(person.can_drive())