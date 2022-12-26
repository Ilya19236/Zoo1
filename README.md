from Tiger import *
from Leopard import *
from Alabay import *
from Horse import *
from Sheep import *
from Aviary import *

Andrey = AmurTiger("Амурский Тигр", "Снежный", 10, ["изюбрь", "кабан", "пятнистый олень"], "Рррр", "плотоядный", "Андрей", 4, 9, 300)
Eugene = FarEastLeopard ("Дальневосточный Леопард", "Снежный", 10, ["косуля", "заяц", "барсук"], "Рррр", "плотоядный", "Евгений", 2, 6, 55)
Petya = Alabay("Алабай", "Везде", 6, ["говядина", "собачий корм", "кость" ], "Аф-аф", "плотоядный", "Петя", 3, 3, 70)
Victoria = ArabicHorse("Арабская Лошадь", "Загон", 15, ["трава", "сено"], "Ржанье", "травоядный", "Виктория", 15, 6, 380)
Maria = Sheep("Овца", "Загон", 15, ["трава", "сено", "силос"], "Беееее", "травоядный", "Мария", 8, 6, 60)
Julia = AmurTiger("Амурский Тигр", "Снежный", 10, ["изюбрь", "кабан", "пятнистый олень"], "Рррр", "плотоядный", "Юлия", 4, 9, 300)
Roman = FarEastLeopard ("Дальневосточный Леопард", "Снежный", 10, ["косуля", "заяц", "барсук"], "Рррр", "плотоядный", "Роман", 2, 6, 50)
Gennadiy = Alabay("Алабай", "Везде", 6, ["говядина", "обачий корм", "кость" ], "Аф-аф", "плотоядный", "Геннадий", 3, 3, 65)


Andrey.MakeSound()
Eugene.MakeSound()
Petya.MakeSound()
Victoria.MakeSound()
Maria.MakeSound()

Andrey.Play()
Eugene.Play()
Petya.Play()
Victoria.Play()
Maria.Play()

Andrey.Eat('банан', 3)
Eugene.Eat('барсук', 2)
Petya.Eat('говядина', 1)
Victoria.Eat('сено', 1)
Maria.Eat('силос', 2)

print(Andrey.IsFeeded())
print(Eugene.IsFeeded())
print(Petya.IsFeeded())
print(Victoria.IsFeeded())
print(Maria.IsFeeded())


AviaryForAmurTigers = Aviary("Вальер Амурских тигров", "Снежный", 10)
AviaryForFarEastLeopard = Aviary("Вальер Дальневосточных Леопардов", "Снежный", 10)
AviaryForAlabay = Aviary("Вальер для Алабая", "Снежный", 6)
AviaryForherbivore = Aviary("Вальер для травоядных", "Загон", 20)

AviaryForAmurTigers.AddFirstAnimal(Andrey)
AviaryForAmurTigers.AddNewAnimal(Eugene)
AviaryForAmurTigers.AddNewAnimal(Victoria)
AviaryForAmurTigers.AddNewAnimal(Petya)
AviaryForAmurTigers.AddNewAnimal(Julia)
print(AviaryForAmurTigers.animalsThatLivesHere)

AviaryForFarEastLeopard.AddFirstAnimal(Eugene)
AviaryForFarEastLeopard.AddNewAnimal(Roman)
print(AviaryForFarEastLeopard.animalsThatLivesHere)

AviaryForAlabay.AddFirstAnimal(Petya)
AviaryForAlabay.AddNewAnimal(Gennadiy)
print(AviaryForAlabay.animalsThatLivesHere)

AviaryForherbivore.AddFirstAnimal(Victoria)
AviaryForherbivore.AddNewAnimal(Eugene)
AviaryForherbivore.AddNewAnimal(Maria)
AviaryForherbivore.AddNewAnimal(Petya)
AviaryForherbivore.AddNewAnimal(Julia)
print(AviaryForherbivore.animalsThatLivesHere)

AviaryForAmurTigers.AllAnimalsMakeSounds()
AviaryForFarEastLeopard.AllAnimalsMakeSounds()
AviaryForAlabay.AllAnimalsMakeSounds()
AviaryForherbivore.AllAnimalsMakeSounds()

AviaryForAmurTigers.FeedAllAnimals(['изюбрь'], 2)
AviaryForFarEastLeopard.FeedAllAnimals(["изюбрь", "кабан", "пятнистый олень"], 2)
AviaryForAlabay.FeedAllAnimals(['говядина'], 2)
AviaryForherbivore.FeedAllAnimals(['силос', 'говядина'], 2)

AviaryForAmurTigers.MoveTheAnimalOut(Julia)
print(AviaryForAmurTigers.animalsThatLivesHere)

AviaryForFarEastLeopard.MoveTheAnimalOut(Roman)
print(AviaryForFarEastLeopard.animalsThatLivesHere)