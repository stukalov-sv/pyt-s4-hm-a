# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N
# Пример: при N = 12 -> [2, 3]

def get_integer_base_factors(number: int) -> list:
    factors_list = []
    div = 2

    while div * div <= number:
        if number % div == 0:
            factors_list.append(div)
            number //= div
        else:
            div += 1

    factors_list.append(number)
    return factors_list

# По примеру можно подумать, что нужны именно уникальные множители, 
# поэтому добавляю этот метод
def get_unique_number_list(int_list: list) -> list:
    result_list = []

    for item in int_list:
        if item not in result_list:
            result_list.append(item)

    return result_list


user_number = int(input('Enter number: '))
base_factors = get_integer_base_factors(user_number)
unique_base_factors = get_unique_number_list(base_factors)

print(f'Base factors of number {user_number}: {base_factors}')
print(f'Base unique factors of number {user_number}: {unique_base_factors}')
