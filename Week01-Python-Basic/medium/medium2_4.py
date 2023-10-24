# M 2.4 Basic decorator
# Skapa en decorator vid namn timer som skriver ut tiden det tar för en funktion att köras.
# Den ska visa exekveringstiden i sekunder. Läs på om hur man timar en funktion.
# ** ChatGPT
import time


def execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f" Start: {start_time: .2f}  End: {end_time: .2f}")
        print(f"def {func.__name__} tog {execution_time: .2f} sekunder att köra.")
        return result

    return wrapper


@execute_time
def main():
    time.sleep(2)


if __name__ == '__main__':
    main()
