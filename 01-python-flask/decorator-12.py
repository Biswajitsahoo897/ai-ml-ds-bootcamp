def add_greetings(func):
    def wrapeer():
        print("Hello Sir!!")
        func()
        print("Goodbye Sir!!")
    return wrapeer
    
@add_greetings
def hello_user():
    print("hello world!!")        

hello_user()