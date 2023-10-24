# H 1.4 Repeating Decorator
# Skriv en decorator som tar in argumentet n.
# Den underliggande funktionen ska köras n gånger om den dekoreras med vår decorator.


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


def main():
    greet("Waleerat")


if __name__ == '__main__':
    main()
