from math import sqrt
from xml.dom import NoModificationAllowedErr

# Task 1
print("TASK 1")
word = 'asdfghjkl;][poiuyhgtfrdsdfvghjklpokijhgfghjmkl;]'
count = 0
letter = 'a'

count = word.count(letter)
print(count)

# Task 2 
print('TASK 2')
def cycle(r = None,
          d = None,
          S = None):
    if r is None and d is None and S is None:
        return None
    
    if type(r) is int:
        if S is None:
            S = 3.14 * r ** 2
        if d is None:
            choice = int(input('1 - через радиус, 2 - через площадь: '))
            if choice == 1:
                d = r * 2
            elif choice == 2:
                d = round(sqrt(4 * S // 3.14), 2)
            else:
                return None
    return (r, d, S)

print(cycle(r = 4))