import re
from exceptions import NotCorrectMessage
import datetime    # в дальнейшем планирую реализовать показ сум за опредиленный промежуток времени


def parse_message(words: str):
    word = re.match(r"([\d ]+) (.*)", words)
    if not word or not word.group(0) or not word.group(1) or not word.group(2):
        raise NotCorrectMessage("Не могу понять сообщение. Напишите сообщение в формате, "
                                "например:\n1500 такси")

    amount = word.group(1).replace(" ", "")
    category_text = word.group(2).strip().lower()   # then I will make him
    return amount
