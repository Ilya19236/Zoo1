class Animal:
    def __init__(self, nameOfView, biom, squarePerOne, ration, sound, typeByMethodOfEat,  name, age, consumesFoodPerDay, mass):
        self.__nameOfView = nameOfView
        self.__biom = biom
        self.__squarePerOne = squarePerOne
        self.__ration = ration
        self.__sound = sound
        self.__typeByMethodOfEat = typeByMethodOfEat
        self.__name = name
        self.__consumesFoodPerDay = consumesFoodPerDay
        self.__age = age
        self.__mass = mass
        self.__necessaryFoodVulumeForOneFiding = consumesFoodPerDay / 3

    @property
    def nameOfView(self):
        return self.__nameOfView

    @property
    def biom(self):
        return self.__biom

    @property
    def squarePerOne(self):
        return self.__squarePerOne

    @property
    def ration(self):
        return self.__ration

    @property
    def sound(self):
        return self.__sound

    @property
    def typeByMethodOfEat(self):
        return self.__typeByMethodOfEat

    @property
    def name(self):
        return self.__name

    @property
    def consumesFoodPerDay(self):
        return self.__consumesFoodPerDay

    @property
    def age(self):
        return self.__age

    @property
    def mass(self):
        return self.__mass


    def Play(self):
        print(self.__name, " поигрался с собой.")

    def MakeSound(self):
        print(self.__name, ": ", self.__sound)

    def Eat(self, food, portion):
        self.thePreviousMass = self.__mass
        if food in self.__ration:
            print(self.__name, " покушал.")
            self.__mass += portion
        else:
            print(self.__name, "отказался кушать. Данная еда не входит в рацион данного животного.")

    def IsFeeded (self):
        if self.thePreviousMass + self.__necessaryFoodVulumeForOneFiding <= self.__mass:
            answer = True
        else:
            answer = False
        return answer