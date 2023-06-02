numbers = [1, 3, 5]
doubled = []

# Long Method
for number in numbers:
    doubled.append(number * 2)

print(doubled)


# Short Method
doubled = [number * 2 for number in numbers]
print(doubled)
