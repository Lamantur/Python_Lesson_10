words_list = ['attribute', 'класс', 'функция']
print()
for word in words_list:
    try:
        byte_word = []
        for el in word:
            bites = ord(el)
            if bites < 255:
                byte_word.append(el)
            else:
                1/0
    except:
        print(f"{word}  - Нет, нельзя записать как b''")
    else:
        print(f"{''.join(byte_word)} - Да, можно записать через b''!")
    finally:
        print()
