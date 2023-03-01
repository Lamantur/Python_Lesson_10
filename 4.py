start_list = ["разработка", "администрирование", "protocol",
              "standard"]


def encoding_list(list):
    result_list = []
    for el in list:
        result_list.append(el.encode('utf-8'))
    return result_list


def decoding_list(list):
    result_list = []
    for el in list:
        result_list.append(el.decode('utf-8'))
    return result_list


print("преобразование 1:\n")
result_list_1 = encoding_list(start_list)
print('\n'.join(map(str, result_list_1)))
print("\nобратное преобразование:\n")
result_list_2 = decoding_list(result_list_1)
print('\n'.join(map(str, result_list_2)))
