# Funtions



# Calling of functions

def make_dough(arg1 ,arg2) :
    if arg1 =='wheat'.strip() and arg2 =='water'.strip():
        return "dough".strip()
    else:
        return "not dough"

def wood_oven(arg3) :
    if arg3 == 'bread':
        return 'Naan'
    else:
        return 'not Naan'



# Tests TDD

print(make_dough('wheat', 'water') == 'dough')
print(make_dough('sand', 'water' ) == 'not dough')

print(wood_oven('bread') == 'Naan')
print(wood_oven('brick') == 'not Naan')