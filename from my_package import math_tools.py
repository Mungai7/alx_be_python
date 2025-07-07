x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Looks in Local first
    inner()

outer()  # Output: local