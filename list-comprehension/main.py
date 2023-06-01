friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# start_s = []

# for friend in friends:
#     # if friend[0] == "S":
#     if friend.startswith("S"):
#         start_s.append(friend)
# print(start_s)

# start_s = [friend for friend in friends if friend[0] == "S"]
start_s = [friend for friend in friends if friend.startswith("S")]
print(start_s)

# Check the ID of a list
print("friends: ", id(friends), "start_s: ", id(start_s))