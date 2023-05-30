l = ["Bob", "Rolf", "Anne"]

t = ("Bob", "Rolf", "Anne")

s = {"Bob", "Rolf", "Anne"}

print(l[0])

print(t[1])

l[0] = "Smith"

print(l)

l.append("Smith")

print(l)

l.remove("Rolf")

print(l)

s.add("Smith")

print(s)

print(t)
