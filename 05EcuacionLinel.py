#pycharm
# ecuacion lineal

import os
os.system('cls'if os.name == 'nt' else 'clear')

print('Ecuacion Lineal')
print('aX+b=0>   X=-b/a')

a=int(input("a:"))
b=int(input("b:"))

X=-b/a

print("X=",X)