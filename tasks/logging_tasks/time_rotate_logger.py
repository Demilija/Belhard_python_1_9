"""
Настроить логгирование с модулем logging.

Настроить формат вывода.
Настроить, чтобы вывод шел в файл и в консоль.
Настроить ротацию файла лога по времени (полночь).
"""
import logging
from logging.handlers import TimedRotatingFileHandler


logging.basicConfig(
    level=logging.DEBUG,
    filename="log_journal.txt"
)
my_loger = logging.getLogger(__name__)
write_to_journal = logging.StreamHandler()
rotate_my_journal = TimedRotatingFileHandler('log_journal.txt', when='midnight')
my_loger.addHandler(write_to_journal)
my_loger.addHandler(rotate_my_journal)


for i in range(5):
    my_loger.warning("Something went wrong")
