# Задача 1 на генераторы
# Ученик написал генератор show_letters(some_str),
# выводящий все символы строки на печать, но только в том случае,
# если они являются буквами (остальные игнорируются)
# def fun(str):
#     for i in str:
#         if i.isalpha():
#             yield i
# for i in fun('dsv8dv44773j'):
#     print(i)
# Задача 2
#Числа Фибоначчи представляют последовательность, получаемую в результате сложения двух предыдущих элементов.
# Начинается коллекция с чисел 1 и 1.
# Она достаточно быстро растет, поэтому вычисление больших значений занимает немало времени.
# Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов.
# def fib(n):
#     fib1 = fib2 = 1
#     print(fib1)
#     print(fib2)
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         yield fib2
# for i in fib(7):
#     print(i)
#Реализуйте итератор колоды карт (52 штуки) CardDeck.
import random
def cadrdesk():
    cadr_desk = ['2 треф', '2 бубны', '2 черви', '2 пики', '3 треф', '3 бубны', '3 черви', '3 пики', '4 треф', '4 бубны', '4 черви', '4 пики', '5 треф', '5 бубны', '5 черви', '5 пики', '6 треф', '6 бубны', '6 черви', '6 пики', '7 треф', '7 бубны', '7 черви', '7 пики', '8 треф', '8 бубны', '8 бубны', '8 черви', '8 пики', '9 треф', '9 бубны', '9 черви', '9 пики', '10 треф', '10 бубны', '10 черви', '10 пики', 'A треф', 'A бубны', 'A черви', 'A пики', 'J треф', 'J бубны', 'J черви', 'J пики', 'D треф', 'D бубны', 'D черви', 'D пики', 'K треф', 'K бубны', 'K черви', 'K пики']
    if len(cadr_desk)!=0:
        y = random.choice(cadr_desk)
        cadr_desk.remove(y)
        print(y)
        print(len(cadr_desk))
        yield cadr_desk.pop()

    else:
        yield 'StopIteration'


d = cadrdesk()
print(d.__next__())
