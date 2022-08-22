"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""
import re


def count_words():
    text = input("Add your text here")
    lst = re.findall("\S+", text)
    print(len(lst))


count_words()
