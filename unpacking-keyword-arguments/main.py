# def named(**kwargs):
#     print(kwargs)


# named(name="Bob", age=25)


def named(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named(**details)
