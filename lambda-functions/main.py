# Using normal functions
def add(x, y):
    return x + y


print(add(5, 7))


# Using lambda functions
add = lambda x, y: x + y

print(add(5, 7))

# Not common
print((lambda x, y: x + y)(5, 7))


# Note: lambda really difficult to read so developers dont use it often
sequence = [1, 3, 5, 9]
doubled = list(map(lambda x: x * 2, sequence))

print(doubled)
