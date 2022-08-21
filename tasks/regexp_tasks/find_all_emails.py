"""
Написать функцию find_emails, которая принимает текст и находит в нем
все email вида some@some.some
"""
import re


def find_emails():
    emails = input("text")
    pattern = "^.*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}.*$"
    res = re.findall(pattern, emails)

    if res:
        print('Found email')
    else:
        print("No")


find_emails()
