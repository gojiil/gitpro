# Функция для подсчета суммы чисел от 1 до n
def sum_numbers(n):
    return sum(range(1, n+1))

# Вызов функции с n=10 и вывод результата
result = sum_numbers(10)
print("Сумма чисел от 1 до 10 равна:", result)
