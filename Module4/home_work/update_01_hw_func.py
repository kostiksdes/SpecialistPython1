# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    number = str(ticket_number)
    number_first = int(number[0]) + int(number[1])
    number_back = int(number[-1]) + int(number[-2])

    if number_first == number_back:
        return True
    else:
        return False

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
