from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    # To remove sort index from response, we have to use, repr=False
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int

    def __post_init__(self):
        self.sort_index = self.age

person1 = Person("Atawur vai", "Clan lead", 40)
person2 = Person("Masud Vai", "Senior Soft Engr", 28)
person3 = Person("Masud Vai", "Senior Soft Engr", 28)

print(id(person1))
print(id(person2))
print(person1)
print(person1.job)


print(person1 > person3)

