def greet(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greet
def say_hello():
    print("Hello, World!")

say_hello()    