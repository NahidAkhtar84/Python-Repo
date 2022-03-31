from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    # we have to set field(init=False) to take it as not class param and not to init.
    sort_index: int = field(init=False)
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
#! sort index added to response

# here the comparison is returning false, where it should return true
# It is not returning true cz we have not defined where to compare in data.
# we can do it sort_index variable and post_init method.
# post_init means, after initialization of the values we get.
print(person1 > person3)



