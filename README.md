from Tiger import *
from Leopard import *
from Alabay import *

Andrey = AmurTiger('Андрей', 7, 9, 340)
Eugene = FarEastLeopard ("Евгений", 2, 6, 45)
Petya = Alabay("Петя", 3, 3, 70)

Andrey.MakeSound()
Eugene.MakeSound()
Petya.MakeSound()

Andrey.Play()
Eugene.Play()
Petya.Play()

Andrey.Eat('банан', 3)
Eugene.Eat('кабан', 2)
Petya.Eat('говядина', 1)

print(Andrey.IsFeeded())
print(Eugene.IsFeeded())
print(Petya.IsFeeded())
