"""
Написать функцию check_phone, которая будет принимать строку и проверять,
что она соответствует шаблону:
1. код страны +375
2. код оператора 29, 33, 44, 25 в скобках
3. три цифры
4. тире
5. две цифры
6. тире
7 две цифры

Например: +375(29)365-12-12
"""
import re


def check_phone():
    phone = input('Enter your phone number')
    pattern = "^\+375\((29|25|44|33)\)[0-9]{3}-[0-9]{2}-[0-9]{2}$"
    result = re.findall(pattern, phone)

    if result:
        print("Valid phone number")
    else:
        print("Is not phone number")


check_phone()
