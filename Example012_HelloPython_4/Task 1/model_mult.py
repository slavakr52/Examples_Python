x = 0
y = 0

def init(a, b): # чтобы передать x и y за рамки функции,
    global x    # используем global
    global y
    x = a
    y = b

def do_it():
    return x * y


