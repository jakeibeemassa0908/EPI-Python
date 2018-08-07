def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car (first):
    def get(a,b):
        return a
    return first(get)

def cdr(second):
    def get(a,b):
        return b
    return second(get)

x=cons(1,2)

print(car(x))
print(cdr(x))
