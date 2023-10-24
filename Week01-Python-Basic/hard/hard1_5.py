# H 1.5 Authentication Decorator
# Skriv en decorator som kollar om en användare är autentiserad eller inte.
# Om den underliggande funktionen inte kallats med password="123" ska {msg: "Not authenticated"} returneras.

def get_input_string(text):
    while True:
        user_input = input(text)
        if not user_input:
            print("Input some text")
            continue
        return user_input


def authentication(func):
    def wrapper(*args, **kwargs):
        if not (args[0] == kwargs["username"] and args[1] == kwargs["password"]):
            print("Not authenticated")
            return False

        func(args[0])

    return wrapper


@authentication
def log_in(username):
    print(f"Hello {username}. Welcome to the system.")


def main():
    username = get_input_string("Username : ")
    password = get_input_string("Password : ")

    log_in(username, password, username="username", password="123")


if __name__ == '__main__':
    main()
