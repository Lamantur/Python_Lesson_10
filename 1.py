
start_list = ['разработка', 'сокет', 'декоратор']


def converter(word):
    wordlist = []
    for el in word:
        wordlist.append("u"+str(hex(ord(el))).replace("x", ""))
    result = '\\'+'\\'.join(wordlist)
    return result


for el in start_list:
    print(f"Буквенный формат - {type(el)}, {el}")
    print(f"Кодовые точки - {type(converter(el))}, {converter(el)}")
