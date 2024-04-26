def max_of_two(x, y):
    if x >= y:
        return x
    elif y> x:
        return y

    #"""Given x and y, that are 2 numbers, return the biggest number."""
    #return "ANSWER HERE" # Remove this line and implement


def max_of_three(x, y, z):
    if x >= y and y>=z:
     return x
    elif y >= x and x>=z:
        return y
    elif z >=x and x>=y:
        return z
