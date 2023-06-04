users = [
    (0, "Bob", "password"),
    (1, "Rolf", "rolf123"),
    (2, "Jose", "password_123"),
    (3, "Aian", "Aian123"),
]


username_mapping = {user[1]: user for user in users}

print(username_mapping["Bob"])


username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# Long method
# if username_input in username_mapping:
#     if password_input == username_mapping[username_input][2]:
#         print("Logged in correctly.")
#     else:
#         print("Invalid username or password.")
# else:
#     print("Invalid username or password.")


# Short method

try:
    _, username, password = username_mapping[username_input]
    if password_input == password:
        print("Your details are correct!")
    else:
        print("Your details are incorrect!")
except KeyError:
    print("Username doesn't exist!")
