friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)

print(local_friends)


local_friends = friends.difference(friends)

print(local_friends)

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)

print(friends)
