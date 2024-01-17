# def calculate_factorial(n):
#
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result
#
# def calculate_permutations(n, r):
#     result = 1
#     for i in range(r):
#         result *= n - i
#     return result
#
# # 1
# subjects = ["музыка", "математика", "русский язык", "литература", "история"]
# number_of_schedules = calculate_factorial(len(subjects))
# print(f"1. Количество различных способов составления расписания: {number_of_schedules}")
#
# # 2
# digits = ["1", "3", "7"]
# number_of_three_digit_numbers = calculate_permutations(len(digits), 3)
# print(f"2. Количество различных трёхзначных чисел: {number_of_three_digit_numbers}")
#
# # 3
# def calculate_factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result
# def calculate_permutations(n, r):
#     result = 1
#     for i in range(r):
#         result *= n - i
#     return result
# def count_odd_four_digit_numbers(digits):
#     return calculate_permutations(len(digits), 4) // 2
# digits_four = ["3", "4", "7", "6"]
# number_of_odd_four_digit_numbers = count_odd_four_digit_numbers(digits_four)
# print(f"3. Количество нечетных четырехзначных чисел: {number_of_odd_four_digit_numbers}")
#
# # 4
# def count_even_four_digit_numbers(digits):
#     return calculate_permutations(len(digits), 4) * calculate_permutations(len(digits) - 1, 3)
# digits_four = ["3", "4", "7", "6"]
# number_of_even_four_digit_numbers = count_even_four_digit_numbers(digits_four)
# print(f"4. Количество четных четырехзначных чисел: {number_of_even_four_digit_numbers}")
# import math


# import timeit
#
# def calculate_factorial(func, n):
#     result = func(n)
#     time_taken = timeit.timeit(lambda: func(n), number=100000)
#     print(f"Результат факториала: {result} - Время выполнения: {time_taken} сек.")
#     return result
#
# def calculate_error(actual, approximate):
#     return ((actual - approximate) / actual) * 100
#
# def factorial_recursive(n):
#     return 1 if n == 0 else n * factorial_recursive(n - 1)
#
# def factorial_math(n):
#     return math.factorial(n)
#
# def stirling_approximation(n):
#     return math.sqrt(2 * math.pi * n) * ((n / math.e) ** n) if n != 0 else 1
#
# def factorial_for_loop(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# n = int(input("Введите значение n для вычисления факториала: "))
#
# print("1) Рекурсивный алгоритм:")
# result_recursive = calculate_factorial(factorial_recursive, n)
#
# print("2) Алгоритм с использованием библиотеки math:")
# result_math = calculate_factorial(factorial_math, n)
#
# print("3) Алгоритм с использованием формулы Стирлинга:")
# result_stirling = calculate_factorial(stirling_approximation, n)
#
# print("4) Алгоритм с использованием цикла for:")
# result_for_loop = calculate_factorial(factorial_for_loop, n)
#
# actual_result = math.factorial(n)
#
# error_recursive = calculate_error(actual_result, result_recursive)
# error_math = calculate_error(actual_result, result_math)
# error_stirling = calculate_error(actual_result, result_stirling)
# error_for_loop = calculate_error(actual_result, result_for_loop)
#
# print(f"\nПогрешность для рекурсивного алгоритма: {error_recursive}%")
# print(f"Погрешность для алгоритма с использованием библиотеки math: {error_math}%")
# print(f"Погрешность для алгоритма с использованием формулы Стирлинга: {error_stirling}%")
# print(f"Погрешность для алгоритма с использованием цикла for: {error_for_loop}%")


# def find(s):
#     length = len(s)
#
#     for i in range(1, length):
#         current_number = int(s[:i])
#         next_expected_number = current_number + 1
#         remaining_string = s[i:]
#
#         while remaining_string.startswith(str(next_expected_number)):
#             next_expected_number += 1
#             remaining_string = remaining_string[len(str(next_expected_number - 1)):]
#
#         if not remaining_string:
#             return current_number
#
#     return int(s)
#
# print(find("123456789101112131415"))
# print(find("17181920"))
# print(find("72637236"))
# print(find("1112"))
# print(find("91011"))
# print(find("99100"))
# print(find("431243"))
# print(find("577495"))


def calculate_averages(arr):
    if not arr or len(arr) <= 1:
        return []

    averages = []
    for i in range(len(arr) - 1):
        average = (arr[i] + arr[i + 1]) // 2
        averages.append(average)

    return averages

input_array = [1, 3, 5, 1, -10]
output_array = calculate_averages(input_array)
print(output_array)
