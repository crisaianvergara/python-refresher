class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        """Returns a string representation of Person Object."""
        return f"Person {self.name}, {self.age} years old."

    # def __repr__(self):
    #     return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 35)

print(bob)
