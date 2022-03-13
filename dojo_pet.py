from http.server import BaseHTTPRequestHandler


class Pet:

    #implement __init__(name, type,tricks,health):
    def __init__(self,name,type,tricks,noisee):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=100
        self.energy= 50
        self.noisee= noisee
    
    def sleep(self):
        self.energy +=25
        return self

    def eat(self):
        self.energy +=5
        self.health +=10
        return self

    def play(self):
        self.health +=5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)
        return self


class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food, pet):
        self.first_name= first_name
        self.last_name =last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
    

    def walk(self):
        self.pet.play()
        return self


    def feed(self):
        if len(self.pet_food) > 0:
            food=self.pet_food.pop()
            print(f"feeding {self.pet.name}")
            self.pet.eat()
        print ("you need more pet food")
        return self


    def bathe(self):
        self.pet.noise()

treats=['bacon',"trash bag", "snausage"]
my_pet_food =["pizza","sushi", treats]
nibbles=Pet("Mr. nibbles","Horse",['nibbles on things','is invisible'],"Hey")
begum = Ninja("begum","batuhan",treats,my_pet_food,nibbles)


begum.feed()
begum.feed()
begum.feed()
