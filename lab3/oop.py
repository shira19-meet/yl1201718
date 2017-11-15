class Animal(object):
    def __init__(self,sound,name,age,favorite_color):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
    def eat(self,food):
        print(" I like food " + self.name + " is eating " + food)
    def description(self):
        print(self.name+ "is" + str(self.age) + " years old and loves the color " + self.favorite_color)
    def make_sound(self,sound):
        print(sound)

dog = Animal("wak wak wak", "shoody" ,108 ,"black")
cat = Animal("arish arish arish", "lammy", 0, "no color")
dog.description()
cat.make_sound("wak wak wak")

class Person(object):
    def __init__(self,name,age,gender, eye_color,favorite_food):
        self.age = age
        self.name = name
        self.gender = gender
        self.eye_color = eye_color
        self.favorite_food = favorite_food
    def food(self,):
        print(self.name,"likes to eat " + self.favorite_food)
    def name1(self,):
        print("my name is " + self.name)
person1 = Person("Shikma", "14", "female", "brown", "avocado")
person1.name1()
