friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]


print(friends == abroad)

# Check the elements if they exactly the same thing
print(friends is abroad)

print(friends is friends)

friends = ["Rolf", "Bob"]
abroad = friends

print(friends is abroad)
