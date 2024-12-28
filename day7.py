# Develop a parsing algorithm to detect suspicious login attempts
# If a user has more than 3 login attempts, then account lock, else log in

with open("file.txt", "r") as file:
    login_list = file.read().split()  # Splitting file content into a list of login attempts

print(login_list)

def login_check(login_list, current_user):
    count = 0
    for i in login_list:
        if i == current_user:
            count += 1
    if count >= 3:
        return "Account locked"
    else:
        return "Login successful"


username = "ram"
print(login_check(login_list, username))
