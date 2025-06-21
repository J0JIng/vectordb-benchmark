import time 

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        print(f"--- Start: func {func.__name__} execution ---")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"    End:   func {func.__name__} execution")
        print(f"--- Elapsed: {end - start} seconds ---") 
        return result

    return inner


@timer
def greet(name: str = "world"):
    time.sleep(2)
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("Alice")