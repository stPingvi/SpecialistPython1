# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
n = int(input("n= "))
from random import randint
my_list = [randint(-10, 10) for i in range(n)]
print(my_list, sum(my_list))
