# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no


n = int(input('Введите размер шоколадки по первой стороне: ', ))
m = int(input('Введите размер шоколадки по второй стороне: ', ))
k = int(input('Введите на сколько долек можно разломить шоколадку по прямой : ', ))

if k < m * n and k % n == 0 or k % m == 0:
    print('yes')
else:
    print('no')
