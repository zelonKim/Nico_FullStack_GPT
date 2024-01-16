
# class Puppy:  
#     def __init__(self): # 생성자 메서드(def __init__)는 객체가 생성될 때마다 자동 호출됨.
#         print(self) # self에는 생성된 객체가 담김.
#         print("Puppy is born!")


# ruffus = Puppy() # <__main__.Puppy object at 0x104d2cbd0>  Puppy is born!
# print(ruffus) # <__main__.Puppy object at 0x104d2cbd0>


# tuppa = Puppy()  # <__main__.Puppy object at 0x10081cbd0>  Puppy is born!
# print(tuppa) # <__main__.Puppy object at 0x10081cbd0>


# #######################



# class Puppy:
#     def __init__(self):
#         self.name = "Ruff"


# ruffus = Puppy()
# print(ruffus.name) # Ruff

# chorong = Puppy()
# print(chorong.name) # Ruff



# #######################



# class Puppy:
#     def __init__(self, name):
#         self.name = name


# ruffus = Puppy("Ruff")
# print(ruffus.name) # Ruff

# chorong = Puppy("Cho")
# print(chorong.name) # Cho








# ######################################







class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


ruffus = Puppy("Ruff", 3, "Beagle")
print(ruffus.name) # Ruff
print(ruffus.age) # 3
print(ruffus.breed) # Beagle


chorong = Puppy("Cho", 5, "Dalmatian")
print(chorong.name) # Cho
print(chorong.age) # 5
print(chorong.breed) # Dalmatian
print()


################


class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


ruffus = Puppy(breed="Beagle", name="Ruff", age=3)
print(ruffus.name) # Ruff
print(ruffus.age) # 3
print(ruffus.breed) # Beagle


chorong = Puppy(breed="Dalmatian", name="Cho", age=5)
print(chorong.name) # Cho
print(chorong.age) # 5
print(chorong.breed) # Dalmatian
print()




###################################




class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self): # 객체의 메모리 주소 대신, 반환값이 출력되도록 해줌.
         return "hello"


ruffus = Puppy(breed="Beagle", name="Ruff", age=3)
print(ruffus) # hello

chorong = Puppy(breed="Dalmatian", name="Cho", age=5)
print(chorong) # hello
print()


###############


class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self): 
         return f"Puppy`s name is {self.name}"


ruffus = Puppy(breed="Beagle", name="Ruff", age=3)
print(ruffus) # Puppy`s name is Ruff

chorong = Puppy(breed="Dalmatian", name="Cho", age=5)
print(chorong) # Puppy`s name is Cho
print()




##############################




class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def sing(self):
        print("Woof Woof")


ruffus = Puppy(breed="Beagle", name="Ruff", age=3)
ruffus.sing() # Woof Woof

chorong = Puppy(breed="Dalmatian", name="Cho", age=5)
chorong.sing() # Woof Woof
print()


############################


class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def sing(self):
        print("Woof Woof")

    def introduce(self):
        self.sing()
        print(f"My name is {self.name}")


ruffus = Puppy(breed="Beagle", name="Ruff", age=3)
ruffus.introduce() # Woof Woof  My name is Ruff

chorong = Puppy(breed="Dalmatian", name="Cho", age=5)
chorong.introduce() # Woof Woof  My name is Cho
print()




########################################




class GuardDog:
    def __init__(self, name, age, breed):
        self.name = name
        self.breed = breed
        self.age = age

    def sing(self):
        print("Grrrrrr")



class Puppy:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sing(self):
        print("Woof Woof")



bibi = GuardDog("Bibi", "Husky", 5) 
bibi.sing() # Grrrrrr

ruffus = Puppy("Ruffus", "Beagle", 2)
ruffus.sing() # Woof Woof
print()



##############
        


# 부모 클래스 -> 클래스들마다 공통된 부분
class Dog: 
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age



