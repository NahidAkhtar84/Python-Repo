from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    job: str
    age: int

person1 = Person("Atawur vai", "Clan lead", 40)
person2 = Person("Masud Vai", "Senior Soft Engr", 28)
person3 = Person("Masud Vai", "Senior Soft Engr", 28)

print(id(person1))
print(id(person2))
print(person1)
print(person1.job)

# If we do not use order=True in dataclass
# TypeError: '>' not supported between instances of 'Person' and 'Person'
print(person2 > person3)

"""
If we use data class as decorator we get a nice visual of the object
not a conventional object. 

We do not have to write init method to initialize parameters. 
"""

