def int_to_roman(num: int) -> str:
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                      100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                      10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    # Создаем переменную для хранения римского числа
    roman_num = ''

    # Проходимся по таблице и добавляем римское число, пока число не достигнет нуля
    for value, numeral in roman_numerals.items():
        while num >= value:
            roman_num += numeral
            num -= value

    return roman_num


print(int_to_roman(10))