# 자식 클래스 -> 클래스들마다 서로 다른 부분
class GuardDog(Dog): # 자식 클래스명(부모 클래스명)을 통해 상속받음.
    def sing(self):
        print("Grrrrrrr")


class Puppy(Dog):
    def sing(self):
        print("Woof Woof")



bibi = GuardDog("Bibi", "Husky", 5) 
bibi.sing() # Grrrrrr

ruffus = Puppy("Ruffus", "Beagle", 2)
ruffus.sing() # Woof Woof
print()




####################################
        



class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sleep(self):
        print("Zzzzzz")



class GuardDog(Dog):
    def sing(self):
        print("Grrrrrrr")



class Puppy(Dog):
    def sing(self):
        print("Woof Woof")



bibi = GuardDog("Bibi", "Husky", 5) 
bibi.sleep() # Zzzzzz
bibi.sing() # Grrrrrrr

ruffus = Puppy("Ruffus", "Beagle", 2)
ruffus.sleep() # Zzzzzz
ruffus.sing() # Woof Woof
print()



###################
        


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sleep(self):
        print("Zzzzzz")



class GuardDog(Dog):
    def sing(self):
        super().sleep()  # super().메서드명()을 통해 '부모 클래스'의 메서드를 호출함.
        print("Grrrrrrr")



class Puppy(Dog):
    def sing(self):
        super().sleep()
        print("Woof Woof")



bibi = GuardDog("Bibi", "Husky", 5) 
bibi.sing() # Zzzzzz  Grrrrrrr


ruffus = Puppy("Ruffus", "Beagle", 2)
ruffus.sing() # Zzzzzz  Woof Woof
print()




###################################




class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age



class GuardDog(Dog):
   pass



class Puppy(Dog):
   pass



bibi = GuardDog("Bibi", "Husky", 5) 
print(bibi.age) # 5

ruffus = Puppy("Ruffus", "Beagle", 2)
print(ruffus.age) # 2
print()



##################
        


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age



class GuardDog(Dog):
   def __init__(self, name, breed):
       super().__init__(name, breed, 5)



class Puppy(Dog):
    def __init__(self, name, breed):
       super().__init__(name, breed, 2)
    
    

bibi = GuardDog("Bibi", "Husky") 
print(bibi.age) # 5

ruffus = Puppy("Ruffus", "Beagle")
print(ruffus.age) # 2
print()




################################





class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age



class GuardDog(Dog):
    def __init__(self):
       self.aggressive=True



class Puppy(Dog):
    def __init__(self):
       self.aggressive=False



bibi = GuardDog() 
print(bibi.aggressive) # True


ruffus = Puppy()
print(ruffus.aggressive) # False
print()









#################################################










def create_player(name, team):
    return {
        "name": name,
        "team": team
    }


def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello, I`m {name}, and I play for {team}")



nico = create_player("Nico", "Team Red")
lynn = create_player("Lynn", "Team Blue")


introduce_player(nico) # Hello, I`m Nico, and I play for Team Red
introduce_player(lynn) # Hello, I`m Lynn, and I play for Team Blue
print()



#####################



class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def introduce(self):
        print(f"Hello, I`m {self.name}, and I play for {self.team}")



nico = Player(name="Nico", team="Team Red")
nico.introduce() # Hello, I`m Nico, and I play for Team Red


lynn = Player(name="Lynn", team="Team Blue")
lynn.introduce() # Hello, I`m Lynn, and I play for Team Blue
print()




#####################




class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def introduce(self):
        print(f"Hello, I`m {self.name}, and I play for {self.team}")



class Team:
    def __init__(self, team_name):
        self.players = []
        self.team_name = team_name

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def show_players(self):
        for player in self.players:
            player.introduce()



team_red = Team("Team Red")
team_red.add_player("Nico")
team_red.show_players()  # Hello, I`m Nico, and I play for Team Red


team_blue = Team("Team Blue")
team_blue.add_player("Lynn")
team_blue.show_players()  # Hello, I`m Lynn, and I play for Team Blue