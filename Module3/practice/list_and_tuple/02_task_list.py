# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

#fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

# TODO: your code here

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

for i, fruit in enumerate(fruits):
    print(i + 1, fruit)
