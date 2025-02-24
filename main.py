def collinearity(x1, y1, x2, y2):
    if all(var != 0 for var in [x1, x2, y1, y2]):
        if x1 / x2 == y1 / y2:
            return True
        else:
            return False
    if x1 != 0: 
        k = x2 / x1
        if y2 == k * y1:
            return True
        else:
            return False
    if y1 != 0:
        k = y2 / y1 
        if x2 == k * x1:
            return True
        else:
            return False
    if all(var == 0 for var in [x1, x2, y1, y2]):
        return True
    if x1 * y2 - x2 * y1 == 0:
        return True
    else:
        return False
