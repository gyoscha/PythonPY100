def func_1(str_):
    str_ = str_.lower()
    str_dict = {}

    for value in str_:
        if value.isalpha():
            if value in str_dict:
                str_dict[value] += 1
            else:
                str_dict[value] = 1

    return str_dict


def func_2(str_dict):
    total_ = sum(str_dict.values())

    return {key: value / total_ for key, value in str_dict.items()}



if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """

    print(func_1(main_str))

