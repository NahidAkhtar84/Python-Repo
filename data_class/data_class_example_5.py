from dataclasses import dataclass, field

"""
#? We freeze class thus we can to be able to add extra attributes to object from outside.
"""

"""
#! We can also freeze class, If we freeze class then we will not be able to assign sort index value like we did.
"""

"""
So we have to user set attribute method.
"""

@dataclass(order=True, frozen=True)
class Person:
    # To remove sort index from response, we have to use, repr=False
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int

    def __post_init__(self):
        # self.sort_index = self.age
        object.__setattr__(self, "sort_index", self.age)

person1 = Person("Atawur vai", "Clan lead", 40)
person2 = Person("Masud Vai", "Senior Soft Engr", 28)
person3 = Person("Masud Vai", "Senior Soft Engr", 28)

print(id(person1))
print(id(person2))
print(person1)
# This gives error as we have frozen the class. 
# person1.age = 1
print(person1.job)


print(person1 > person3)

