# decorator is a function that can work befor other functiona and after 


def greet(fun):

    def wrapper(name):
        
        #before
        print("Welcome ")
        #under @greet function
        fun(name)
        #after
        print("World")
    
    return wrapper


@greet
def sayName(name):
    print(name)


sayName('Lynxis')