class Person:
    species = "homo species"
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def year_born(self):
        return 2023 - self._age
    
p1 = Person("Shalom", 36)
p2 = Person("Mung", 38)

for p in [p1, p2, Person]:
    print(p.species)
#for p in [p1, p2, Person]:
#    print(p.name)
#for p in [p1, p2, Person]:
#    print(p.age)

print(p1.year_born())