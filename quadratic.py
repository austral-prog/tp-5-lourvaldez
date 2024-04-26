# Replace the "ANSWER HERE" for your answer
import math
def roots(a, b, c):
    numer = (b ** 2) - (4 * a * c)
    if numer < 0:
        return "( )"
    else:
        raiz = math.sqrt(numer)
        xu = (-b - raiz) / (2 * a)
        xd = (-b + raiz) / (2 * a)
        if xu == xd:
            return f"({xu})"
        else:
            return f"({xd}, {xu})"

def value_y(a, b, c, x):
    igrie = (a * (x ** 2) + b * x + c)
    return igrie


# to_string works
def to_string(a, b, c):
    if a!=0 and b!=0 and c!=0:
        return(f"f(x) = {a} * X^2 + {b} * X + {c}")
    elif a==0 and b!=0 and c!=0:
          return(f"f(x) = {b} * X + {c}")
    elif a!=0 and b!=0 and c==0:
          return(f"f(x) = {a} * X^2 + {b} * X")
    elif a==0 and b==0 and c!=0:
        return (f"f(x) = {c}")
    elif a!=0 and b==0 and c!=0:
        return(f"f(x) = {a} * X^2 + {c}")


def derivation(a, b, c):
    a = 2*a
    if a != 0 and b !=0:
        return (f"f'(x) = {a} * X + {b}")
    elif a==0 and b!=0:
        return (f"f'(x) = {b}")
    elif a!=0 and b==0:
        return (f"f'(x) = {a} * X")
    elif a==0 and b==0:
        return (f"f'(x) = 0")


