class Aviary:
    def __init__(self, name, typeOfbiom, square):
        self.__name = name
        self.__typeOfbiom = typeOfbiom
        self.__square = square
        self.__animalsThatLivesHere = []
        self.__animalsThatLivesHereID = []
        self.IsAnimal = ""

    @property
    def name(self):
        return self.__name

    @property
    def TypeOfbiom(self):
        return self.__typeOfbiom

    @property
    def square(self):
        return self.__square

    @property
    def animalsThatLivesHere(self):
        return self.__animalsThatLivesHere

    @property
    def animalsThatLivesHereID(self):
        return self.__animalsThatLivesHereID

    def AddFirstAnimal(self, firstAnimal):
        if len(self.__animalsThatLivesHere) == 0 and self.__square >= firstAnimal.squarePerOne and (firstAnimal.biom == self.__typeOfbiom or firstAnimal.biom == "Везде"):
            self.__animalsThatLivesHere.append(firstAnimal.name)
            self.__animalsThatLivesHereID.append(firstAnimal)
            self.IsAnimal = firstAnimal

    def AddNewAnimal(self, newAnimal):
        if len(self.__animalsThatLivesHere) > 0 and self.__square >= newAnimal.squarePerOne and (newAnimal.biom == self.__typeOfbiom or newAnimal.biom == "Везде") and (newAnimal.typeByMethodOfEat == "плотоядный" or newAnimal.typeByMethodOfEat == "всеядный"):
            if self.IsAnimal.__class__ == newAnimal.__class__:
                    self.__animalsThatLivesHere.append(newAnimal.name)
                    self.__animalsThatLivesHereID.append(newAnimal)
        elif len(self.__animalsThatLivesHere) > 0 and self.__square >= newAnimal.squarePerOne and (newAnimal.biom == self.__typeOfbiom or newAnimal.biom == "Везде") and newAnimal.typeByMethodOfEat == "травоядный":
            if self.IsAnimal.typeByMethodOfEat == "травоядный":
                self.__animalsThatLivesHere.append(newAnimal.name)
                self.__animalsThatLivesHereID.append(newAnimal)

    def MoveTheAnimalOut(self, animal):
        for i in range(len(self.__animalsThatLivesHere)):
            if self.__animalsThatLivesHere[i] == animal.name:
                AnimalThatMoveOut = animal
        self.__animalsThatLivesHere.remove(AnimalThatMoveOut.name)
        self.__animalsThatLivesHereID.remove(AnimalThatMoveOut)

    def AllAnimalsMakeSounds(self):
        answer = []
        for i in range(len(self.__animalsThatLivesHereID)):
            everyAnimalThatLivesHere = self.__animalsThatLivesHereID[i]
            SoundThatMakeOneAnimal = (everyAnimalThatLivesHere.name, ":", everyAnimalThatLivesHere.MakeSound())
            answer.append(SoundThatMakeOneAnimal)

    def FeedAllAnimals (self, food, portion):
        for i in range(len(self.__animalsThatLivesHereID)):
            everyAnimalThatLivesHere = self.__animalsThatLivesHereID[i]
            print(everyAnimalThatLivesHere.ration)
            print(food)
            for l in range(len(food)):
                IsFood = food[l]
            if IsFood in everyAnimalThatLivesHere.ration:
                print(everyAnimalThatLivesHere.name, " покушал.")
            else:
                print(everyAnimalThatLivesHere.name, "отказался кушать. Данная еда не входит в рацион данного животного.")