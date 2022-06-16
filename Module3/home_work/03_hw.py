# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

n = 5
numbers = []

for numb in range(n):
    numb = random.randint(-110, 100)
    numbers.append(numb)

total = 0  # Переменная для накопления суммы
for a in numbers:
    if a % 2 == 0 and a >= 0:
        total += a

print(numbers)
print("Сумма чисел =", total)
