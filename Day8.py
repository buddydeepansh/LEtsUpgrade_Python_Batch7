# decorator wala program

def outer_decorator_function(fun):
    print("We are inside Outer decorator function.")
    a = int(input("Enter a range"))

    def inner_decorated_function():
        print("Inside decotrated function")

        fun(a)

    return inner_decorated_function()

def fibbo(n):
    a = 0
    b = 1
    c = a + b
    i = 0
    while i < n:
        print(a)
        c = a + b
        a = b
        b = c
        i += 1

fibbo = outer_decorator_function(fibbo)


# exception handling

file = open("abx.txt","r")
try:
    file.write("This is the text we are writing")
except:
    print("The file is opened in the read mode so you cannot write in it.")