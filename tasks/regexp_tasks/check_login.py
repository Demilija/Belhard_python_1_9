"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""
import re


def check_login():
    log = input('Enter your logging')
    pattern = "^[A-Z][a-z0-9_]{5,20}$"
    result = re.findall(pattern, log)
    if result:
        print("Ok logging")
    else:
        print("Logging is not valid")


check_login()
